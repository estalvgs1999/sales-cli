import sys

clients = ['Pablo','Ricardo']

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already in the client\'s list')


def list_clients():
    global clients
    
    for idx,client in enumerate(clients):
        print(f'{idx}: {client}')


def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print('Client is not in client\'s list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in client\'s list')


def search_client(client_name):
    for client in clients:
        if client == client_name:
            return True
    
    return False


def _print_welcome():
    print('WELCOME TO SALES CLI')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ').strip()

        if client_name == 'exit':
            sys.exit()
        
    return client_name

if __name__ == "__main__":
    _print_welcome()
    command = input().upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_name = input('What is the updated client name? ')
        update_client(client_name, updated_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')
    else:
        print('Invalid command')
        