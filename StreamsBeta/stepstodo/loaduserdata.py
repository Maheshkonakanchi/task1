from utils import XLutils

path = "C:\\Users\\Mahesh.K\\PycharmProjects\\git hub projects\\StreamsBeta\\inputfiles\\userdetails.xlsx"
class userinfo:
    def getuserdetails(self):
        for r in range(2, 6, 1):
            username = XLutils.getuser(path, "users_sheet", r, 1)
            password = XLutils.getuser(path, "users_sheet", r, 2)
            print(username)
            print(password)


a = userinfo()
a.getuserdetails()
