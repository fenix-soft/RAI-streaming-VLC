#!/usr/bin/env python

"""
Script per vedere gli stream RAI senza Flash.
Richiede python-requests e vlc sul sistema.
Scritto per Linux, ma con una minima modifica dovrebbe funzionare anche su Windows.

Author: Paolo MONTESEL
Copyright: 2016
License: MIT

UTILIZZO: python diretta.py
"""

import json
import os
import requests

CONFIG_URL = "http://www.rai.tv/dl/RaiTV/iphone/android/advertising_config.html"
PLAYER_CMD = "vlc \"{:s}\" 2> /dev/null &"


def http_get(url):
    return requests.get(url).text


def json_get(url):
    return json.loads(http_get(url))


def menu(options):
    for i, option in enumerate(options):
        print "[{}] - {:s}".format(i + 1, option)
    print ""
    
    return int(raw_input("> ")) - 1


def play(url):
    os.system(PLAYER_CMD.format(url))


if __name__ == "__main__":
    print "=== RAI STREAMING ==="
    channels = json_get(CONFIG_URL)["Channels"]
    canale = menu([c["name"] for c in channels])
    
    diretta_link = channels[canale]["direttaLink"]
    if diretta_link.find("&dem=") == -1:
        diretta_link = json_get(channels[canale]["direttaLink"])["video"][0]
        
    play(diretta_link)
