
class ShowUsersCommand:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self):
        users = self.user_repository.get_all_users()
        if not users:
            print("No users available.")
            return

        for user in users:
            print(f"Username: {user.username}, FullName: {user.firstname} {user.lastname}, Role: {user.role.name}")
