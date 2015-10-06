
def naive_count(str):
    i=0
    count=0
    L=len(str)
    while i<L:
        for n in str[i+1:]:
            if n*2<str[i]: count=count+1
        i=i+1

    print count