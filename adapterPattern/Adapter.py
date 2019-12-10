from adapterPattern.Socket import Socket


class Adapter:
    def __init__(self):
        self.socket = Socket()

    def adapt(self):
        self.socket.give_power_220v()
        print('将220v 转为 5v')
