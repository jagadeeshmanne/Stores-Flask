from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 400

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': "Store with name '{}' already exists.".format(name)}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred creating the store.'}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': f"Store with name '{name}' deleted"}, 200


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}