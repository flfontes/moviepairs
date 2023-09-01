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

        self.button_frame = ttb.Frame(self)
        self.button_frame.pack(padx=20, pady=(20, 10), fill="x")

        self.search_button01 = ttb.Button(
            master=self.button_frame,
            text="Search First Actor",
            command=self.actor_search,
            bootstyle="primary outline",
        )
        self.search_button01.pack(padx=(0, 10), expand=True, fill="x", side="left")

        self.search_button02 = ttb.Button(
            master=self.button_frame,
            text="Search Second Actor",
            command=self.actor_search,
            bootstyle="primary outline",
        )
        self.search_button02.pack(padx=(10, 0), expand=True, fill="x", side="left")

        self.movie_list = ttb.Frame(self, bootstyle="primary")
        self.movie_list.pack(padx=20, pady=(10, 20), fill="both", expand=True)
        
        self.counter = ttb.Label(self.movie_list, text = "Nothing Happened")
        self.counter.pack()

        
    # Actor Search
    def actor_search(self):
        self.counter.config(text = "Button Pressed")


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
