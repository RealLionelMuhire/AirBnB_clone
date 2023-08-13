#!/usr/bin/python3
"""this is the console"""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex


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
    
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id"""
        if not args:
            print("** class name missing **")
        elif args != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args_list = shlex.split(args)
            if args_list[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                obj_id = args_list[1]
                obj_key = "{}.{}".format("BaseModel", obj_id)
                all_objs = storage.all()
                if obj_key in all_objs:
                    obj = all_objs[obj_key]
                    print(obj)
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()