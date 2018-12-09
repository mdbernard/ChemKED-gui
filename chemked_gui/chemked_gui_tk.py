# import os
# import sys
from tkinter import *
# import tkinter.messagebox
from pyked import __version__, chemked


class MainWindow(Frame):
    """ Controls the main window size, location, menu bar,
        handling, and functions.
    """

    def __init__(self, parent=None):
        # set up the window
        Frame.__init__(self, parent, width=800, height=600)
        self.parent = parent
        self.pack()
        self.winfo_toplevel().title("ChemKED")
        self.center_window()
        self.create_menu_bar()

        # the data the user will modify and export with the GUI
        self.data = {
            "file-authors": [
                {"name": Entry(self),
                 "ORCID": Entry(self)}
            ],
            "file-version": Entry(self),
            "chemked-version": Entry(self),
            "reference": {
                "doi": Entry(self),
                "authors": [
                    {"name": Entry(self),
                     "ORCID": Entry(self)}
                ],
                "journal": Entry(self),
                "year": Entry(self),
                "volume": Entry(self),
                "pages": Entry(self),
                "detail": Entry(self)
            },
            "experiment-type": '',  #TODO this should be a combo box
            "apparatus": {
                "kind": '',  #TODO this should be a combo box
                "institution": Entry(self),
                "facility": Entry(self)
            },
            "datapoints": [
                {"temperature": Entry(self),
                 "pressure": Entry(self),
                 "ignition-delay": Entry(self),
                 "equivalence-ratio": Entry(self)}
            ],
            "common-properties": {
                "species": [
                    {"species-name": Entry(self),
                     "InChI": Entry(self),
                     "amount": Entry(self)}
                ],
                "kind": '',  #TODO this should be a combo box
                "ignition-target": '', #TODO this should be a combo box
                "ignition-type": '', #TODO this should be a combo box
            }
        }
        self.set_init_data()

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
        file_menu.add_command(label="TODO: Preferences", command=self.preferences)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.winfo_toplevel().quit)
        menu.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menu)
        edit_menu.add_command(label="TODO: Put something here")
        menu.add_cascade(label="Edit", menu=edit_menu)

    def preferences(self):
        print("This feature will be added in a future update!")

    def set_init_data(self):
        self.data["chemked-version"].insert(END, __version__)

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
