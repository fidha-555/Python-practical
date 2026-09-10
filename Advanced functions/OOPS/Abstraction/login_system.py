from abc import ABC , abstractmethod
class LoginSystem(ABC):
    def __verify_user(self,username):
        print(f"Verifying username:{username}")
        return True
    def __check_password(self,password):
        print(f"Checking Password:{password}")
        return True
    def login(self,username,password):
        if self.__verify_user(username) and self.__check_password(password):
            self.post_login_action(username)
        else:
            print("Authentication failed.")
    @abstractmethod
    def post_login_action(self,username):
        pass
class PortalLogin(LoginSystem):
    def post_login_action(self,username):
        print(f"Welcome back,{username}! Redirecting to dashboard...")
PortalLogin().login("user","pass123")