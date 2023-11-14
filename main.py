# import required modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import UserInterface

# empty list to hold Question objects
question_bank = []
# loop through question_data to extract data
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # use extracted q text and answer to create new Question object and add to question bank
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create QuizBrain object and pass in list of Question objects
quiz = QuizBrain(question_bank)
# create user interface
quiz_interface = UserInterface(quiz)
