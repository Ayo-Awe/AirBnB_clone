#!/usr/bin/python3
"""Console Entry Point"""
import cmd
import os
from models import storage, classes


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def preloop(self) -> None:
        """Add newline character to prompt if interpreter is
        run in non-interactive mode
        """
        if not os.isatty(self.stdin.fileno()):
            self.prompt += "\n"

    def do_EOF(self, line):
        """EOF command to exit program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit program
        """
        return True

    def emptyline(self) -> bool:
        """Does nothing when emptyline is enter
        as a command
        """
        pass

    def do_create(self, line):
        """Create an instance of the specified model and
            save it to file storage
        """
        # Print error if empty string is supplied
        if line == "":
            print("** class name missing **")
            return

        if line in classes:
            base = classes[line]()
            base.save()
            print(base.id)
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
