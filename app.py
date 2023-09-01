from tkinter import *

import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox


class App(ttb.Frame):
    """
    WIP: A class handling the layout and functionality of the MoviePairs app.
    """

    # Main frame
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=True, fill="both")

        # Frame containing the main search buttons
        self.bframe = ttb.Frame(self)
        self.bframe.pack(padx=20, pady=(20, 10), fill="x")

        # Search Button for Actors
        self.button = ttb.Button(
            master=self.bframe,
            text="Search Actors",
            command=lambda: self.actor_search(self.button),
            bootstyle="primary outline",
            state="normal",
        )
        self.button.pack(expand=True, fill="x")

        self.movlist = ttb.Frame(self, bootstyle="primary")
        self.movlist.pack(padx=20, pady=(10, 20), fill="both", expand=True)

        self.counter = ttb.Label(self.movlist, text="Nothing Happened")
        self.counter.pack()


    # Actor Search
    def actor_search(self, button) :
        """
        IDEAS FOR THE FUNCTIONALITY:
        - ...
        """
        self.input_name01 = ttb.Querybox.get_string(
            parent = self,
            prompt = "What is the name of the first actor you are looking for?",
            title = "Input First Actor",
        )
        
        self.input_name02 = ttb.Querybox.get_string(
            parent = self,
            prompt = "What is the name of the other actor you are looking for?",
            title = "Input Second Actor",
        )
        
        button["text"] = f"{self.input_name01} and {self.input_name02}"
        button["state"] = "disabled"
        
        self.request_actors()


    def request_actors(self):
        pass

if __name__ == "__main__":
    root = ttb.Window(
        themename="solar",
        title="MoviePairs 1.0",
        iconphoto="",  # ! TODO
        size=(400, 800),
    )
    root.place_window_center()

    App(root)

    root.mainloop()

    """
    FUNCTIONALITY IDEAS
    - Style changes (dark vs light mode)
    - More than 2 actors match
    - ...
    """
