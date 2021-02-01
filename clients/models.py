import uuid

class Client:

    def __init__(self, name, company, email, position, uid= uuid.uuid4()):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid

    
    def to_dict(self):
        return vars(self)

    
    @staticmethod
    def schema():
        return ['name','company','email','position','uid']