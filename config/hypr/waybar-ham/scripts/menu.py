#!/usr/bin/env python

import json

def create_menu(applications):
    """Creates the menu items"""
    menu_items = []
    for i, (app_name, app_path) in enumerate(applications):
        menu_item = {
            "label": app_name,
            "id": i,
            "tooltip": app_path,
            "action": f"python3 ~/.config/waybar/scripts/launcher.py {app_path}"  # Replace "/path/to/launcher.py" with the actual path to the launcher.py script
        }
        menu_items.append(menu_item)

    waybar_output = {
        "text": "Launcher",
        "class": "launcher",
        "tooltip": "Click to open the launcher",
        "menu": menu_items
    }

    # Print the JSON output to standard output
    print(json.dumps(waybar_output))

def main():
    """Main function"""
    applications = [
        ("Microsoft StudioCode", "/usr/bin/code"),
        ("Sublime Text", "/op/sublime_text/sublime_text"),
        ("Blender", "/usr/bin/blender")
    ]

    create_menu(applications)

if __name__ == "__main__":
    main()
