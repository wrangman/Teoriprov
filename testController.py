'''
TESTCONTROLLER.PY: This class is the controller for buttons etc.

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ga.ntig.se"
'''


from random import randint
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from imageUtilities import open_image

class TestController:
    def __init__(self, view, qs):   #qs has the questions
        self.view = view
        self.qs = qs
        self.selections = []
        self.test_page = None  #get the radiobuttons
        
        #test page controllers
        view.test_buttons["Nästa fråga"].config(command=self.btn_nextquestion_click)
        view.test_buttons["Tillbaka"].config(command=self.btn_previousquestion_click)
        view.test_buttons["Lämna in"].config(command=self.btn_handin_click)
        view.test_buttons["Avsluta"].config(command=self.btn_exittomenu_click)

        #start page controllers
        view.main_buttons["Starta nytt test"].config(command=self.btn_newtest_click)
        view.main_buttons["Fortsätt test"].config(command=self.btn_loadtest_click)
        view.main_buttons["Visa rekord"].config(command=self.btn_showhighscores_click)
        view.main_buttons["Avsluta"].config(command=self.btn_confirmexit_click)
        
        
    #PAGE UPDATE
    def update_test_page(self):
        self.test_page = self.view.pages["test_page"]
        
        current_question = self.qs.get_question()
                
        if current_question:
            question_text = current_question.question
            answer_a = current_question.a
            answer_b = current_question.b
            answer_c = current_question.c
            answer_d = current_question.d
            
            image_url = current_question.image_url
            
        else:
            return
        
        # Update the title label
        lbl_currentquestion = self.test_page.winfo_children()[0]  # index what question
        lbl_currentquestion.config(text=f"Fråga {self.qs.get_current_index()+1}/{self.qs.get_total_questions()}")

        # image
        lbl_image = self.test_page.winfo_children()[1]  # image
        image = open_image(f"img/{image_url}")
        
        if image:
            self.image = image
            lbl_image.config(image=image)
        else:
            lbl_image.config(image=None, text="(Bild hittades inte)", font=self.style_error)
    
        # Update the question label
        lbl_question = self.test_page.winfo_children()[2]  # label question
        lbl_question.config(text=question_text)

        # Update the radio buttons
        radio_frame = self.test_page.winfo_children()[3]  #radio buttons
        options = [answer_a,answer_b,answer_c,answer_d]
    
        selected_option = tk.StringVar()
    
        for i, option in enumerate(options):
            radio_button = radio_frame.winfo_children()[i]
            radio_button.config(text=option, value=option, variable=selected_option)
            selected_option.set(answer_a)


    def save_selection(self):
        radio_frame = self.test_page.winfo_children()[3]  #radiobuttons

        
        print(radio_frame)

    #BUTTON ACTIONS
    #test screen
    def btn_nextquestion_click(self):
        self.save_selection()
        self.qs.next_question()
        self.update_test_page()

    def btn_previousquestion_click(self):
        self.save_selection()
        self.qs.previous_question()
        self.update_test_page()
    
    def btn_handin_click(self):
        pass
    
    def btn_exittomenu_click(self):
        if messagebox.askyesno("Avsluta test", "Gå tillbaka till startmenyn?"):
            self.qs.new_test()
            self.view.show_page("start_page") 
        
    
    #start screen
    def btn_newtest_click(self):
        self.qs.get_question()
        self.view.show_page("test_page")
        self.update_test_page()
   
    def btn_loadtest_click(self):
        pass

    def btn_showhighscores_click(self):
        pass

    def btn_confirmexit_click(self):
        temp_msg = self.exit_message()
        if messagebox.askyesno("Exit", temp_msg):
            self.view.master.destroy()
            
    def exit_message(self):
        messages = ("Vill du avsluta?\nKlicka JA för att avsluta.",
                    "Säker på att du vill sluta?\nKlicka JA för att avsluta.",
                    "Vill du sluta öva inför provet nu?\nKlicka JA för att avsluta.",
                    "Kan du alla trafikregler nu?\nKlicka JA för att avsluta.",
                    "Har du viktigare saker för dig?\nKlicka JA för att avsluta.",
                    "Är du redo för det riktiga teoriprovet nu?\nKlicka JA för att avsluta.",
                    "Avsluta - är du helt säker?\nKlicka JA för att avsluta.",
                    "Kan du alla trafikskyltar?\nKlicka JA för att avsluta.",
                    "Ska du övningsköra nu?\nKlicka JA för att avsluta.",
                    "Avsluta redan?\nKlicka JA för att avsluta.")

        random_message = randint(0, len(messages) - 1)
        return messages[random_message]

    