from Window import Window
from config import path
from XlsxReader import XlsxReader
import random


class Question:
    def __init__(self, question_path):
        self.correct = None
        self.result = 0
        self.row = 0

        self.xlsx = XlsxReader(question_path)
        self.window = Window(command, self)

    def next(self):
        if self.xlsx.row_size == self.row:
            self.window.results(self.result)
            exit()

        self.row += 1
        data = self.xlsx.read(self.row)

        self.window.question.configure(text=data[0].value)
        answer_id = list(range(1, 5))

        random.shuffle(answer_id)

        self.window.answer_A.configure(text=data[answer_id[0]].value)
        self.window.answer_B.configure(text=data[answer_id[1]].value)
        self.window.answer_C.configure(text=data[answer_id[2]].value)
        self.window.answer_D.configure(text=data[answer_id[3]].value)

        self.correct = ['A', 'B', 'C', 'D'][answer_id.index(1)]


def command(choose: str, quest: Question):
    if quest.correct == choose:
        quest.result += 1
        print('\u001b[32m Правильно')
    else:
        print('\u001b[31m Неправильно')
    quest.next()


def main():
    question = Question(path / 'questions.xlsx')
    question.next()
    question.window.draw()


if __name__ == '__main__':
    main()
