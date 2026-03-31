try:
    a=10
    b=u
    c=a/b
    print('Division:', c)
except ZeroDivisionError as e:
    print('Exception', e)
except ValueError as e:
    print('Please number hi dalna tha')
except Exception as e:
    print('exception', e)

else:
    print('else block executed')
finally:
    print('finally block executed')
