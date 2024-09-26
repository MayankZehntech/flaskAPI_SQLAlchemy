from flask import jsonify, request, abort
from ..models.models import Task
from .. import db
from datetime import datetime
import re
from app.services.validation_service import validate_name, validate_title
from sqlalchemy.exc import SQLAlchemyError



# Create Task
def create_task():
    try:
        data = request.get_json()

        if not data or not 'Name' in data or not 'Title__c' in data:
            abort(400, description="Invalid input, 'name' and 'title' are required.")

        name = request.json.get('Name')
        title = request.json.get('Title__c')

        # Validate Name and Title using service layer
        if not validate_name(name):
            abort(400, description="Task must have a non-nullable 'Name' field with valid text format.")
        if not validate_title(title):
            abort(400, description="Title must have a non-nullable 'Title__c' field with valid format.")


        new_task = Task(Name=data['Name'], Title__c=data['Title__c'])

        db.session.add(new_task)
        db.session.commit()

        return jsonify(new_task.to_dict()), 201
    
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        abort(500, description=f"An error occurred while creating the task: {str(e)}")
    
    finally:
        db.session.close()  # Close the database connection

# Get all tasks
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks]), 200
    
    except SQLAlchemyError as e:
        abort(500, description=f"An error occurred while retrieving tasks: {str(e)}")

    finally:
        db.session.close()  # Close the database connection

# Get task by id
def get_task(id):
    try:
        task = Task.query.get_or_404(id)
        return jsonify(task.to_dict()), 200

    except SQLAlchemyError as e:
        abort(500, description=f"An error occurred while retrieving the task: {str(e)}")

    finally:
        db.session.close()

# Update task
def update_task(id):
    try:
        if not request.json:
            abort(400, description="Invalid input")
        

        name = request.json.get('Name')
        title = request.json.get('Title__c')

        #data = request.get_json()
        task = Task.query.get_or_404(id)

        # Validate Name and Title using service layer
        if name and not validate_name(name):
            abort(400, description="Task must have a non-nullable 'Name' field with valid text format.")
        if title and not validate_title(title):
            abort(400, description="Title must have a non-nullable 'Title__c' field with valid format.")


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
    
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        abort(500, description=f"An error occurred while updating the task: {str(e)}")

    finally:
        db.session.close()  # Close the database connection
    

# Delete task
def delete_task(id):
    try:
        task = Task.query.get_or_404(id)

        db.session.delete(task)
        db.session.commit()

        return jsonify({"message": "Task deleted successfully"}), 200
    
    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback in case of error
        abort(500, description=f"An error occurred while deleting the task: {str(e)}")
    finally:
        db.session.close()  # Close the database connection
