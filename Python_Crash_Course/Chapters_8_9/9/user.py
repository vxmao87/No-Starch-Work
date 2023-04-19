# 9-11
# 9-3
class User:
    """
    A typical but simplified Internet user.
    """
    def __init__(self, first_name, last_name, age, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        """
        Describes the user.
        """
        print(f"User: {self.first_name} {self.last_name} ({self.age}) - {self.username}")

    def greet_user(self):
        """
        Greets the user with a personalized message.
        """
        print(f"Welcome back {self.username}! Another great day!")

    # 9-5
    def increment_login_attempts(self):
        """
        Increases the number of login attempts on the account by 1.
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """
        Resets the number of login attempts on an account.
        """
        self.login_attempts = 0
