'''
QUESTIONSMANAGER.PY: Loads questions and has modules specific to the questions like next question etc.

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ga.ntig.se"
'''

import json
from question import Question

class QuestionsManager():
    def __init__(self):
        self.current_question_index = 0  
        self.questions = []
        
        self.load_from_json("questions.json")
 
 
    def load_from_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for entry in data:
                question = Question(
                    entry['question'],
                    entry['A'],
                    entry['B'],
                    entry['C'],
                    entry['D'],
                    entry['key'],
                    entry.get('image_url', None)
                )
                self.questions.append(question)
                
    def get_question(self):
        return self.questions[self.current_question_index]
    
    def get_current_index(self):
        return self.current_question_index
    
    def get_total_questions(self):
        return Question.total_question_index
    
    def new_test(self):
        self.current_question_index = 0
    
    def next_question(self):
        if self.get_current_index() < self.get_total_questions()-1:
            # self.save_selection()
            self.current_question_index += 1
        else:
            print("No more questions available.")

    # def save_selection(self):
    #     self.view.selected_choices[question_number] = selected_option
    
    def previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
        else:
            print("Already at the first question.")
