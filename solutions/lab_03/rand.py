import random

lst_10 = [str(random.choice(range(1, 200))) for i in range(10)]
lst_100 = [str(random.choice(range(1, 200))) for i in range(100)]
lst_1000 = [str(random.choice(range(1, 200))) for i in range(1000)]
print(lst_10)  
with open('input_task_2.txt', 'w', encoding='utf-8') as fo:
    print(' '.join(lst_10), file=fo)
    print(' '.join(lst_100), file=fo)
    print(' '.join(lst_1000), file=fo)