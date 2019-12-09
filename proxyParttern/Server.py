from proxyParttern.IProxy import IProxy


class Server(IProxy):
    def request(self):
        print('代理服务器正在请求网络')
