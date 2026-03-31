class Loginerror(Exception):
    pass
def check_login(username ,password):
    correct_user= 'admin'
    correct_pass= '12345'

    if username != correct_user or password != correct_pass:
        raise Loginerror("Incorrect username or password")
    else:
        print('Login Successful')

try:
    user_input = input('Enter your username: ')
    pass_input = input('Enter your password: ')
    check_login(user_input,pass_input)

except Loginerror as e:
    print(f"Error catch: {e}")

except Exception as other_e:
    print(f"Other error catch: {other_e}")

finally:
    print("Login process finished")