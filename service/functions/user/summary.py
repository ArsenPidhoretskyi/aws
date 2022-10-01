from models import User
from db_summary import ObjectSummary


class UserSummary(ObjectSummary[User]):
    def __init__(self, user: User):
        super(UserSummary, self).__init__(user)

        self.firstName = user.firstName
        self.lastName = user.lastName
        self.email = user.email

    def asDict(self):
        return vars(self)
