#!/usr/bin/python3
""" Method Command Interpreter """
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommmand(cmd.Cmd):
    prompt = '(hbnb)'
    __classes = [
            "Amenity",
            "BaseModel",
            "City",
            "Place",
            "Review",
            "State",
            "User"
            ]
    def do_create(self, args):
        """Create a new instance of BaseModel, save it and prints the id
        Usage: create <class name>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = models.storage.all()
            key_value = string[0] + '.' + string[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** instance found **")

    def do_destroy(self, args):
        """Delete an instance Usage: destroy <class name> <id>"""
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key_find = args[0] + '.' + args[0]
            if key_find in objects.keys():
                objects.pop(key_find, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """Print a string representation of all instances
           Usage: all <class name>
        """
        args = args.split()
        object = models.storage.all()
        new = []

        if len(args) == 0:
            for obj in objects.values():
                new_list.append(obj.__str__())
            print(new_list)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exit **")
        else:
            for obj in objects.value():
                if obj.__class__.__name__ == args[0]:
                    new_list.append(obj.__str__())
                print(new_list)

    def do_update(self, args):
        """update an instance
           Usage update <class name> <id> <attribute name> "<attribute value>"
        """
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key_find = args[0] + '.' + args[1]
            onj = objects.get(key_find, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(onj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()
    def check_class_name(self, name=""):
        """Check if stdin user  typed class name and id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Check class id"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def no_quit(self, args):
        """<Quit> Command To Exit The Program"""
        return True

    def do_EOF(self, args):
        """Handles end of file"""
        return True

    def emptyline(self):
        """Dont execute anything when user press enter an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()