def check_num(num):
    if num != 0:
        if num % 7 == 0:
            print('Number is multiple 7')
        else:
            print('Number is not multiple 7')
    else:
        print('0')


number = int(input('Enter ur number: '))
check_num(number)
