from user import User


class UserRepository:
    def __init__(self, db, user, password):
        self.db = db
        self.user = user
        self.password = password

    def save_to_database(self, user: "User"):
        print(f"{user.name} is getting saved to database")

    def delete_from_database(self, user: "User"):
        print(f"{user.name} is getting deleted from database")
