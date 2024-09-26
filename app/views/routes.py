from flask import Blueprint
from ..controllers.task_controller import create_task, get_tasks, get_task, update_task, delete_task

task_bp = Blueprint('task_bp', __name__)

# Route for creating a new task
@task_bp.route('/TodoLists', methods=['POST'])
def create():
    return create_task()

# Route for fetching all tasks
@task_bp.route('/TodoLists', methods=['GET'])
def fetch_all():
    return get_tasks()

# Route for fetching a specific task by id
@task_bp.route('/TodoLists/<int:id>', methods=['GET'])
def fetch_one(id):
    return get_task(id)

# Route for updating a task
@task_bp.route('/TodoLists/<int:id>', methods=['PUT'])
def modify(id):
    return update_task(id)

# Route for deleting a task
@task_bp.route('/TodoLists/<int:id>', methods=['DELETE'])
def remove(id):
    return delete_task(id)
