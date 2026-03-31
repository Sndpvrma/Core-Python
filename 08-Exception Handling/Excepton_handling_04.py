from operator import index
a=10
b=0

try:
    c=a/b
    print('division',c)

except IndexError as e:
    print('TypeError Exception', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError Exception', e)
except Exception as e:
    print('Exception:', e)

else:
    print('in else block')
finally:
    print('in finally block')

