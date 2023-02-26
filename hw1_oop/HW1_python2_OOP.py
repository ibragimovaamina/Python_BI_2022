from datetime import datetime


class Chat:
    default_start = datetime(1970, 1, 1)
    
    def __init__(self):
        self._chat_history = []    # List of all messages in chat
            
    def show_last_message(self):
        last_message = self._chat_history[0]
        print(last_message.show())
    
    def get_history_from_time_period(self, start=None, end=None):
        if start is None:
            start = self.default_start
        if end is None:
            end = datetime.now()
        self.start = start
        self.end = end
                
        for message in self._chat_history:
            if self.end >= message.datetime >= self.start:
                print(message.show())           
    
    def show_chat(self, separator='\n'):
        print(*[message.show() for message in self._chat_history], sep=separator)
       
    def _recieve(self, message):
        if isinstance(message, Message):
            message.datetime = datetime.now()    # Set attribute datetime when message is recieved by chat
            self._chat_history.insert(0, message)


class Message:
    def __init__(self, text, user):
        self.user = user
        self.text = text  
        self.datetime = None     # Will set this attribute after sending message to chat
                
    def show(self):
        if self.datetime:
            return f'{self.datetime} {self.user}: {self.text}'
        else:
            return f'{self.user}: {self.text}'
        
    def send(self, chat):
        if isinstance(chat, Chat):
            chat._recieve(self)

    
class User:
    all_users = []    # List of all objects of class User
    
    def __init__(self, login, name='Unknown', city='Unknown', birthdate='Unknown'):
        self.login = login
        self.name = name
        self.city = city
        self.birthdate = birthdate
        self.history = None    # Add method for this later!
        self.all_users.append(self)
    
    def print_user_info(self):    # Print all information about user
        print(f'User: {self.login}\nName: {self.name}\nCity: {self.city}\nBirthdate: {self.birthdate}')
        
    def print_all_users():
        for user in User.all_users:
            print(user.login)      