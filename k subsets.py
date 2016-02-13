def all_k_subsets(s, k):
    myset = set()
    if k == 0 or len(s) < k:
        myset.add("")
        return myset
    if len(s) == k:
        myset.add(s)
        return myset
    else:
        first = s[0]
        rest = s[1:]
        subsets = all_k_subsets(rest,k-1)
        myset.update(all_k_subsets(rest,k))
        for i in subsets:
            myset.add(first + i)    #create all of the subsets involving the first letter
        return myset
