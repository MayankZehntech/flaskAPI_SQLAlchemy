import re
from flask import jsonify

# Validation for 'Name' field
def validate_name(name):
    if not name or not isinstance(name, str) or not re.match("^[A-Za-z ]+$", name):
        return False
    return True

# Validation for 'Title__c' field
def validate_title(title):
    if not title or not isinstance(title, str) or not re.match("^[A-Za-z0-9 ]+$", title):
        return False
    return True

# Error handler for 404 not found
def handle_404_error(error):
    response = jsonify({
        'message': str(error.description),
        'status_code': 404
    })
    response.status_code = 404
    return response

# Error handler for 400 bad request
def handle_400_error(error):
    response = jsonify({
        'message': str(error.description),
        'status_code': 400
    })
    response.status_code = 400
    return response
