number = int(input('Enter a number: '))
number_list = []

for i in range(number):
    input_number = float(input(f'Enter Number {i+1}: '))
    number_list.append(input_number)

print(f'List: {number_list}')    
print('Average: ', sum(number_list) / len(number_list))
