print(' Thi sGame Will Take Serveral Numbers And Print The Average of Them')

count = int(input('how Many Numbers Would You Like To Sum : '))

current_count = 0
summ = 0

while current_count < count:
    number = float(input('Enter The Number : '))
    summ += number
    current_count += 1


print('Summ Of All Number = ' , summ)
print(' Average Of All Number = ' , summ/count)
print(type(summ))
