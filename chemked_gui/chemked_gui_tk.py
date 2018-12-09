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

        # the data the user will modify and export with the GUI
        # blank strings to be replaced with Entry() widgets by fill_data()
        self.data = {
            "file-authors": [],
            "file-version": '',
            "chemked-version": '',
            "reference": {
                "doi": '',
                "authors": [],
                "journal": '',
                "year": '',
                "volume": '',
                "pages": '',
                "detail": ''
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

        # fill in the tabs with their contents
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(side=TOP, fill=BOTH, expand=1)
        self.tab_1 = Frame(self.tabs)  # Metadata
        self.tab_2 = Frame(self.tabs)  # Experiment Info
        self.tab_3 = Frame(self.tabs)  # Datapoints
        self.fill_tabs()

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
        status = Label(self, text="Status: Ready", justify=LEFT, bd=1, relief=SUNKEN)
        status.pack(side=BOTTOM, fill=X, anchor=W)

    def fill_tabs(self):
        #TODO fill tabs with contents

        # ---TAB 1: METADATA AND REFERENCES---
        tab_1_metadata = Frame(self.tab_1)
        tab_1_reference = Frame(self.tab_1)

        label_metadata = Label(tab_1_metadata, text="Metadata", justify=CENTER)
        label_metadata.grid(columnspan=6, row=0, column=0, sticky=N)
        label_reference = Label(tab_1_reference, text="Reference", justify=CENTER)
        label_reference.grid(columnspan=6, row=0, column=0, sticky=N)

        label_file_version = Label(tab_1_metadata, text="File Version")
        label_file_version.grid(columnspan=3, row=1, column=0, sticky=E)
        label_chemked_version = Label(tab_1_metadata, text="ChemKED Version")
        label_chemked_version.grid(columnspan=3, row=2, column=0, sticky=E)

        self.data["file-version"] = Entry(tab_1_metadata)
        entry_file_version = self.data["file-version"]
        entry_file_version.grid(columnspan=3, row=1, column=3)
        self.data["chemked-version"] = Entry(tab_1_metadata)
        entry_chemked_version = self.data["chemked-version"]
        entry_chemked_version.insert(index=0, string=__version__)
        entry_chemked_version.grid(columnspan=3, row=2, column=3)

        tab_1_metadata.pack(side=LEFT, fill=BOTH, expand=1)
        tab_1_reference.pack(side=RIGHT, fill=BOTH, expand=1)

        # ---ADD ALL TABS TO THE TAB FRAME---
        self.tabs.add(self.tab_1, text="Metadata")
        self.tabs.add(self.tab_2, text="Experiment Info")
        self.tabs.add(self.tab_3, text="Datapoints")

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
