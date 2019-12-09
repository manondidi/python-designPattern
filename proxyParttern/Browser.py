from proxyParttern.Proxy import Proxy


class Browser:
    def __init__(self, proxy):
        self.proxy = proxy

    def request(self):
        print('浏览器准备访问网络')
        self.proxy.request()
