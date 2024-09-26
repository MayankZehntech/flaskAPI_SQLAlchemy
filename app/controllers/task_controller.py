from flask import jsonify, request, abort
from ..models.models import Task
from .. import db
from datetime import datetime
import re


# Validate 'Name' field
def validate_name(name):
    if not name or not isinstance(name, str) or not re.match("^[A-Za-z ]+$", name):
        abort(400, description="Task must have a non-nullable 'Name' field with valid text format.")

# Validate 'Title__c' field
def validate_title(title):
    if not title or not isinstance(title, str) or not re.match("^[A-Za-z0-9 ]+$", title):
        abort(400, description="Title must have a non-nullable 'Title__c' field with valid format.")



# Create Task
def create_task():
    data = request.get_json()

    if not data or not 'Name' in data or not 'Title__c' in data:
        abort(400, description="Invalid input, 'name' and 'title' are required.")

    name = request.json.get('Name')
    title = request.json.get('Title__c')

    # Validate Name and Title
    validate_name(name)
    validate_title(title)

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
    if not request.json:
        abort(400, description="Invalid input")
    

    name = request.json.get('Name')
    title = request.json.get('Title__c')

    #data = request.get_json()
    task = Task.query.get_or_404(id)

    # Validate inputs
    if name:
        validate_name(name)
    if title:
        validate_title(title)

    # Update task details
    if name:
        task.Name = name
    if title:
        task.Title__c = title

    # if 'Name' in data:
    #     task.Name = data['Name']
    # if 'Title__c' in data:
    #     task.Title__c = data['Title__c']

    task.created_at = datetime.now()
    db.session.commit()

    return jsonify(task.to_dict()), 200

# Delete task
def delete_task(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"}), 200
