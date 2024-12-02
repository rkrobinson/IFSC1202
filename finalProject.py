import re

# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# UserList class
class UserList:
    def __init__(self, filename):
        self.user_list = []
        self.filename = filename
        self.read_user_file()

    def read_user_file(self):
        """Reads usernames and passwords from the file."""
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.user_list.append(User(username, password))
        except FileNotFoundError:
            # File does not exist; initialize an empty user list
            print(f"File '{self.filename}' not found. Starting with an empty user list.")

    def write_user_file(self):
        """Writes usernames and passwords to the file."""
        with open(self.filename, 'w') as file:
            for user in self.user_list:
                file.write(f"{user.username},{user.password}\n")

    def display_user_list(self):
        """Displays the list of users with their passwords."""
        if not self.user_list:
            print("\nNo users in the system.")
            return
        print("\nUsername        Password")
        print("--------------- ---------------")
        for user in self.user_list:
            print(f"{user.username:15} {user.password}")
        print()

    def find_username(self, username):
        """Finds the index of a username in the list."""
        for i, user in enumerate(self.user_list):
            if user.username == username:
                return i
        return -1

    def add_user(self, username, password):
        """Adds a new user."""
        if self.find_username(username) == -1:
            self.user_list.append(User(username, password))
            return True
        return False

    def delete_user(self, username):
        """Deletes a user."""
        index = self.find_username(username)
        if index != -1:
            del self.user_list[index]
            return True
        return False

    def change_password(self, username, password):
        """Changes the password of an existing user."""
        index = self.find_username(username)
        if index != -1:
            self.user_list[index].password = password
            return True
        return False

    def strength(self, password):
        """Calculates the strength of a password."""
        score = 0
        if len(password) >= 8:
            score += 1
        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'[0-9]', password):
            score += 1
        if re.search(r'[~!@#$%^&*()_+|\-={}[\]:;<>?/]', password):
            score += 1
        return score


# Main program
def main():
    userlist = UserList("users.txt")
    while True:
        print("\nMenu:")
        print("1) Add a New User")
        print("2) Delete an Existing User")
        print("3) Change Password on an Existing User")
        print("4) Display All Users")
        print("5) Save Changes to File")
        print("6) Quit")
        selection = input("Enter Selection: ").strip()

        if selection == "1":
            username = input("Enter username: ").strip()
            if userlist.find_username(username) != -1:
                print("Error: Username already exists.")
                continue
            while True:
                password = input("Enter password: ").strip()
                strength = userlist.strength(password)
                if strength < 5:
                    print(f"This password is weak - {strength}. Try again.")
                else:
                    break
            userlist.add_user(username, password)
            print("User Added")

        elif selection == "2":
            username = input("Enter username to delete: ").strip()
            if userlist.delete_user(username):
                print("User Deleted")
            else:
                print("Error: Username not found.")

        elif selection == "3":
            username = input("Enter username to change password: ").strip()
            if userlist.find_username(username) == -1:
                print("Error: Username not found.")
                continue
            while True:
                password = input("Enter new password: ").strip()
                strength = userlist.strength(password)
                if strength < 5:
                    print(f"This password is weak - {strength}. Try again.")
                else:
                    break
            userlist.change_password(username, password)
            print("Password Changed")

        elif selection == "4":
            userlist.display_user_list()

        elif selection == "5":
            userlist.write_user_file()
            print("Changes Saved")

        elif selection == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid Selection. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
