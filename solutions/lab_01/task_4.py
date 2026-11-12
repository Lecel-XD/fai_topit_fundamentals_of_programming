student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[0], student.split()[0][-1])                                                            #1
print(student.split()[0], student.split()[1])                                                        #2
print(student.upper(), student.lower())                                                              #3
print(f'{student.split()[0][0]}.{student.split()[1][0]}')                                            #4
print(course[::-1])                                                                                  #5

print('%s — %s: %d/%d (%.1f%%)' % (student, course, completed, total, completed * 100 / total))      #6
print('{} — {}: {}/{} ({}%)'.format(student, course, completed, total, completed * 100 / total))
print(f'{student} — {course}: {completed}/{total} ({completed * 100 / total}%)')

symbol = "Я"                                                                                         #7
print(symbol, ord(symbol), chr(ord(symbol)), symbol.encode("utf-8"), len(symbol.encode("utf-8")))

# symbol[0] = 'A'                                                                                    #8




