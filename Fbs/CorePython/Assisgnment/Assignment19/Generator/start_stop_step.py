def my_range(start, stop, step):
    if step == 0:
        raise ValueError("step cannot be zero")

    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


res = my_range(2, 10, 2)

for i in res:
    print(i, end=" ")