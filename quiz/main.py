from data import Data
from question_model import Question
from quiz_brain import QuizBrain

difficulty = input('difficulty (easy, medium) default (medium) : ')
data = Data(difficulty)
question_list = data.get()
question_bank = [Question(data['question'],data['correct_answer']) for data in question_list]
quiz = QuizBrain(question_bank)

while quiz.has_next():
    quiz.next_question()

print('You\'ve completed the quiz')
print(f'Your final score is {quiz.score}/{quiz.question_number}')
