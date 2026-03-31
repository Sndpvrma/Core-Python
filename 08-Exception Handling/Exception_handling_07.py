class LoginException(Exception):

    def __init__(self, message):
        super().__init__(message)

Login_id="Admin"
Password="12345"

try:
    if Login_id=="Admin" and Password=="12345":
        print('Valid User')
    else:
        raise LoginException('Invalid User')

except LoginException as e:
    print('Login Exception:', e)