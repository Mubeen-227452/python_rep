class user:
    def __init__(self, fname, lname):
        self.__fname = fname
        self.__lname = lname

    def get_full_name(self):
        return self.__fname + " " + self.__lname

    def user_login(self, username):
        print("Access Granted")

    def user_work(self):
        print(self.__fname + " is working")


class superUser(user):
    def __init__(self, fname, lname):
        user.__init__(self, fname, lname)


    def super_user_work(self):
        print("Performing well")


su1 = superUser("Mub","diwa")
print(su1.get_full_name())
