from proxyParttern.Browser import  Browser
from proxyParttern.Proxy import  Proxy




#代理模式
def main():
    proxy = Proxy()
    browser = Browser(proxy)
    browser.request()


if __name__ == '__main__':
    main()
