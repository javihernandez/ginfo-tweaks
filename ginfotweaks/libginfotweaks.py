# -*- coding: utf-8 -*-

"""ginfotweaks library for manipulating launchers"""

import os
from xdg.DesktopEntry import DesktopEntry
from xdg.IniFile import *
from xdg.BaseDirectory import *
from subprocess import Popen, list2cmdline

SYSTEM, USER = range(3,5)

allowedGroups = ["Desktop Entry", "KDE Desktop Entry", "GinfoTweaks Entry", "GinfoTweaks Category"]

class Launcher(DesktopEntry):
    """Launcher class"""

    defaultGroup = 'GinfoTweaks Entry'

    def parse(self, file):
        IniFile.parse(self, file, allowedGroups)

    def launch(self):
        """Execute the launcher"""

        exe = self.getExec()
        command = [x for x in exe.split() if not '%' in x]
        command = list2cmdline(command)

        sp = Popen(command, shell=True)
        return True

    def getAuthor(self):
        return self.get('Author', locale=True)


class Category(DesktopEntry):
    """Category class"""

    defaultGroup = 'GinfoTweaks Category'

    def parse(self, file):
        IniFile.parse(self, file, allowedGroups)


# ginfotweaks common utilities

SYS_BASEDIR = os.path.join('/usr/lib', 'ginfotweaks', 'launchers')
USER_BASEDIR = os.path.join(xdg_data_home, 'ginfotweaks', 'launchers')

def get_launchers():
    """Retrieve all system and user launchers"""

    system_launchers = get_path_launchers(SYS_BASEDIR)
    user_launchers = get_path_launchers(USER_BASEDIR)
    
    return system_launchers, user_launchers

def get_path_launchers(path):
    """Get launches from a given path"""

    launchers = list()

    if os.path.exists(path):
        for i in os.listdir(path):
            if i.endswith('.launcher'):
                launchers.append(Launcher(os.path.join(path, i)))

    return launchers

def get_category_from_path(category, path):
    """Get category from a given path"""

    if path == SYSTEM:
        path = _get_fixed_category_path(SYS_BASEDIR)
        category_object = _get_category(category, path)
        
    elif path == USER:
        path = _get_fixed_category_path(USER_BASEDIR)
        category_object = _get_category(category, path)

    else:
        category_object = _find_category(category, path)

    return category_object
 

def _get_fixed_category_path(path):
    """Returns category path from a given launcher path"""
    if path.endswith('/'):
        path = path[:-1]
    base_dir = os.path.split(path)[0]
    return os.path.join(base_dir, 'categories')

def _get_category(category, path):
    if os.path.exists(path):
        for i in os.listdir(path):
            if i.endswith('.category'):
                a = Category(os.path.join(path, i))
                if a.getName() == category:
                    return a

def _find_category(category, path):
    # First, we look for .category files in current dir
    if os.path.exists(path):
        for i in os.listdir(path):
            if i.endswith('.category'):
                a = Category(os.path.join(path, i))
                if a.getName() == category:
                    return a

    # If not, try searching in categories dir
    path = _get_fixed_category_path(path)
    return _get_category(category, path)

