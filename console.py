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

        # Create and save new instance of class
        if line in classes:
            base = classes[line]()
            base.save()
            print(base.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of instance based
            on the class name and id
        """
        obj = find_object(line)

        if obj is None:
            return

        print(obj)

    def do_destroy(self, line):
        """Deletes an instance based on
        its class name and id
        """

        obj = find_object(line)

        if obj is None:
            return

        key = f"{obj.__class__.__name__}.{obj.id}"

        objects = storage.all()
        del objects[key]
        del obj

        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        # No argument print all instances
        if line == "":
            for obj in storage.all().values():
                print(obj)
            return

        t_class = get_class(line)

        if t_class is None:
            print("** class doesn't exist **")
            return

        for obj in storage.all().values():
            # Print objects that match the class name
            if obj.__class__.__name__ == t_class.__name__:
                print(obj)


def parse_args(line):
    """Parses the command line argument and
    returns a tuple of all the arguments
    """
    args = tuple(line.split())
    return args


def get_class(class_name):
    """Returns the class associated with
     the class_name or None if it doesn't exist
    """

    if class_name in classes:
        return classes[class_name]
    else:
        return None


def get_object(cls, id):
    """Retrieves an object from file storage based on
    its class and id
    """

    key = f"{cls.__name__}.{id}"
    objects = storage.all()

    if key in objects:
        return objects[key]
    else:
        return None


def find_object(line):
    """Handles functions associated with retrieving
    an object given className and id. Returns the object if
    it exist or None
    """

    args = parse_args(line)

    if len(args) == 0:
        print("** class name missing **")
        return None

    t_class = get_class(args[0])

    if t_class is None:
        print("** class doesn't exist **")
        return None

    if len(args) == 1:
        print("** instance id missing **")
        return None

    obj = get_object(t_class, args[1])

    if obj is None:
        print("** no instance found **")
        return None

    return obj


if __name__ == "__main__":
    HBNBCommand().cmdloop()
