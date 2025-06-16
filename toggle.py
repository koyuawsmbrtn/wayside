#!/usr/bin/python
import os
if os.system("pgrep -x waybar") == 0:
    os.system("killall waybar -9")
else:
    os.system("waybar -c ~/.config/wayside/waybar_config.json &")