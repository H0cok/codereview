"""
Користувач воодить речення на англійській мові, розділяючи слова пробілами. Вивести список, кожний елемент якого є списком, де
перший елемент - кожне друге слово речення, а другий кількість повторів цьогого слова у реченні.
"""
import re
def find_text(text):
    n= re.split(' ',text)
    fin=[]
    for i in n:
        b=re.findall('[A-Za-z]{1,}',i)
        if b =='':
            b=' '
        fin.append(b[0])
        print(b)
    fin1=[]
    for i in fin[::2]:
        k=0
        k=len(re.findall(str(i),str(fin)))
        fin1.append([i,k])
    return fin1
a= find_text(input())
print(a)
