import hashlib

users_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not username or not password:
        print("Invalid input!")
        return

    hashed = hash_password(password)
    users_db[username] = hashed
    print("User registered successfully!")

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    hashed = hash_password(password)

    if username in users_db and users_db[username] == hashed:
        print("Login successful!")
    else:
        print("Login failed!")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
