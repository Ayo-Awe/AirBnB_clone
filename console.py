#!/usr/bin/python3
"""Console Entry Point"""
import cmd
import os


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    use_rawinput = False

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
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
