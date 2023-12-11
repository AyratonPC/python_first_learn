def check_two_numbers(num, num2):
    if num > num2:
        return num
    return num2


first_user_num = int(input('Enter ur first number: '))
second_user_num = int(input('Enter ur second number: '))
print(check_two_numbers(first_user_num, second_user_num))
