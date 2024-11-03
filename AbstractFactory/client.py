from abstractFactory import AbstractFactory
abstractFactory = AbstractFactory()

windowsFactory = abstractFactory.createFactory('mac')
macFactory = abstractFactory.createFactory('windows')

windowsFactory.getButton()
macFactory.getButton()

windowsFactory.getCursor()
macFactory.getCursor()