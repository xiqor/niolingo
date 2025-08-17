from app_logic import database
class Item:
    # initialization
    def __init__(self, item_type, spelling, transcription, meaning=''):
        self.type = item_type
        self.spelling = spelling
        self.transcription = transcription
        self.meaning = meaning

    # save new item to db WORKS
    def add(self):
        database.add_item(self)

    # remove item from db WORKS
    def remove(self):
        database.remove_item(self)

    # pretty print of item
    def pprint(self):
        pass