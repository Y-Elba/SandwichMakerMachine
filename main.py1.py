class Message:

    def __init__(self, msg):
        self.msg = msg

    def printing_message(self):
        print(self.msg)


message_object = Message("Hello Class")

message_object.printing_message(),
