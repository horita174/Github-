def loop(num):
    while True:
        if num >= 15:
            return num
        else:
            num += 1
        print(num)

num = 10
print(loop(num))
