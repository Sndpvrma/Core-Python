try:
    number = int(input('Enter a number: '))

    if number > 10:
        raise Exception('Invalid number')
except Exception as e:
    print('Exception:', e)

print('After')

