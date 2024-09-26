from flask import jsonify

def handle_404_error(error):
    response = jsonify({
        'message': str(error.description), 
        'status_code': 404
    })
    response.status_code = 404
    return response

def handle_400_error(error):
    response = jsonify({
        'message': str(error.description),
        'status_code': 400
    })
    response.status_code = 400
    return response
