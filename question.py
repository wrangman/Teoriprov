'''
QUESTION.PY: Question class that stores question info

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ga.ntig.se"
'''

class Question:
   
    total_question_index = 0
    
    def __init__(self, question, a, b, c, d, key, image_url=None):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.key = key
        self.image_url = image_url
        
        Question.add_question()
            
    @classmethod
    def total_questions(cls):
        return cls.total_question_index
    
    @classmethod
    def add_question(cls):
        cls.total_question_index += 1
    
    
    
    
    