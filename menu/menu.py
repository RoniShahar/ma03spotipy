from consolemenu import *
from consolemenu.items import *
from user.user import *


def login_menu():
    menu = ConsoleMenu("Login")
    login_item = FunctionItem("Login", check_if_user_exist)
    menu.append_item(login_item)
    menu.show()


