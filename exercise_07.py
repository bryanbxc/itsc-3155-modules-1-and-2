number_list = []
even_numbers = []

while True:
    input_str = input('Enter a number or QUIT to quit: ')
    try:
        number_list.append(int(input_str))
    except ValueError:
        for i in number_list:
            if i % 2 == 0:
                even_numbers.append(i)
        print('All Numbers: ', number_list)
        print('EVEN Numbers: ', even_numbers)
        break
