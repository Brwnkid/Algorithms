
def merge(left,right):
    sorted = []
    count = 0
    i, j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted.append(left[i])
            i = i+1
        else:
            if left[i] > 2*right[j]:
                count = count + 1
            sorted.append(right[j])
            j = j+1
    if i >= len(left):
        sorted.extend(right[j:])
    else:
        sorted.extend(left[i:])
    return sorted, count

def merge_count(str):
    if len(str)==1:
        return str, 0
    else:
        mid = len(str)/2
        left = str[:mid]
        right = str[mid:]
        left, l = merge_count(left)
        right, r = merge_count(right)
        both, b = merge(left,right)
        print "left " + left + " " + str(l)
        print "right " +right+ " " + str(r)
        return both, l+r+b
