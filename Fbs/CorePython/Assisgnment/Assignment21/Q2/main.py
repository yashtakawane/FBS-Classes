from televison import Television

tv = Television()

try:
    tv.getData()

except ValueError as e:
    print("Error:", e)
    tv.model = 0
    tv.screen_size = 0
    tv.price = 0

tv.display()