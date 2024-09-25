from flask import Blueprint, jsonify, request, abort
from . import db
from .models import Task
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    message = {
        "message": "Welcome to the TodoList API!",
        "routes": {
            "get_all_tasks": "/TodoLists [GET]",
            "get_task_by_id": "/TodoLists/<id> [GET]",
            "create_task": "/TodoLists [POST]",
            "update_task": "/TodoLists/<id> [PUT]",
            "delete_task": "/TodoLists/<id> [DELETE]"
        }
    }
    return jsonify(message)

# Create Task
@main.route('/TodoLists', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or not 'Name' in data or not 'Title__c' in data:
        abort(400, description="Invalid input, 'name' and 'title' are required.")

    new_task = Task(Name=data['Name'], Title__c=data['Title__c'])

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

# Get all tasks
@main.route('/TodoLists', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Get task by id
@main.route('/TodoLists/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict()), 200

# Update task
@main.route('/TodoLists/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)

    if 'Name' in data:
        task.Name = data['Name']
    if 'Title__c' in data:
        task.Title__c = data['Title__c']

    task.created_at = datetime.now()
    db.session.commit()

    return jsonify(task.to_dict()), 200

# Delete task
@main.route('/TodoLists/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"}), 200
