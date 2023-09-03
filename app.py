import os
import tkinter as tk

import json # ! Temporary import, useful for troubleshooting

from dotenv import load_dotenv

import requests as r

import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Dialog


class App(ttb.Frame):
    """
    WIP: A class handling the layout and functionality of the MoviePairs app.
    """

    # Main frame
    def __init__(self, parent):
        """
        ...
        """
        super().__init__(parent)
        self.pack(expand=True, fill="both")

        load_dotenv()
        self.__api_key = os.getenv("api_key")
    
        self.layout()
    
    
    def layout(self):

        # Frame containing the main search buttons
        self.bframe = ttb.Frame(self)
        self.bframe.pack(padx=20, pady=(20, 10), fill="x")

        self.buttons()

        self.movlist = ttb.Frame(self, bootstyle="primary")
        self.movlist.pack(padx=20, pady=(10, 20), fill="both", expand=True)

        self.movie_list()


    def buttons(self):
        self.button=ttb.Button(
            master=self.bframe,
            text="Search Actors",
            command=lambda: self.actor_search(self.button),
            bootstyle="primary",
        )
        self.button.pack(expand=True, fill="x")

    # Content of the list frame
    def movie_list(self):
        self.counter=ttb.Label(self.movlist, text="Nothing Happened")
        self.counter.pack()
        
    # Actor Search
    def actor_search(self, button) :
        """
        ...
        """
        self.input_name01 = ttb.Querybox.get_string(
            parent = self,
            prompt = "What is the name of the first actor you are looking for?",
            title = "Input First Actor",
        )
        
        self.request_actors(self.input_name01)
        
        self.input_name02 = ttb.Querybox.get_string(
            parent = self,
            prompt = "What is the name of the other actor you are looking for?",
            title = "Input Second Actor",
        )
        
        button["text"] = f"Actors Picked: {self.input_name01.title()} and {self.input_name02.title()}"
        button["state"] = "disabled"
        
        self.request_actors(self.input_name02)


    def request_actors(self, actor):
        
        self.response = r.get(
            url=f"https://api.themoviedb.org/3/search/person?query={actor.replace(' ', '%20')}&include_adult=false&language=en-US&page=1", 
            headers={
                "accept": "application/json",
                "Authorization": f"Bearer {self.__api_key}"
                }
            )
        print(self.response.status_code)
        
        if self.response.status_code == 200:# or len(self.response.json()["results"]) == 0:
            print(f"{actor.title()} was found!")
        else:
            print(f"{actor.title()} was not found!")
        
        with open(f"{actor}.json", "w") as outfile:
            json.dump(self.response.json(), outfile, indent=4)
        
        self.actor_info = {
            "name": self.response.json()["results"][0]["name"],
            "id": self.response.json()["results"][0]["id"],
            "pic": self.response.json()["results"][0]["profile_path"]
        }
        
        self.confirmation = Dialog(
            self,
            title = "Test")
        self.confirmation.build()
        self.confirmation.show()
        
        print(self.actor_info)


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
