from database import db

users = db

def login(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Logged in")
            return user
    print("Wrong username or password")
    return False

def signup(username, password, name, surname, age, gender, balance=0):
    for user in users:
        if user['username'] == username:
            print("Username already exists")
            return False
    user = {
        'username': username,
        'password': password,
        'name': name,
        'surname': surname,
        'age': age,
        'gender': gender,
        'balance': balance
    }
    users.append(user)
    print("User successfully created")
    return user

def withdraw(user, money):
    if user['balance'] >= money:
        user['balance'] -= money
        print("New balance:", user["balance"])
        return True
    else:
        print("You don't have enough balance.")
        return False

def deposit(user, money):
    user['balance'] += money
    print("Your new balance:", user['balance'])
    return True

def admin():
    print("Username , Name , Surname , Age , Gender , Balance")
    for user in users:
        print(user['username'], " ", user['name'], " ", user['surname'], " ", user['age'], " ", user['gender'], " ", user['balance'])


while True:
    print("1. Login")
    print("2. Sign up")
    print("3. Admin")
    button = input('> ')
    if button == '1':
        username = input("Username: ")
        password = input("Password: ")
        user = login(username, password)
        if user:
            print("Logged in as:", user['name'], user['surname'])
            print("Balance:", user['balance'])
            print("What do you want to do?")
            print("1. Withdraw")
            print("2. Deposit")
            choice = input("> ")
            if choice == "1":
                money = int(input("Amount to withdraw: "))
                withdraw(user, money)
            elif choice == "2":
                money = int(input("Amount to deposit: "))
                deposit(user, money)
    elif button == '2':
        username = input("Username: ")
        password = input("Password: ")
        name = input("Name: ")
        surname = input("Surname: ")
        age = input("Age: ")
        gender = input("Gender: ")
        balance = int(input("Balance: "))
        user = signup(username, password, name, surname, age, gender, balance)
        if user:
            print("Signed up as:", user['name'], user['surname'])
            print("Balance:", user['balance'])
    elif button =='3':
        username=input("Username:")
        password=input("Password:")
        if username == 'admin' and password == 'admin':
            admin()
        else:
            print("You are not admin!!")    
   
   
