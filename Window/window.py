import tkinter as tk
from tkinter import messagebox as mb


class Window:
    def __init__(self, command, question):
        self.root = tk.Tk()
        self.root.title('Опросник')
        self.root.geometry('1600x700')

        self.question = tk.Label(self.root)
        self.question.grid(row=0, columnspan=2)

        self.butt_A = tk.Button(self.root, text='A', command=lambda: command('A', question))
        self.butt_A.grid(row=1, column=0)
        self.answer_A = tk.Label(self.root)
        self.answer_A.grid(row=1, column=1)

        self.butt_B = tk.Button(self.root, text='B', command=lambda: command('B', question))
        self.butt_B.grid(row=2, column=0)
        self.answer_B = tk.Label(self.root)
        self.answer_B.grid(row=2, column=1)

        self.butt_C = tk.Button(self.root, text='C', command=lambda: command('C', question))
        self.butt_C.grid(row=3, column=0)
        self.answer_C = tk.Label(self.root)
        self.answer_C.grid(row=3, column=1)

        self.butt_D = tk.Button(self.root, text='D', command=lambda: command('D', question))
        self.butt_D.grid(row=4, column=0)
        self.answer_D = tk.Label(self.root)
        self.answer_D.grid(row=4, column=1)

        self.correct_result_label = tk.Label(self.root, fg='green', text='Правильные 0')
        self.correct_result_label.grid(row=5, column=0)
        self.uncorrect_result_label = tk.Label(self.root, fg='red', text='Неправильные 0')
        self.uncorrect_result_label.grid(row=5, column=1)

    @staticmethod
    def draw_results(correct_answer: int, uncorrect_answer):
        mb.showerror('Количество правильных ответов',
                     message=f'Количество правильных ответов {correct_answer}\n'
                             f'Количество неправильных ответов {uncorrect_answer}')

    def draw(self):
        self.root.mainloop()
