

from flask_restful import Resource

from .Users import Users
class Users_(Resource):
    def get(self):
        info = Users.query.all()
        s = ""
        for i in info:
            s+= str(i.id) + " name " + str(i.name)

        return { "data": s }

