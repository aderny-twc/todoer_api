from flask import Flask, jsonify, make_response, request

from db_pack.db_comm import DbApiTeller


app = Flask(__name__)

### CONFIGURATION
#DB configuration
app.config['db_config'] = {'host': 'localhost',
                            'user': 'todoerAPI',
                            'password': 'todoerAPIpasswd',
                            'database': 'todoerAPIdb',}

#Table fields
app.config['data_fields'] = ['task_id',
                            'title',
                            'description',
                            'done',
                            'created_at']

#User id (palceholder)
USER_ID = 1
#Tasks table
TABLE_NAME = 'tasks'

#DB object
db_teller = DbApiTeller(config=app.config['db_config'],
                        user_id=USER_ID,
                        table_name=TABLE_NAME,
                        fields=app.config['data_fields'])


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
    contents = db_teller.get_data()
    tasks_data = db_data_modifier(app.config['data_fields'], contents)

    return jsonify({'taskgs': tasks_data})


#Getting a single task
@app.route('/todoer/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    contents = db_teller.get_data(task_id)
    #print(task_id)
    if not contents:
        return make_response(jsonify({'error': 'Not Found'}), 404)
    else:
        tasks_data = db_data_modifier(app.config['data_fields'], contents)
    
    return jsonify({'taskgs': tasks_data})


#Adding a new task
@app.route('/todoer/api/tasks', methods=['POST'])
def create_task():
    if (not request.json
        or not 'title' in request.json
        or not 'description' in request.json):
        abort(400)

    task = {
            'title': request.json['title'],
            'description': request.json['description'],
            'done': str(request.json.get('done', 0)),
            'user_id': USER_ID,
            }
    db_teller.post_data(task) 
    #print(task)
    return jsonify({'task': task}), 201


if __name__ == '__main__':
    app.run(debug=True)
