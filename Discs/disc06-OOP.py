#!/usr/bin/python3


"""
1.2
"""

class Email():
    def __init__(self,msg,sender_name,recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server():
    def __init__(self):
        self.clients = {}
    
    def send(self,email):
        self.clients[email.recipient_name].recive(email)


    def register_client(self.client,client_name):
        self.client[client_name] = client


class Client():
    def __init__(self,server,name):
        self.inbox = []
 
    def compose(self,msg,recipient_name):
        sending_email = Email(msg,name,recipient_name)
        Server.send(sending_email)
        

    def receive(self,email):
        self.inbox += [email]


"""
2.1
"""

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init(self,name,owner)
        self.lives = 9

    def talk(self):
        print("{0} says meow".format(self.name))

    def lose_life(self):
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False

class NoisyCat(Cat):
    def talk(self):
        print("{0} says meow".format(self.name))
        print("{0} says meow".format(self.name))
        

#Nonlocal没什么新思路的题，不做了。


