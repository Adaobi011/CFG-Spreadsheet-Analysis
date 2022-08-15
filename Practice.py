text_file = open('people.txt', 'w')
people = 'Joanne \nSusan \nAmina'
text_file.write(people)
text_file.close()

with open('people.txt', 'r') as text_file:
    contents = text_file_read(people)
print(contents)

new_item = input('Enter a to-do item: ')

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()
todo = todo + new_item + '\n'

with open('todo.txxt', 'w+') as todo_file:
    todo_file.write(todo)

import csv

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]
with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names, lineterminator='\n')

    spreadsheet.writeheader()
    spreadsheet.writerows(data)§1§
