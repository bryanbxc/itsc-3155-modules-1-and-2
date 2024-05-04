str1 = input('Enter a string: ')
str2 = input('Enter another string: ')

if str1 in str2:
    print("True")
elif str2 in str1:
    print("True")
else:
    print("False")