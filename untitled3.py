#ejercicio continue 
num = 0
while num <= 20:
    if num == 10 or num == 16:
        num += 2
        continue
    print(num)
    num += 2