"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""

text = 'абв сабва лиабвам лол сабля лошадь'

text = text.split()
text = [word for word in text if 'абв' not in word]
print(' '.join(text))
