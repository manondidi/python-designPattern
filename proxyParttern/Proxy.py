from proxyParttern.IProxy import IProxy
from proxyParttern.Server import Server


class Proxy(IProxy):
    def __init__(self):
        self.server = Server()

    def request(self):
        print('proxy即将转发请求')
        self.server.request()
