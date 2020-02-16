from flask_restplus import Namespace, fields


class CategoryDTO:
    api = Namespace('category', description='Category resource')
    category = api.model('category', {
        'name': fields.String(required=True, description='Category name'),
        'description': fields.String(required=False, description='Category description'),
        'slug': fields.String(required=False, description='Category url'),
        'language': fields.String(required=False, description='Category language'),

    })
