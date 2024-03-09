import data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

"""" kullanıcıya istediğimiz sayıda ve random bir şekilde soruları göstermek için aşağıdaki kodu yazıyoruz.
"""
num_questions = 4
all_questions = [Question(q["text"], q["answer"]) for q in question_data]
selected_questions = random.sample(all_questions,num_questions)

""""kullanıcıya random değil de sırasıyla data.py deki soruların hepsini sormak için de aşağıdaki kodlar kullanılır."""
# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(q_text=question_text, q_answer=question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)
quiz = QuizBrain(selected_questions)
#if quiz still has questions remaining
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
