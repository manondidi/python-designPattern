from adapterPattern.Phone import Phone
from adapterPattern.Adapter import Adapter


if __name__ == '__main__':
    phone = Phone()
    adapter = Adapter()
    phone.adapter = adapter
    phone.charge()