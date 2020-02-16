from flask_restplus import Namespace, fields


class HealthyDTO:
    api = Namespace('health', description='API health check')
    health = api.model('health', {
        'healthy': fields.Boolean(required=True, description='Health status'),
        'message': fields.String(required=False, description='Health message')
    })
