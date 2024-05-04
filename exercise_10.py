input_string = input("Enter a string: ")
string_list = list(input_string)
new_string_list = []

for k in range(0, len(string_list), 3):
    new_substring_list = []
    for i in range(0, 3):
        if (k + i) < len(string_list):
            new_substring_list.append(string_list[k + i])
    new_string_list.append(new_substring_list)

print(new_string_list)
