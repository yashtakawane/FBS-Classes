def groupAnagrams(l1):
    d1 = {}

    for word in l1:
        key = "".join(sorted(word))

        if key in d1:
            d1[key].append(word)
        else:
            d1[key] = [word]

    return list(d1.values())


l1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = groupAnagrams(l1)
print(res)