from Modules.user import User

class Admin(User):
    def __init__(self, FN, LN, UN, Pass):
        super().__init__(FN, LN, UN, Pass)