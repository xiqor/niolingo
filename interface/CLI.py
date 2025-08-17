import cmd
from app_logic import dictionary

class Cli(cmd.Cmd):
    intro = '''
    Welcome to Vocaboo: simple CLI vocabulary (for now:D)
    Type 'help' or '?' for help
    '''
    prompt = 'vocaboo >> '

    def do_add(self, arg):
        '''Add new word to your dictionary:
        add <type> <spelling> <transcription> <meaning>'''
        args = arg.split()
        item = dictionary.Item(item_type=args[0], spelling=args[1], transcription=args[2], meaning=args[3])
        item.add()

    def do_remove(self, item_id):
        '''Remove existing word from your dictionary by id (use 'get' to get id):
        remove <id>'''
        dictionary.Item.remove(item_id)

    def do_update(self, arg):
        pass

    def do_get(self, arg): #WIP name
        '''Get info about existing word in dictionary:
        get <spelling/meaning>'''
        print(dictionary.Item.get(arg))


    def do_show(): #WIP name
        pass

    def do_exit(self, arg):
        return True

    #Todo add comand for review mode: set number of questions and randomize it
