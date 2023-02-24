from datetime import datetime

class Chat:
    pass
    #def __init__(self, ):
    # Ваш код здесь



class Message:
    def __init__(self, text, user='Anonym'):
        self.text = text
        if user in users:    # such user exists in our base
            self.user = user
        else:
            self.user = User(user)
        
    def show(self):
        print(f'{self.user.login}: {self.text}')
        
    def send(self):
        pass
    

users = {} # dictionary of objects of class User()

class User:
    def __init__(self, login, name='Unknown', city='Unknown', birthdate='Unknown', history=None):
        if login not in users:
            self.login = login # creating object of class
            self.name = name
            self.city = city
            self.birthdate = birthdate
            self.history = history
            users[login] = self # adding object to dictionary of users using login as a key
        else:
            print('User with such login already exists! Login has to be unique.')
            
    
    def print_user_info(self): # output all known information about user
        print(f'User: {self.login}\nName: {self.name}\nCity: {self.city}\nBirthdate: {self.birthdate}')
        
    #def __del__(self): # function for deleting user from dictionary
    #    users.pop(self.login, None)
    #    print(f'User {self.login} deleted')
    
    def print_all_users():
        print(users)
        
        
        
user1 = User('Amy')

user1.print_user_info()

msg1 = Message('Hi', 'Kate')
msg1.show()

User.print_all_users()