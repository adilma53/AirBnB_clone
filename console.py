#!/usr/bin/python3
"""defines the HBNBCommand class"""
import cmd
import sys
import shlex
import os
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """represents the entry point of the command interpreter"""
    prompt = '(hbnb) '
    __mc = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass
    
    def prase_arg(self, arg):
        """parse the arg"""
        args = arg.split()
        if len(args) == 0:
            return None
        if args[0] not in self.__mc:
            return None
        return args[0]

    def do_create(self, arg):
        """create a new instance of BaseModel and prints the id"""
        model = self.prase_arg(arg)
        if model is None:
            print("** class name missing **")
            return
        obj = eval(model)()
        obj.save()
        print(obj.id)
    def do_show(self, arg):
        """show the string representation of an instance"""
        arg = self.prase_arg(arg)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in BaseModel.__mc:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(arg[0], arg[1]) not in obj.keys():
            print("** no instance found **")
            return
        else:
            print("{} {}".format(arg[0], arg[1]))
    
    def do_destroy(self, arg):
        """destroy an instance"""
        arg = self.prase_arg(arg)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in BaseModel.__mc:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(arg[0], arg[1]) not in obj.keys():
            print("** no instance found **")
            return
        else:
            del obj["{}.{}".format(arg[0], arg[1])]
            storage.save()
    
    def do_clear(self, arg):
        """clear the console"""
        os.system("clear")



if __name__ == '__main__':
    HBNBCommand().cmdloop()