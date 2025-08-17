import cmd
from app_logic import dictionary

class Cli(cmd.Cmd):
    intro = '''
    Welcome to Vocaboo: simple CLI vocabulary (for now:D)
    Type 'help' or '?' for help
    '''
    prompt = 'vocaboo >> '

    def do_add(self, arg):
        '''Add new word or phrase:
        add <type> <spelling> <transcription> <meaning>'''
        args = arg.split()
        item = dictionary.Item(item_type=args[0], spelling=args[1], transcription=args[2], meaning=args[3])
        item.add()


    def do_remove():
        pass

    def do_update():
        pass

    def do_show(): #WIP name
        pass

    def do_exit(self, arg):
        return True

    #Todo add comand for review mode: set number of questions and randomize it
