first_list = []
second_list = []

for x in range(2):
    for i in range(5):
        if x < 1:
            num_a = int(input('Enter a number for the first list: '))
            first_list.append(num_a)
        else:
            num_b = int(input('Enter a number for the second list: '))
            second_list.append(num_b)
        
print(f'First list: {first_list}')  
print(f'Second list: {second_list}')   
print('Common list: ', list(set(first_list) & set(second_list)))
