import re
class User:
    def __init__(self, username, password):
        self.UserName = username
        self.Password = password
class UserList:
    def __init__(self, filename):
        self.filename = filename
        self.Userlist = []
        self.ReadUserFile()
    def ReadUserFile(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.Userlist.append(User(username, password))
        except FileNotFoundError:
            print("File not found, starting with an empty user list.")
    def WriteUserFile(self):
        with open(self.filename, "w") as file:
            for user in self.Userlist:
                file.write(f"{user.UserName},{user.Password}\n")
    def DisplayUserList(self):
        print(f"{'Username':<15}{'Password':<15}")
        print("-" * 30)
        for user in self.Userlist:
            print(f"{user.UserName:<15}{user.Password:<15}")
    def FindUsername(self, username):
        for index, user in enumerate(self.Userlist):
            if user.UserName == username:
                return index
        return -1
    def ChangePassword(self, username, password):
        index = self.FindUsername(username)
        if index != -1:
            self.Userlist[index].Password = password
    def AddUser(self, username, password):
        if self.FindUsername(username) == -1:
            self.Userlist.append(User(username, password))
    def DeleteUser(self, username):
        index = self.FindUsername(username)
        if index != -1:
            del self.Userlist[index]
    def Strength(self, password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(char.isupper() for char in password):
            strength += 1
        if any(char.islower() for char in password):
            strength += 1
        if any(char.isdigit() for char in password):
            strength += 1
        if any(char in "~!@#$%^&*()_+|-={}[]:;<>?/" for char in password):
            strength += 1
        return strength
user_list = UserList("Final Project Passwords.txt")
while True:
    print("\nMenu:")
    print("1) Add a New User")
    print("2) Delete an Existing User")
    print("3) Change Password on an Existing User")
    print("4) Display All Users")
    print("5) Save Changes to File")
    print("6) Quit")
    selection = input("Enter Selection: ")
    if selection == "1":
        username = input("Enter User ID: ")
        if user_list.FindUsername(username) != -1:
            print("Username Already Exists")
        else:
            while True:
                password = input("Enter Password: ")
                strength = user_list.Strength(password)
                if strength < 5:
                    print(f"This password is weak - {strength}")
                else:
                    user_list.AddUser(username, password)
                    print("User Added")
                    break
    elif selection == "2":
        username = input("Enter User ID: ")
        if user_list.FindUsername(username) == -1:
            print("Username Not Found")
        else:
            user_list.DeleteUser(username)
            print("User Deleted")
    elif selection == "3":
        username = input("Enter User ID: ")
        if user_list.FindUsername(username) == -1:
            print("Username Not Found")
        else:
            while True:
                password = input("Enter New Password: ")
                strength = user_list.Strength(password)
                if strength < 5:
                    print(f"This password is weak - {strength}")
                else:
                    user_list.ChangePassword(username, password)
                    print("Password Changed")
                    break
    elif selection == "4":
        user_list.DisplayUserList()
    elif selection == "5":
        user_list.WriteUserFile()
        print("Changes Saved")
    elif selection == "6":
        print("Exiting Program")
        break
    else:
        print("Invalid Selection")
