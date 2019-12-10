from adapterPattern.Adapter import Adapter


class Phone:

    def __init__(self):
        self.adapter = None

    def charge(self):
        print('手机充电')
        self.adapter.adapt()
