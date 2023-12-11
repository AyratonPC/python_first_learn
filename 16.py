def main():
    number_1 = int(input('Enter first num: '))
    number_2 = int(input('Enter second num: '))
    how_do = input('Enter ur do: "/" or "*" or "+" or "sr_arfm": ')

    def what_do(answer, num_2, num_1):
        if answer == '*':
            return num_1 * num_2
        elif answer == '-':
            return num_1 - num_2
        elif answer == '+':
            return num_1 + num_2
        elif answer == 'sr_arfm':
            return (num_1 + num_2) / 2
        else:
            print('Not have the do')

    print(what_do(how_do, number_2, number_1))


main()
