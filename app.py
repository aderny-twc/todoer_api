from flask import Flask, jsonify

from mysqlcm import UseDataBase


app = Flask(__name__)

#Database configuration
app.config['dbconfig'] = {'host': 'localhost',
                            'user': 'todoerAPI',
                            'password': 'todoerAPIpasswd',
                            'database': 'todoerAPIdb',}

app.config['data_list'] = ['task_id',
                            'title',
                            'description',
                            'done',
                            'created_at']


def db_data_modifier(key_list, contents) -> list:
    """
    Creates a list of dictionaries with keys passed as an argument.
    """
    if len(contents[0]) == len(key_list):
        data_list = []
        for row_data in contents:
            data_list.append(dict(zip(key_list, row_data)))
        return data_list
    else:
        return None


#Getting all tasks for user
@app.route('/todoer/api/tasks', methods=['GET'])
def get_tasks():
    with UseDataBase(app.config['dbconfig']) as cursor:
        _SQL = """
                SELECT task_id, title, description, done, created_at
                FROM tasks
                WHERE user_id = %s
                """
        cursor.execute(_SQL, (1,))
        contents = cursor.fetchall()
    tasks_data = db_data_modifier(app.config['data_list'], contents)

    return jsonify({'taskgs': tasks_data})


@app.route('/todoer/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    with UseDataBase(app.config['dbconfig']) as cursor:
        _SQL = """
                SELECT task_id, title, description, done, created_at
                FROM tasks
                WHERE user_id = %s AND task_id = %s
                """
        cursor.execute(_SQL, (1, task_id))
        contents = cursor.fetchall()
    if not contents:
        return jsonify({'error': 'Not Found'})
    else:
        tasks_data = db_data_modifier(app.config['data_list'], contents)
    
    return jsonify({'taskgs': tasks_data})


if __name__ == '__main__':
    app.run(debug=True)
