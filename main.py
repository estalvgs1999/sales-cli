import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name','company','email','position']
clients = []


def _init_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f,fieldnames= CLIENT_SCHEMA)
        for client in reader:
            clients.append(client)


def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp'
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f,fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def list_clients():
    global clients
    
    for idx,client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')


def update_client(client_uid, updated_client):
    global clients

    if client_uid - 1 <= len(clients):
        clients[client_uid] = updated_client
    else:
        print('Client is not in client\'s list')


def delete_client(client_uid):
    global clients

    if client_uid - 1 <= len(clients):
        del clients[client_uid]
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


def _get_client_field(field = 'name'):
    client_field = None

    while not client_field:
        client_field = input(f'What is the client\'s {field}? ').strip()

        if client_field == 'exit':
            sys.exit()
        
    return client_field


def _get_client_data():
    client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),

        }
    return client


def run():
    _init_clients_from_storage()
    _print_welcome()
    command = input().upper()

    if command == 'C':
        client = _get_client_data()
        create_client(client)

    elif command == 'D':
        client_uid = int(_get_client_field('uid'))
        delete_client(client_uid)

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_uid = int(_get_client_field('uid'))
        updated_client = _get_client_data()
        update_client(client_uid, updated_client)

    elif command == 'S':
        client_name = _get_client_field()
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print(f'The client: {client_name} is not in our client\'s list')
    
    else:
        print('Invalid command')

    _save_clients_to_storage()


if __name__ == "__main__":
    run()