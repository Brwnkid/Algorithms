def subsets(set):
    if (len(set) == 1):
        return set
    subset = subsets(set[:-1])
    return subset + " " + subset + set[-1]
