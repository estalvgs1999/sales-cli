
PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('Enter password: ')

        if password == PASSWORD:
            return func()
        else:
            print('Incorrect password')
    return wrapper


@password_required
def needs_password():
    print('Correct password')


def upper(func):
    # Get parameters without explicitly passing them
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    return wrapper


@upper
def say_my_name(name):
    return f'Hello {name}!'
    

if __name__ == '__main__':
    #needs_password()
    result = say_my_name('esteban')
    print(result)