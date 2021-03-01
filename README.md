# Flask REST api
flask api service for to-do lists (Work in progress...)

## Models fields

### Tasks

| Field       | Type    |
| :---------- | ------- |
| task_id     | int     |
| title       | varchar |
| description | varchar |
| done        | bool    |
| created_at  | date    |
| user_id     | int FK  |

### Users

| Field      | Type    |
| :--------- | ------- |
| user_id    | int     |
| first_name | varchar |
| last_name  | varchar |
| password   | varchar |

## views

| Route                           | Method | Action                       |
| ------------------------------- | ------ | ---------------------------- |
| /todoer/api/tasks               | GET    | Getting all tasks by user_id |
| /todoer/api/tasks/<int:task_id> | GET    | Gettong a single task        |
| /todoer/api/tasks               | POST   | Creating a task              |
| /todoer/api/tasks/<int:task_id> | PUT    | Updating by task_id          |
| /todoer/api/tasks/<int:task_id> | DELETE | Deleting by task_id          |

## Project structure

```
doer_api/
├── app.py
├── db_pack
│   ├── db_comm.py
│   ├── __init__.py
│   └── mysqlcm.py
├── README.md
└── requirements.txt
```

## Application launch

### Installation

```
$ git clone https://github.com/aderny-twc/todoer_api.git
$ cd todoer_api/
$ python -m venv venv
$ source venv/bin/activate
(venv) pip install -r requirements.txt
```

### Database configuration

MySQL/MariaDB by default

```python
app.config['db_config'] = {'host': 'localhost',
                            'user': 'todoerAPI',
                            'password': 'todoerAPIpasswd',
                            'database': 'todoerAPIdb',}
```

### Run

```
(venv) python app.py
```