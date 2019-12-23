"""
Заданий рядок. Вивести сумму всих цифр
"""
a = ('dsad486feaf8egjytj4jytj66')
c=0
for i in a:
    if i in '0123456789':
        c+=int(i)
print(c)