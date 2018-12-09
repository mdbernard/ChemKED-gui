# import os
# import sys
from tkinter import *
from tkinter import ttk
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
        self.pack(fill=BOTH, expand=1)
        self.winfo_toplevel().title("ChemKED")
        self.center_window()
        self.create_menu_bar()
        self.create_status_bar()

        # fill in the tabs with their contents
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(side=TOP, fill=BOTH, expand=1)
        self.tab_meta = Frame(self.tabs)
        self.tab_comp = Frame(self.tabs)
        self.tab_data = Frame(self.tabs)
        self.fill_tabs()

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
            "experiment-type": ttk.Combobox(self, values=["ignition-delay"]),
            "apparatus": {
                "kind": ttk.Combobox(self, values=["rapid compression machine", "shock tube"]),
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
                "kind": ttk.Combobox(self, values=["mass fraction", "mole fraction", "mole percent"]),
                "ignition-target": ttk.Combobox(self, values=["temperature", "pressure",
                                                              "OH", "OH*", "CH", "CH*"]),
                "ignition-type": ttk.Combobox(self, values=["d/dt max", "max", "1/2 max",
                                                            "min", "d/dt max extrapolated"]),
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
        #TODO
        print("This feature will be added in a future update!")

    def set_init_data(self):
        # This method might be completely unnecessary
        pass

    def create_status_bar(self):
        status = Label(self, text="Status: Ready", bd=1, relief=SUNKEN)
        status.pack(side=BOTTOM, fill=X, anchor=W)

    def fill_tabs(self):
        #TODO fill tabs with contents

        # add all tabs to tabs frame
        self.tabs.add(self.tab_meta, text="Metadata")
        self.tabs.add(self.tab_comp, text="Experiment Info")
        self.tabs.add(self.tab_data, text="Datapoints")

    def verify_inputs(self):
        #TODO
        pass

    def export_to_yaml(self):
        #TODO
        pass


def main():
    root = Tk()
    mainframe = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
