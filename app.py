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

        # Button
        self.button01 = ttb.Button(
            master=self.bframe,
            text="Search First Actor",  # ! TODO - Can we change the text of the button on click?
            command=self.actor_search,  # ! TODO - Is lambda is used, can I pass the button as an argument to the function?
            bootstyle="primary outline",
            state="normal",  # ! TODO
        )
        self.button01.pack(padx=(0, 10), expand=True, fill="x", side="left")

        self.button02 = ttb.Button(
            master=self.bframe,
            text="Search Second Actor",
            command=self.actor_search,
            bootstyle="primary outline",
        )
        self.button02.pack(padx=(10, 0), expand=True, fill="x", side="left")

        self.movlist = ttb.Frame(self, bootstyle="primary")
        self.movlist.pack(padx=20, pady=(10, 20), fill="both", expand=True)

        self.counter = ttb.Label(self.movlist, text="Nothing Happened")
        self.counter.pack()


    # Actor Search
    def actor_search(self):
    # def actor_search(self, button) :
        """
        IDEAS FOR THE FUNCTIONALITY:
        - Change button label to actor's name
        - Disable button
        """
        self.counter.config(text="Button Pressed")


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
