from config import path
from XlsxReader import XlsxReader


xlsx = XlsxReader(path / 'questions.xlsx')
for row in range(1, xlsx.row_size + 1):
    print(xlsx.read(row)[0].value)
