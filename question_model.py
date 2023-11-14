# class to create question objects
class Question:

    # pass in question text and answer and set to respective attributes
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
