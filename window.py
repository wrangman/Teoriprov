'''
WINDOW.PY: Actual program window which can display the different pages

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ga.ntig.se"
'''

import tkinter as tk
from tkinter import *
from imageUtilities import open_image

class Window(tk.Frame):
   def __init__(self, parent, qs):
      super().__init__(parent)
      self.place_window()
      
      #Set the window icon & title
      icon = tk.PhotoImage(file = "Teoriprov/img/k_logo16.png")
      self.master.iconphoto(False, icon)
      self.master.title("Teoriprov")
      
      #Define the global styles for fonts
      self.style_btn = ("Arial", 16)
      self.style_title = ("Arial", 36, "bold")
      self.style_question = ("Arial", 24, "bold")
      self.style_copy = ("Arial", 16)
      self.style_error = ("Arial", 16, "italic")
      self.padx, self.pady, self.width, self.padding = 16, 8, 0, 12

      self.test_buttons = {}
      self.main_buttons = {}
           
      self.qs = qs
      
      #Create the pages
      self.pages = {}  # Dictionary to store different frames
      self.draw_start_page()
      self.draw_test_page()
      self.show_page("start_page") #show first

      
   def draw_test_page(self):
       
      frame_testpage = tk.Frame(self)
      
      # Create a label for the title
      lbl_currentquestion = tk.Label(frame_testpage, text="Fråga 0/0", font=self.style_title)
      lbl_currentquestion.pack(side="top", fill="x", padx=self.padding, pady=self.padding)
      
      # image
      image = open_image("Teoriprov/img/q1.png")
      
      #TODO: error handling doesnt' work here      
      if image:
         lbl_image = tk.Label(frame_testpage, image=image)
         lbl_image.image = image  # Keep a reference to the image
         lbl_image.pack(fill="both")
      else:
         lbl_image = tk.Label(frame_testpage, text="(Bild hittades inte)", font=self.style_error)
         lbl_image.pack(fill="both")
         
      # Create a label for the question
      lbl_question = tk.Label(frame_testpage, text="(n/a)", font=self.style_question)
      lbl_question.pack(fill="x", padx=self.padding, pady=self.padding)
      
      # radio buttons
      frame_radiobuttons = tk.Frame(frame_testpage)
      frame_radiobuttons.pack(side="left", padx=self.padding, pady=self.padding/2)
      
      selected_option = tk.StringVar() 

      options = ["1", "2", "3", "4"]

      for option in options:
         radio_button = tk.Radiobutton(frame_radiobuttons, text=option, variable=selected_option, value=option, font=self.style_copy)
         radio_button.pack(anchor="nw", padx=self.padding, pady=self.padding/2)
      
      # Place the buttons at the bottom without overlapping the window
      frame_buttons = tk.Frame(frame_testpage)
      frame_buttons.pack(side="bottom", fill="x", pady=self.padding)
      
      button_data = ["Nästa fråga",
                     "Tillbaka",
                     "Lämna in",
                     "Avsluta"]

      for i, label in enumerate(button_data):
         button = tk.Button(frame_buttons, text=label, padx=self.padx, pady=self.pady, width=self.width, font=self.style_btn, command=None)
         if i == 0 or i == len(button_data) - 1: 
            button.pack(side="right", padx=self.padding)
         else:
            button.pack(side="right", padx=self.padding/2)
         
         self.test_buttons[label] = button  # Store the button in a dictionary with its label as the key

      self.test_buttons["Nästa fråga"].config(fg="#fff", bg="#2C91ED")

      self.pages["test_page"] = frame_testpage
      

   def draw_start_page(self):
      frame_startpage = tk.Frame(self)
      
      # Add a title label
      lbl_title = tk.Label(frame_startpage, text="Teoriprov: Körkort", font=self.style_title)
      lbl_title.pack(side="top", fill="x", padx=self.padding, pady=self.padding)
      
      # Create a frame for the main content
      frame_content = tk.Frame(frame_startpage)
      frame_content.pack(fill="both", expand=True)
      
      # Create a frame for the message and bullet points
      frame_info = tk.Frame(frame_content)  # Add a background color for visualization
      frame_info.grid(row=0, column=0, padx=self.padding, pady=self.padding, sticky="nswe")

      # Add the message
      wrap = round((self.winfo_screenwidth()/2)/2) #calc width of screen and make sure text wraps nicelyl.
      
      lbl_message = tk.Label(frame_info, text="Öva inför teoriprovet med denna app - om du fortfarande inte klarar provet är det dig det är fel på - bwhaha!", wraplength=wrap, font=self.style_copy, justify="left")
      lbl_message.pack(fill="both", expand=True, padx=self.padding, pady=self.padding*2)

      # Add the bullet points
      bullet_points = ["Starta testet här eller fortsätt ett tidigare test",
                     "Du har 20 minuter på dig",
                     "När tiden är ute lämnas provet in automatiskt",
                     "Testet sparas automatiskt i bakgrunden",
                     "Avsluta med krysset högst upp till höger"]

      formatted_text = "\n".join([f"• {item}\n" for item in bullet_points])

      lbl_bulletlist = tk.Label(frame_info, text=formatted_text, font=self.style_copy, justify="left")
      lbl_bulletlist.pack(side="left", fill="both", expand=False, padx=self.padding, pady=self.padding)

      # Add an image (replace with your image file path)
      image = tk.PhotoImage(file="Teoriprov/img/start.png")
      lbl_image = tk.Label(frame_content, image=image)
      lbl_image.image = image
      lbl_image.grid(row=0, column=1, padx=self.padding*2, pady=self.padding, sticky="nsew")

      # Configure the column to expand
      frame_content.columnconfigure(0, weight=1)

      # Add buttons for frame_startpage
      button_data = ["Avsluta",
                     "Visa rekord",
                     "Fortsätt test",
                     "Starta nytt test"]
     
      # Create a button frame for the buttons on the bottom
      frame_buttons = tk.Frame(frame_startpage)
      frame_buttons.pack(side="right", fill="x")
      
      for i, label in enumerate(button_data):
         button = tk.Button(frame_buttons, text=label, padx=self.padx, pady=self.pady, width=self.width, font=self.style_btn, command=None)
         if i == 0 or i == len(button_data) - 1: 
            button.grid(row=0, column=i, padx=self.padding, pady=self.padding)
         else:
            button.grid(row=0, column=i, padx=self.padding/2, pady=self.padding)
         self.main_buttons[label] = button

      self.main_buttons["Starta nytt test"].config(fg="#fff", bg="#2C91ED")
      
      self.pages["start_page"] = frame_startpage
         

   def show_page(self, show):
      for page_name, page_frame in self.pages.items():
         if page_name != show:
            page_frame.pack_forget()  # Hide other frames
         else:
            page_frame.pack(fill="both", expand=True)  # Show the selected

                  
   #WINDOW SPECIFIC
   def place_window(self):
      self.pack(fill="both", expand=True)
      # self.master.resizable(False, False)
      
      screen_width = self.winfo_screenwidth()
      screen_height = self.winfo_screenheight()

      if screen_width > 1920:
         width=1129
         height=820
      else:
         width = round(screen_width/1.7)     #approx half screen size
         height = round(screen_height/1.15)
      
      x = (screen_width - width) // 2
      y = (screen_height - height) // 2

      self.master.minsize(width, height)
      self.master.geometry(f"{width}x{height}+{x}+{y}")

   def initialize(self):
      self.mainloop()