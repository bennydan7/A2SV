def partition_labels(s):
    last_index = {}

    for i, char in enumerate(s):
        last_index[char] = i
    
    
    res = []
    size,end = 0, 0

    for i, char in enumerate(s):
        size += 1
        end = max(end,last_index[char])

        if i == end:
            res.append(size)
            size = 0
    return res


print(partition_labels(s = "ababcbacadefegdehijhklij"))