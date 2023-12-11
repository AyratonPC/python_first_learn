def check(num):
    if not num == 0:
        if num % 2 == 0:
            print('Even number')
        else:
            print('Odd number')
    else:
        print('0')


user_num = int(input('Enter ur number: '))
check(user_num)
