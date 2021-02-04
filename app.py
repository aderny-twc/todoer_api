from flask import Flask, jsonify


app = Flask(__name__)

app.config['dbconfig'] = {'host': 'loclalhost',
                            'user': 'todoerAPI',
                            'password': 'todoerAPIpasswd',
                            'database': 'todoerAPIdb',}


@app.route('/todoer/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'task': 1})




if __name__ == '__main__':
    app.run(debug=True)
