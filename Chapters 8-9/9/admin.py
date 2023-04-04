# 9-12
from user import User

# 9-8
class Privileges:
    """
    A class on privileges of the admin account.
    """
    def __init__(self):
        self.privileges_list = [
            "can add posts",
            "can delete posts",
            "can ban users",
            "can see how frequently a post has been clicked on",
            "can design new features"
        ]

    def show_privileges(self):
        """
        Displays the admin account's privileges.
        """
        print("This admin account has the following privileges:")
        for privilege in self.privileges_list:
            print(f"-- {privilege}")

# 9-7
class Admin(User):
    """
    The highest form of user.
    """
    def __init__(self, first_name, last_name, age, username):
        super().__init__(first_name, last_name, age, username)
        self.privileges = Privileges()