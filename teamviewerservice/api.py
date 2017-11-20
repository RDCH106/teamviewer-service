# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
import pyautogui
import os
from flask import send_file
import subprocess
import json

config = None


def load_config():
    try:
        with open('config/tv_config.json') as config_file:
            config = json.load(config_file)
            print("Loaded: config/tv_config.json")
            config["tv_path"]
    except IOError:
        print("Error loading tv_config.json!")
        print("Create config/tv_config.json with the content:")
        print("{\"tv_path\": \"C:/path/to/teamviewer/TeamViewer.exe\"}")
        exit()
    except KeyError:
        print("Misformed tv_config.json!")
        print("Create config/tv_config.json with the content:")
        print("{\"tv_path\": \"C:/path/to/teamviewer/TeamViewer.exe\"}")
        exit()
    return config


class StartTV(linkero.Resource):
    @linkero.auth.login_required
    def get(self):
        # https://msdn.microsoft.com/en-us/library/windows/desktop/ms684863(v=vs.85).aspx
        DETACHED_PROCESS = 8
        subprocess.Popen(config["tv_path"], creationflags=DETACHED_PROCESS)
        return "OK"


class Screenshot(linkero.Resource):
    @linkero.auth.login_required
    def get(self):
        pyautogui.screenshot('screenshot.png')
        return send_file(os.path.dirname(os.path.realpath(__file__)) + '/screenshot.png',
                         mimetype='image/gif', cache_timeout=10)


class Logout(linkero.Resource):
    def get(self):
        return "Logout", 401

##
## Actually setup the Api resource routing here
##
def loadAPI():
    config = load_config()
    linkero.api.add_resource(StartTV, '/startTV')
    linkero.api.add_resource(Screenshot, '/screenshot')
    linkero.api.add_resource(Logout, '/logout')