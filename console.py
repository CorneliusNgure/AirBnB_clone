#!/usr/bin/python3

"""
A command-line interface for the HBNB program.

This module defines a command-line interface using the cmd module.
It provides a basic shell where users can interact with the HBNB program
by entering commands.
"""

import cmd
import shlex
import ast
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    A class representing the HBNB command-line interface.

    This class inherits from the cmd.Cmd class provided by the cmd module.
    Used for creating interactive command interpreters.

    Attributes:
        prompt (str): The prompt displayed to the user when waiting for input.
    """

    prompt = "(hbnb) "
    permissible_classes = ["BaseModel", "User", "Amenity",
                            "Review", "City", "State", "Place"]

    def emptyline(self):
        """Print nothing when no commands are put"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Command handler for the end-of-file (EOF) signal.

        Returns True to exit the command interpreter
        loop, effectively quitting the program.

        Args:
            arg (str): The argument provided with the EOF signal (ignored).

        Returns:
            bool: True to exit the command interpreter loop.
        """
        return True

    def do_create(self, arg):
        """Create a new instance of the BaseModel and load it
            to JSON
        """
        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{cmd_args[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Display the string representative of an instance"""
        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            object_storage = storage.all()

            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            if key in object_storage:
                print(object_storage[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete instances by specifying their class and id"""
        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            object_storage = storage.all()
            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            if key in object_storage:
                del object_storage[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Display the string representation of instances or classes"""
        object_storage = storage.all()

        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            for key, value in object_storage.items():
                print(str(value))
        elif cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        else:
            for key, value in object_storage.items():
                if key.split(".")[0] == cmd_args[0]:
                    print(str(value))

    def default(self, arg):
        """
        Defines the default logic for invalid user input
        """
        list_of_args = arg.split('.')

        name_of_class = list_of_args[0]

        cmd_args = list_of_args[1].split('(')

        cmd_method = cmd_args[0]

        additional_args = cmd_args[1].split(')')[0]

        dictionary_method = {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update,
                'count': self.do_count
                }

        if cmd_method in dictionary_method.keys():
            if cmd_method != "update":
                return dictionary_method[cmd_method]("{} {}".format(
                    name_of_class, additional_args))
            else:
                if not name_of_class:
                    print("** class name missing **")
                    return
                try:
                    obj_id, dict_arg = self.parse_curly_braces_data(additional_args)
                except Exception:
                    pass
                try:
                    call = dictionary_method[cmd_method]
                    return call("{} {} {}".format(name_of_class, obj_id, dict_arg))
                except Exception:
                    pass
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False

    def parse_curly_braces_data(self, additional_args):
        """Parses the curly braces data"""

        curlyBraces = re.search(r"\{(.*?)\}", additional_args)

        if curlyBraces:
            id_with_comma = shlex.split(additional_args[:curlyBraces.span()[0]])

            id = [i.strip(",") for i in id_with_comma][0]

            data_string = curlyBraces.group(1)

            try:
                dictionary_arg = ast.literal_eval("{" + data_string + "}")
            except Exception:
                print("** invalid dictionary format **")
                return
            return id, dictionary_arg
        else:
            cmd_args = additional_args.split(",")
            if cmd_args:
                try:
                    id = cmd_args[0]
                except Exception:
                    return "", ""
                try:
                    name_of_attribute = cmd_args[1]
                except Exception:
                    return id, ""
                try:
                    value_of_attribute = cmd_args[2]
                except Exception:
                    return id, name_of_attribute
                return f"{id}", f"{name_of_attribute} {value_of_attribute}"

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class
        """
        storage_objects = storage.all()

        cmd_args = shlex.split(arg)

        if arg:
            name_of_class = cmd_args[0]

        count = 0

        if cmd_args:
            if name_of_class in self.permissible_classes:
                for objects in storage_objects.values():
                    if objects.__class__.__name__ == name_of_class:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """Updates attributes of an instance"""

        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            object_storage = storage.all()

            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            
            if key not in object_storage:
                print("** no instance found **")
            elif len(cmd_args) < 3:
                print("** attribute name missing **")
            elif len(cmd_args) < 4:
                print("** value missing **")
            else:
                obj_key = object_storage[key]
                curlyBraces = re.search(r"\{(.*?)\}", arg)

                if curlyBraces:
                    data_string = curlyBraces.group(1)
                    dictionary_arg = ast.literal_eval("{" + data_string + "}")

                    for attr_name, attr_value in dictionary_arg.items():
                        setattr(obj_key, attr_name, attr_value)
                else:
                    attr_name = cmd_args[2]
                    attr_value = cmd_args[3]

                    try:
                        value_of_attribute = eval(attr_value)
                    except Exception:
                        value_of_attribute = attr_value

                    setattr(obj_key, attr_name, value_of_attribute)

                obj_key.save()

    def do_update(self, arg):
        """Updates attributes of an instance"""

        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            print("** class name missing **")
        elif cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        elif len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            object_storage = storage.all()

            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            if key not in object_storage:
                print("** no instance found **")
            elif len(cmd_args) < 3:
                print("** attribute name missing **")
            elif len(cmd_args) < 4:
                print("** value missing **")
            else:
                obj_key = object_storage[key]
                curlyBraces = re.search(r"\{(.*?)\}", arg)

            if curlyBraces:
                try:
                    data_string = curlyBraces.group(1)

                    dictionary_arg = ast.literal_eval("{" + data_string + "}")
                    name_of_attribute = list(dictionary_arg.keys())
                    value_of_attribute = list(dictionary_arg.values())

                    try:
                        name_of_attr_1 = name_of_attribute[0]
                        value_of_attr_1 = value_of_attribute[0]
                        setattr(obj_key, name_of_attr_1, value_of_attr_1)

                    except Exception:
                        pass

                    try:
                        name_of_attr_2 = name_of_attribute[1]
                        value_of_attr_2 = value_of_attribute[1]
                        setattr(obj_key, name_of_attr_2, value_of_attr_2)

                    except Exception:
                        pass

                except Exception:
                    pass
            else:
                attr_name = cmd_args[2]
                attr_value = cmd_args[3]

                try:
                    value_of_attribute = eval(attr_value)

                except Exception:
                    pass

                setattr(obj_key, attr_name, value_of_attribute)
                
            obj_key.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
