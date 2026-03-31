print('Before')
print('Mid')

try:
    a=10
    b=0
    c=a/b
    print('Division', c)
except ZeroDivisionError as e:
    print('exception', e)
except Exception as e:
    print('exception', e)

print('After')