from flask_restplus import Resource
from backend.main.services.health_service import check_health
from backend.main.dtos import HealthyDTO

api = HealthyDTO.HealthyDTO.api
dto = HealthyDTO.HealthyDTO.health


@api.route('/')
class Healthy(Resource):
    @api.doc('Check health of the API')
    @api.marshal_with(dto)
    def get(self):
        return check_health()
