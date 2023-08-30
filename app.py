from tkinter import *

import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox


# movie_list = ttb.Frame(root, bootstyle = "primary")
# movie_list.pack(padx = 20, pady = (20, 10), fill = "both", expand = True)

# actor_title = ttb.Label(movie_list, bootstyle = "primary inverse")
# actor_title.config(text = "Actor vs Actor")
# actor_title.pack(pady = 20)

# actor01_button = ttb.Button(root, text = "First Actor", bootstyle = "primary outline")
# actor01_button.pack(padx = (20, 10), pady = (10, 20), side = "left", expand = True, fill = "both")

# actor02_button = ttb.Button(root, text = "Second Actor", bootstyle = "primary outline")
# actor02_button.pack(padx = (10, 20), pady = (10, 20), side = "right", expand = True, fill = "both")

class Movies(ttb.Frame):
    """
    WIP:
    """
    
    # Main frame
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(
            expand = True, 
            fill = "both"
            )
        
        button_frame = ttb.Frame(self)
        button_frame.pack(
            padx = 20, 
            pady = (20, 10), 
            fill = "x"
            )
        
        search_button01 = ttb.Button(
            master = button_frame, 
            text = "Search First Actor", 
            command = lambda: actor_search(),
            bootstyle = "primary outline"
            )
        search_button01.pack(
            padx = (0, 10), 
            expand = True, 
            fill = "x", 
            side = "left"
            )

        search_button02 = ttb.Button(
            master = button_frame, 
            text = "Search Second Actor", 
            command = lambda: actor_search(),
            bootstyle = "primary outline"
            )
        search_button02.pack(
            padx = (10, 0), 
            expand = True, 
            fill = "x", 
            side = "left"
            )
        
        movie_list = ttb.Frame(self, bootstyle = "primary")
        movie_list.pack(padx = 20, pady = (10, 20), fill = "both", expand = True)
    
    def actor_search(self):
        pass
        




if __name__ == "__main__":
    root = ttb.Window(
        themename = "solar",
        title = "MoviePairs 1.0",
        iconphoto = "", # ! TODO
        size = (400, 800)
        )
    root.place_window_center()
    
    Movies(root)
    
    root.mainloop()