#!/usr/bin/python3
"""This is the console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """
    class HBNBCommand
    """
    prompt = "(hbnb) "
    supported_classes = ["BaseModel", "User"]

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
        elif args != "BaseModel" and args != "User":
            print("** class doesn't exist **")
        else:
            new_obj = BaseModel() if args == "BaseModel" else User()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args_list = shlex.split(args)
            if args_list[0] not in self.supported_classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                obj_id = args_list[1]
                obj_key = "{}.{}".format(args_list[0], obj_id)
                all_objs = storage.all()
                if obj_key in all_objs:
                    obj = all_objs[obj_key]
                    print(obj)
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args_list = shlex.split(args)
            if args_list[0] not in self.supported_classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                obj_id = args_list[1]
                obj_key = "{}.{}".format(args_list[0], obj_id)
                all_objs = storage.all()
                if obj_key in all_objs:
                    del all_objs[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg not in self.supported_classes and arg:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            print([str(obj) for obj in all_objs.values()])

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute"""
        if not args:
            print("** class name missing **")
        else:
            args_list = shlex.split(args)
            if args_list[0] not in self.supported_classes:
                print("** class doesn't exist **")
            elif len(args_list) < 2:
                print("** instance id missing **")
            else:
                obj_id = args_list[1]
                obj_key = "{}.{}".format(args_list[0], obj_id)
                all_objs = storage.all()
                if obj_key in all_objs:
                    obj = all_objs[obj_key]
                    if len(args_list) < 3:
                        print("** attribute name missing **")
                    elif len(args_list) < 4:
                        print("** value missing **")
                    else:
                        attr_name = args_list[2]
                        attr_value = args_list[3]
                        if hasattr(obj, attr_name):
                            attr_type = type(getattr(obj, attr_name))
                            setattr(obj, attr_name, attr_type(attr_value))
                            obj.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
