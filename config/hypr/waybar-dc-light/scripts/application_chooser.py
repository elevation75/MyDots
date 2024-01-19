#!/usr/bin/env python3
import subprocess
import json
import sys

# Define the list of applications
applications = [
    {"name": "Terminal", "command": "gnome-terminal"},
    {"name": "Text Editor", "command": "gedit"},
    {"name": "Web Browser", "command": "firefox"},
    {"name": "File Manager", "command": "nautilus"}
]

# Create the menu JSON structure
menu = []
for app in applications:
    menu.append({"label": app["name"], "command": app["command"]})

# Convert the menu to a JSON string
menu_json = json.dumps(menu)

def execute_command(command):
    subprocess.Popen(command.split())

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--waybar-click":
        # A click event occurred
        click_index = int(sys.argv[2])
        if click_index >= 0 and click_index < len(applications):
            # Execute the command associated with the clicked application
            execute_command(applications[click_index]["command"])
    else:
        # Print the menu JSON to be used by Waybar
        print(menu_json)

if __name__ == "__main__":
    main()
