def linear_search(el, lst):
    """Линейный поиск элемента в списке"""
    cnt = 0
    for idx in range(len(lst)):
        cnt += 1
        if lst[idx] == el:
            return idx + 1, cnt
    return -1, cnt


def is_prime(num):
    """Проверка, является ли число простым"""
    if num < 2: return False
    for denominator in range(2, int(num ** 0.5) + 1):
        if num % denominator == 0:
            return False
    return True


def binary_search(arr, low, high, V):
    """Бинарный поиск в отсортированном списке"""
    cnt = 0
    while high >= low:
        cnt += 1
        mid = low + ((high - low) // 2)
        if V == arr[mid]:
            return mid + 1, cnt
        elif V < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, cnt


def selection_sort(arr):
    """Сортировка выбором"""
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

    summa = 0
    mn =  float('inf')
    mx = float('-inf')
    even = 0
    gt_av_count = 0

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
            gt_av_count += 1

    print(f"Сумма: {summa}")
    print(f"Минимум: {mn}")
    print(f"Максимум: {mx}")
    print(f"Чётных: {even}")
    print(f"Выше среднего ({av:.2f}): {gt_av_count}")

    search_num = int(input('Введите число: '))
    print('Индекс:', linear_search(search_num, measurements)[0], end='\n\n')

    print('IS_PRIME:')
    for num in [1, 3, 5, 4, 7, 9, 11, 12, 17]:
        print(num, is_prime(num))
    print()

    with open('input_task_2.txt', 'r', encoding='utf-8') as fi:
        arr_10 = list(map(int, fi.readline().split()))
        arr_100 = list(map(int, fi.readline().split()))
        arr_1000 = list(map(int, fi.readline().split()))

    selection_sort(arr_10)
    selection_sort(arr_100)
    selection_sort(arr_1000)

    print(10, linear_search(151, arr_10), binary_search(arr_10, 0, 9, 151))
    print(100, linear_search(151, arr_100), binary_search(arr_100, 0, 99, 151))
    print(1000, linear_search(151, arr_1000), binary_search(arr_1000, 0, 999, 151))



if __name__ == '__main__':
    main()
