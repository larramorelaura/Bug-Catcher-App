from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user
DATABASE = 'private_wall'


class Message:
    DB = 'private_wall'
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.sender = data['sender']
        self.reciever = data['receiver']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_user_messages(cls,data):

        # Fetch the user to associate with all the message objects
        receiver = user.User.get_by_id(data)

        # Query for all messages, with the sender's user data
        query = """SELECT messages.*,
                first_name, last_name, email, senders.created_at as sender_created_at, senders.updated_at as sender_updated_at
                FROM messages
                JOIN users as senders on messages.sender_id = senders.id
                WHERE receiver_id =  %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query,{"id": data})

        # Create and populate a list of message objects
        messages = []

        for message in results:
            # Make the sender object
            sender_data = {
                "id": message["sender_id"],
                "first_name": message["first_name"],
                "last_name": message["last_name"],
                "email": message["email"],
                "created_at": message["sender_created_at"],
                "updated_at": message["sender_updated_at"],
            }
            sender = user.User(sender_data)

            # Make the message object
            message = {
                "id": message["id"],
                "content": message["content"],
                "sender": sender,
                "receiver": receiver,
                "created_at": message["created_at"],
                "updated_at": message["updated_at"],
            }
            messages.append( cls(message) )

        return messages

                
