from dellDesktopBuilder import DellDesktopBuilder
from hpDesktopBuilder import HpDesktopBuilder
from desktopDirector import DesktopDirector

hpDesktopBuilderinstance = HpDesktopBuilder()
dellDesktopBuilderInstance = DellDesktopBuilder()

director1 = DesktopDirector(hpDesktopBuilderinstance)
director2 = DesktopDirector(dellDesktopBuilderInstance)

director1.buildDesktop()
director2.buildDesktop()

desktop1 = director1.getDesktop()
desktop2 = director2.getDesktop()

desktop1.showSpecs()
desktop2.showSpecs()