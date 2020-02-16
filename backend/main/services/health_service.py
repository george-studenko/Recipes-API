def check_health():
    response = {'healthy': True,
                'message': 'Service is up and running'}
    return response, 200
