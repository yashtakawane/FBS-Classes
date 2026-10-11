def maxProduct(l1):
    s1 = set(l1)
    l2 = list(s1)
    max_product = l2[0] * l2[1]
    num1 = l2[0]
    num2 = l2[1]

    for i in range(0, len(l2)):
        for j in range(i + 1, len(l2)):
            product = l2[i] * l2[j]

            if product > max_product:
                max_product = product
                num1 = l2[i]
                num2 = l2[j]

    return num1, num2, max_product


l1 = [-10, -5, 2, 3, 4]
res = maxProduct(l1)
print(res)