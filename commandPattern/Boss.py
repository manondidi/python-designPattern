from commandPattern.ICommand import ICommand


class Boss:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def remove_command(self, command):
        self.commands.remove(command)

    def clear_command(self):
        self.commands.clear()

    def notify(self):
        for command in self.commands:
            command.excute()
