#!/usr/bin/env python

import tkinter as tk

def launch_application(app_name):
    """Launches the specified application"""
    print(f"Launching {app_name}...")  # Replace with the code to launch the selected application

def create_menu(applications):
    """Creates the menu with clickable buttons"""
    root = tk.Tk()
    root.title("Application Launcher")

    menu = tk.Menu(root, tearoff=0)
    for app_name, _ in applications:
        menu.add_command(label=app_name, command=lambda name=app_name: launch_application(name))

    def show_menu(event):
        menu.tk_popup(event.x_root, event.y_root)

    root.bind("<Button-1>", show_menu)

    root.mainloop()

def main():
    """Main function"""
    applications = [
        ("Microsoft StudioCode", "/opt/visual-studio-code/bin/code &"),
        ("Sublime Text", "/opt/sublime_text/sublime-text"),
        ("Blender", "/usr/bin/blender")
    ]

    create_menu(applications)

if __name__ == "__main__":
    main()
