from Day17_question_model import Question
from Day17_data import question_data
from Day17_quiz_brain import QuizBrain

question_bank = []
for each in question_data:
    new_question = Question(each["question"], each["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print(f"You've completed the quiz!\nYour final score is: {quiz.score}/{len(question_bank)} ")