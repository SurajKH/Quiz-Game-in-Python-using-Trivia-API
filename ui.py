# import statements
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


# we have set the theme color to color with code '#375362'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        # Window Configuration
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Total Score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas Creation
        self.canvas = Canvas(width=300, height=200, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill="black")

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        q_text = self.quiz.next_question()
        print(q_text)
        self.canvas.itemconfig(self.question_text, text=q_text)

        # We have considered the true and false buttons over here
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_check)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, comman=self.false_check)

        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def true_check(self):
        self.quiz.check_answer("True")

    def false_check(self):
        self.quiz.check_answer("False")
