#!/usr/bin/python3

"""
A command-line interface for the HBNB program.

This module defines a command-line interface using the cmd module.
It provides a basic shell where users can interact with the HBNB program
by entering commands.

Classes:
    HBNBCommand: A class representing the command-line interface.

"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    A class representing the HBNB command-line interface.

    This class inherits from the cmd.Cmd class provided by the cmd module.
    Used for creating interactive command interpreters.

    Attributes:
        prompt (str): The prompt displayed to the user when waiting for input.
    """

    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
