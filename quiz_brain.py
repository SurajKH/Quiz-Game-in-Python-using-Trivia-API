import html

class QuizBrain:
    """
    QuizBrain Basically considers the score calculation based on the choice made by the user
    we have considered still_has_questions,next_question,check_answer methods in QuizBrain Class
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # we basically consider unescaping the html entities over here
        q_text_variable = html.unescape(self.current_question.text)
        #return f"Q.{self.question_number}: {q_text}"
        res = str(self.question_number)+str(q_text_variable)
        return res

    # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
    # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
