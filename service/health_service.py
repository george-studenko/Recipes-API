from flask import jsonify


class Health_Service():
    def check_health(self):
        return jsonify({'healthy': True,
                            'message': 'Service is up and running'}
                           )