def read_file_content(file=None):
    return [line.rstrip() for line in open(file)]

def compare_lists(list1=[], list2=[]):
    unique = []
    for i in list1:
        if i not in list2:
            unique.append(i)
        else:
            if i not in _overlap:
                _overlap.append(i)
    return unique

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print('Usage: domain-diff.py file1.txt file2.txt')
    else:
        _overlap = []
        print()
        l1 = read_file_content(sys.argv[1])
        l2 = read_file_content(sys.argv[2])
        _unique_l1 = compare_lists(l1, l2)
        _unique_l2 = compare_lists(l2, l1)

        print(f"Unique values in {sys.argv[1]}:")
        print(*_unique_l1, sep="\n", end="\n\n\n")
        print(f"Unique values in {sys.argv[2]}:")
        print(*_unique_l2, sep="\n", end="\n\n\n")
        print(f"Duplicate values in both lists:")
        print(*_overlap, sep="\n", end="\n\n")