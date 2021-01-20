
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    clients += f'{client_name},'


def list_clients():
    global clients
    for client in clients.split(','):
        print(f'- {client}')

def _print_welcome():
    print('WELCOME TO SALES CLI')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == "__main__":
    _print_welcome()
    command = input()

    if command.upper() == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()