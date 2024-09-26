from flask import jsonify, request, abort
from ..models.models import Task
from .. import db
from datetime import datetime

# Create Task
def create_task():
    data = request.get_json()

    if not data or not 'Name' in data or not 'Title__c' in data:
        abort(400, description="Invalid input, 'name' and 'title' are required.")

    new_task = Task(Name=data['Name'], Title__c=data['Title__c'])

    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

# Get all tasks
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Get task by id
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict()), 200

# Update task
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
def delete_task(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"}), 200
