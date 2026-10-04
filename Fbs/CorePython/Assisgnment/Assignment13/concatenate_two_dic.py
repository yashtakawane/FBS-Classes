def concatenate(d1,d2,d3):
    for key in d1:
        d3[key]=d1[key]

    for key in d2:
        d3[key]=d2[key]

    return d3

d1 = {1: "Yash", 2: "Raj"}
d2 = {3: "Ram", 4: "Amit"}
d3 = {}

res = concatenate(d1, d2, d3)

print(res)