import copy


def report(header):
    print(header)
    print(original, id(original), id(original[0]), id(original[0][1]))
    print(alias, id(alias), id(alias[0]), id(alias[0][1]))
    print(shallow, id(shallow), id(shallow[0]), id(shallow[0][1]))
    print(deep, id(deep), id(deep[0]), id(deep[0][1]))
    print('-----------------------------------')


original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)
report('Initial:')

original.append(["Databases", 5])
report('Append:')

original[0][1] = 3
report('Second operation:')

wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print(wrong_matrix, id(wrong_matrix[0]), id(wrong_matrix[1]), id(wrong_matrix[2]))

correct_matrix = [[0] * 3 for _ in range(3)]
print(correct_matrix, id(correct_matrix[0]), id(correct_matrix[1]), id(correct_matrix[2]))
