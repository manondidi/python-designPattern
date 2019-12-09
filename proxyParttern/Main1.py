from proxyParttern.Browser import  Browser
from proxyParttern.Proxy import  Proxy





def main():
    proxy = Proxy()
    browser = Browser(proxy)
    browser.request()


if __name__ == '__main__':
    main()
