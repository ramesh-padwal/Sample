import pytest
from Configurations.loginconfig import Credentials
class Test_Login:
    # def __init__(self):
    #     credObj = Credentials()
    #     self.username = credObj.Username
    #     self.password = credObj.Password

    def test_login(self):
        if Credentials.Username=="Ramesh" and Credentials.Password=="Admin":
            print("Login is successful!")
            assert True
        else:
            print("Invalid Credentials")
            assert False



