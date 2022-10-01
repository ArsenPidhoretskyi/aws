from models import User


class UserSummary:
    def __init__(self, user: User):
        self.id = user.id
        self.firstName = user.firstName
        self.lastName = user.lastName
        self.email = user.email

    def asDict(self):
        return vars(self)
