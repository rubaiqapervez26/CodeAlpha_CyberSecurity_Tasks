# insecure_app.py

import os

# Fake database (dictionary)
users_db = {
    "admin": "admin123",
    "user1": "password1"
}

def login():
    print("=== Login System ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # No validation
    if username in users_db:
        if users_db[username] == password:
            print("Login successful!")
            save_login(username, password)
        else:
            print("Incorrect password!")
    else:
        print("User not found!")

def save_login(username, password):
    # Insecure file handling
    file = open("log.txt", "a")
    file.write(f"{username}:{password}\n")
    file.close()

def register():
    print("\n=== Register User ===")
    username = input("Choose username: ")
    password = input("Choose password: ")

    # No validation or checks
    users_db[username] = password

    # Saving in file (plaintext)
    file = open("users.txt", "a")
    file.write(username + ":" + password + "\n")
    file.close()

    print("User registered successfully!")

def view_users():
    print("\n=== All Users ===")
    # No access control
    for user, pwd in users_db.items():
        print(f"Username: {user}, Password: {pwd}")

def delete_user():
    print("\n=== Delete User ===")
    username = input("Enter username to delete: ")

    # No authentication check
    if username in users_db:
        del users_db[username]
        print("User deleted!")
    else:
        print("User not found!")

def main():
    while True:
        print("\n1. Login")
        print("2. Register")
        print("3. View Users")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            view_users()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
