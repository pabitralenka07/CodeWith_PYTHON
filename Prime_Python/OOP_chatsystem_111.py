class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, chatroom, text):
        msg = Message(self.name, text)
        chatroom.add_message(msg)

class ChatRoom:
    def __init__(self):
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(user.name, "joined the chat")

    def leave(self, user):
        self.users.remove(user)
        print(user.name, "left the chat")

    def add_message(self, message):
        self.messages.append(message)

    def show_chat(self):
        print("\nChat History:")
        for msg in self.messages:
            print(msg.sender + ":", msg.text)


u1 = User("Amit")
u2 = User("Sneha")

room = ChatRoom()

room.join(u1)
room.join(u2)

u1.send_message(room, "Hello!")
u2.send_message(room, "Hi!")

room.show_chat()

room.leave(u1)
