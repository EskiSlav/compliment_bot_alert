from __future__ import annotations


class User:
    def __init__(self, **user) -> None:
        self.id: int = user['id']
        self.is_bot: bool = user['is_bot']
        self.first_name: str = user['first_name']
        self.last_name: str = user['last_name']
        self.username: str = user['username']
        self.language_code: str = user['language_code']

    def __repr__(self) -> str:
        return str(self.__dict__)


class Chat:
    def __init__(self, **chat) -> None:
        self.id: int = chat['id']
        self.first_name: str = chat['first_name']
        self.last_name: str = chat['last_name']
        self.username: str = chat['username']
        self.type: str = chat['type']

    def __repr__(self) -> str:
        return str(self.__dict__)


class Message:
    def __init__(self, **message) -> None:
        self.from_user = User(**message['from'])
        self.chat = Chat(**message['chat'])
        self.date: int = message['date']
        self.text: int = message['text']

    def __repr__(self) -> str:
        return str(self.__dict__)


class Update:
    def __init__(self, **update) -> None:
        self.update_id = update['update_id']
        self.message = Message(**update['message'])

    def __repr__(self) -> str:
        return str(self.__dict__)
