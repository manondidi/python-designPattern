from commandPattern.Boss import Boss
from commandPattern.Command1 import Command1
from commandPattern.Command2 import Command2
from commandPattern.Excuter import Excuter

if __name__ == '__main__':
    excuter = Excuter()  # 执行者
    command1 = Command1(excuter)
    command2 = Command2(excuter)
    boss = Boss()
    boss.add_command(command1)
    boss.add_command(command2)
    boss.notify()
