from admin_setup import AdminDeAndSerializing

class Admin_():
    def __init__(self, name: str,password: str):
        self.name = name
        self.password = password
    

    @staticmethod
    def read():
        admin_deserializ = AdminDeAndSerializing.read()
        return Admin_(admin_deserializ.name, admin_deserializ.password)


