numbers_list = []
unique_numbers = []

for i in range(10):
    num = int(input(f'Enter number {i+1}: '))
    numbers_list.append(num)

for i in numbers_list:
    if numbers_list.count(i) == 1:
        unique_numbers.append(i)

print('Original List: ', numbers_list)  
print('Numbers that appear once: ', unique_numbers)
