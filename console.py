#!/usr/bin/python3
"""this is the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """Called when an empty line + ENTER is input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()