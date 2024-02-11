#!/usr/bin/python3

"""
A command-line interface for the HBNB program.

This module defines a command-line interface using the cmd module.
It provides a basic shell where users can interact with the HBNB program
by entering commands.

"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User

class HBNBCommand(cmd.Cmd):
    """
    A class representing the HBNB command-line interface.

    This class inherits from the cmd.Cmd class provided by the cmd module.
    Used for creating interactive command interpreters.

    Attributes:
        prompt (str): The prompt displayed to the user when waiting for input.
    """

    prompt = "(hbnb) "
    permissible_classes = ["BaseModel", "User"]

    def do_quit(self, arg):
        """
        Command handler for the 'quit' command.

        This method is called when the user enters the quit command.
        Returns True to exit the command interpreter loop.

        Args:
            arg (str): The argument provided with the 'quit' command (ignored).

        Returns:
            bool: True to exit the command interpreter loop.
        """
        return True

    def help_quit(self, arg=None):
        """
        Help text for the 'quit' command.

        Prints a message explaining the purpose of the 'quit' command.

        Args:
            arg (str): Arg provided with the 'help quit' command (ignored).
        """
        print("Quit command to exit the program")

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
        print()
        return True

    def Empty_Line(self):
        """Unresponsive when empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of the BaseModel and load it
            to JSON
        """
        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            print("** class name missing **")
        if cmd_args[0] not in self.permissible_classes:
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
        if cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        if len(cmd_args) < 2:
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
            return
        if cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        if len(cmd_args) < 2:
            print("** instance id is missing **")
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
        if cmd_args[0] not in self.permissible_classes:
            print("** class doesn't exist **")
        else:
            for key, value in object_storage.items():
                if key.split(".")[0] == cmd_args[0]:
                    print(str(value))

    def do_update(self, arg):
        """Updates attributes of an instance"""

        cmd_args = shlex.split(arg)

        if len(cmd_args) == 0:
            print("** class name missing **")
        if cmd_args [0] not in self.permissible_classes:
            print("** class doesn't exist **")
        if len(cmd_args) < 2:
            print("** instance id missing **")
        else:
            object_storage = storage.all()

            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            if key not in object_storage:
                print("** no instance found **")
            if len(cmd_args) < 3:
                print("** attribute is missing **")
            if len(cmd_args) < 4:
                print("** value is missing **")
            else:
                obj_key = object_storage[key]

            name_of_attribute = cmd_args[2]
            value_of_attribute = cmd_args[3]

            try:
                value_of_attribute = eval[value_of_attribute]
            except Exception:
                pass
            setattr(obj_key, name_of_attribute, value_of_attribute)

            obj_key.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
