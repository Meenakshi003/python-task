numbers = [1,2,6,7,13,14,12,17,16,53,67,34,75,48]
def even_numbers(num):
    if(num%2 == 0):
        return True
    else:
        return False
evennums = filter(even_numbers, numbers)
print(' the even numbers are:')
for num in evennums:
    print(num)
