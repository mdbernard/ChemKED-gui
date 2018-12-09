# import os
# import sys
from tkinter import *
# import tkinter.messagebox


class MainWindow(Frame):
    """ Controls the main window size, location, menu bar,
        handling, and functions.
    """

    def __init__(self, parent=None):
        Frame.__init__(self, parent, width=800, height=600)
        self.parent = parent
        self.pack()
        self.winfo_toplevel().title("ChemKED")
        self.center_window()
        self.create_menu_bar()

    def center_window(self):
        """ Centers the window on the user's screen. """
        self.winfo_toplevel().update_idletasks()
        screen_width = self.winfo_toplevel().winfo_screenwidth()
        screen_height = self.winfo_toplevel().winfo_screenheight()
        window_width = self.winfo_toplevel().winfo_width()
        window_height = self.winfo_toplevel().winfo_height()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.winfo_toplevel().geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

    def create_menu_bar(self):
        menu = Menu(self)
        self.winfo_toplevel().config(menu=menu)

        file_menu = Menu(menu)
        file_menu.add_command(label="Preferences", command=self.preferences)
        file_menu.add_command(label="Exit", command=self.winfo_toplevel().quit)
        menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)

    def preferences(self):
        print("This feature will be added in a future update!")

    def create_status_bar(self):
        pass

    def create_tabs(self):
        pass

    def verify_inputs(self):
        pass

    def export_to_yaml(self):
        pass


def main():
    root = Tk()
    mainframe = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
