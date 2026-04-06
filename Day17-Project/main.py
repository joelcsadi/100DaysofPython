from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    question_text = dictionary["question"]
    question_answer = dictionary["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
else:
    print(f"You finished the quiz with {quiz.score}/{len(quiz.question_list)} points.")

