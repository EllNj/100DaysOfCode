class QuizBrain:
    # attributes q number and q list
    # method next question
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q.text} (True/False)? ")
        self.check_answer(user_answer, current_q.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
