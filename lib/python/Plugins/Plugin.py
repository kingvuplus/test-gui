from Components.config import ConfigSubsection, config
from Tools.LoadPixmap import LoadPixmap
config.plugins = ConfigSubsection()

class PluginDescriptor:
    WHERE_EXTENSIONSMENU = 0
    WHERE_MAINMENU = 1
    WHERE_PLUGINMENU = 2
    WHERE_MOVIELIST = 3
    WHERE_MENU = 4
    WHERE_AUTOSTART = 5
    WHERE_WIZARD = 6
    WHERE_SESSIONSTART = 7
    WHERE_TELETEXT = 8
    WHERE_FILESCAN = 9
    WHERE_NETWORKSETUP = 10
    WHERE_EVENTINFO = 11
    WHERE_NETWORKCONFIG_READ = 12
    WHERE_AUDIOMENU = 13
    WHERE_SOFTWAREMANAGER = 14
    WHERE_SATCONFIGCHANGED = 15
    WHERE_SERVICESCAN = 16
    WHERE_EXTENSIONSINGLE = 17
    WHERE_CONFIGITEMS = 18

    def __init__(self, name = 'Plugin', where = [], description = '', icon = None, fnc = None, wakeupfnc = None, needsRestart = None, internal = False, weight = 0):
        self.name = name
        self.internal = internal
        self.needsRestart = needsRestart
        self.path = None
        if isinstance(where, list):
            self.where = where
        else:
            self.where = [where]
        self.description = description
        if icon is None or isinstance(icon, str):
            self.iconstr = icon
            self.icon = None
        else:
            self.icon = icon
        self.weight = weight
        self.wakeupfnc = wakeupfnc
        self.__call__ = fnc

    def updateIcon(self, path):
        if isinstance(self.iconstr, str):
            self.icon = LoadPixmap('/'.join((path, self.iconstr)))
        else:
            self.icon = None

    def getWakeupTime(self):
        return self.wakeupfnc and self.wakeupfnc() or -1

    def __eq__(self, other):
        return self.__call__ == other.__call__
