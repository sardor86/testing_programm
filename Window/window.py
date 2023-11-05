import tkinter as tk


class Window:
    def __init__(self, command_a, command_b, command_c, command_d):
        self.root = tk.Tk()
        self.root.title('Опросник')
        self.root.geometry('800x700')

        self.question = tk.Label(self.root)
        self.question.grid(row=0)

        self.butt_A = tk.Button(self.root, text='A', command=command_a)
        self.butt_A.grid(row=1, column=0)
        self.answer_A = tk.Label(self.root)
        self.answer_A.grid(row=1, column=1)

        self.butt_B = tk.Button(self.root, text='B', command=command_b)
        self.butt_B.grid(row=2, column=0)
        self.answer_B = tk.Label(self.root)
        self.answer_B.grid(row=2, column=1)

        self.butt_C = tk.Button(self.root, text='C', command=command_c)
        self.butt_C.grid(row=3, column=0)
        self.answer_C = tk.Label(self.root)
        self.answer_C.grid(row=3, column=1)

        self.butt_D = tk.Button(self.root, text='D', command=command_d)
        self.butt_D.grid(row=4, column=0)
        self.answer_D = tk.Label(self.root)
        self.answer_D.grid(row=4, column=1)

    def draw(self):
        self.root.mainloop()
