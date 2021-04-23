import json
import os

class User:
    def __init__(self, username, password, email):
      self.username = username
      self.password = password
      self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r' , encoding='utf-8') as f:
                users = json.load(f)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email = user['email'])
                    self.users.append(newUser)

    def register(self,user: User):
        self.users.append(user)
        self.saveToFile()
        print("User Created.")

    def login(self,username,password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn == True
                self.currentUser = user
                print('Signed in')
                break
        

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Logged Out')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Not logged in')

    def saveToFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open('users.json','w') as f:
            json.dump(list,f)


repository = UserRepository()

while True:
    print('Menu'.center(50,"*"))
    choise = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nYour Choise: ")
    if choise == '5':
        break
    else:
        if choise == '1':
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username=username,password=password,email=email)
            repository.register(user)
        elif choise == '2':
            if repository.isLoggedIn:
                print('Already Logged In')
            else:
                username = input('username: ')
                username = input('password: ')
                repository.login(username,password)
        elif choise == '3':
            repository.logout()
        elif choise == '4':
            repository.identity()
        else:
          print('Wrong Choise')