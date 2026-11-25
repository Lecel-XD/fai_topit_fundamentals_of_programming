def linear_search(el, lst):
    for idx in range(len(lst)):
        if lst[idx] == el:
            return idx
    return -1


def is_prime(num):
    for denominator in range(2, int(num ** 0.5) + 1):
        if num % denominator == 0:
            return False
    return True



measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

summa = 0
mn =  float('inf')
mx = float('-inf')
even = 0
av_count = 0

# finds min, max, sum, average
for num in measurements:
    summa += num
    if num < mn:
        mn = num
    if num > mx:
        mx = num
    if num % 2 == 0:
        even += 1
av = summa / len(measurements)

# finds num of elements greater than average
for num in measurements:
    if num > av:
        av_count += 1

print(f"Сумма: {summa}")
print(f"Минимум: {mn}")
print(f"Максимум: {mx}")
print(f"Чётных: {even}")
print(f"Выше среднего ({av:.2f}): {av_count}")
