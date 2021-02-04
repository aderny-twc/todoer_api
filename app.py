from flask import Flask, jsonify

from mysqlcm import UseDataBase


app = Flask(__name__)

app.config['dbconfig'] = {'host': 'localhost',
                            'user': 'todoerAPI',
                            'password': 'todoerAPIpasswd',
                            'database': 'todoerAPIdb',}


@app.route('/todoer/api/tasks', methods=['GET'])
def get_tasks():
    with UseDataBase(app.config['dbconfig']) as cursor:
        _SQL = """
                SELECT task_id, title, description, done, created_at
                FROM tasks
                WHERE user_id = 1
                """
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    key_list = ['task_id', 'title', 'description', 'done', 'created_at']
    tasks_data = []
    for row_data in contents:
        tasks_data.append(dict(zip(key_list, row_data)))

    return jsonify(tasks_data)



if __name__ == '__main__':
    app.run(debug=True)
