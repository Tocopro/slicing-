a = [11, 22, 45, 8, 22, 34, 20, 78, 89, 99, 5, 1]


def slicing_list():
    list_length = len(a)
    sizes = int(list_length / 3)
    begin = 0
    end = sizes

    for i in range(3):
        indexes = slice(begin, end)
        sample = a[indexes]

        print(i, sample)
        print(list(reversed(sample)))

        begin = end
        end += sizes


slicing_list()
