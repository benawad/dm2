def compose(rel1, rel2):
    new_set = []
    for i in rel2:
        for j in rel1:
            if i[1] == j[0]:
                new_set.append((i[0], j[1]))
    return set(new_set)


def main():
    rel1 = set([(1, 2), (1, 3), (2, 3), (2, 4), (3, 1)])
    rel2 = set([(2, 1), (3, 1), (3, 2), (4, 2)])
    print("R1: %s" % rel1)
    print("R2: %s" % rel2)
    print("R1 compose R2: %s" % compose(rel1, rel2))
    print("R2 compose R1: %s" % compose(rel2, rel1))


if __name__ == '__main__':
    main()
