from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# For loop - for item in list
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
       
quiz = QuizBrain(question_bank)

while quiz.questions_remaining():
    quiz.next_question()
