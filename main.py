from app_logic import dictionary, database
from interface import CLI

database.create_tables

if __name__ == '__main__':
    cli = CLI.Cli()
    cli.cmdloop()
