def get_sharpees(n):
    sharpees = []
    i = 1
    while len(sharpees) < n:
        summ=0
        summ=sum(digit for digit in str(i))
        if summ%5==0:
            sharpees.append(i)
        i += 1
    return sharpees
n = 5
sharpees_array = get_sharpees(n)
print(sharpees_array)