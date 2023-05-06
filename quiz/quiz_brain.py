class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def has_next(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number} {question.text} (True/False/t/f)?: ')
        self.check_answer(user_answer, question.answer)

    def check_answer(self, user_answer, answer):
        user_answer = user_answer.lower()
        print(answer)
        if answer == 'True':
            if user_answer == 'true' or user_answer == 't' or user_answer == 'yes' or user_answer == 'y':
                print("That's right!")
                self.score += 1
            else:
                print("That's wrong")
        elif answer == 'False':
            if user_answer == 'false' or user_answer == 'f' or user_answer == 'no' or user_answer == 'n':
                print("That's right!")
                self.score += 1
            else:
                print("That's wrong")
        print(f'You current score is {self.score}/{self.question_number}')
        print('\n')


