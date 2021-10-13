# import click
import socketio
sio = socketio.Client(logger=True, engineio_logger=True)

def handleFind(err, msg):
    print('FIND DATA', err, msg)
    sio.disconnect()
    pass

def handleCreate(err, msg):
    print('CREATE DATA', err, msg)
    sio.disconnect()
    pass

@sio.event
def connect():
    try:
        print("I'm connected!")
        sio.emit('find', ('shape-storage-record', {
            'storageId': 'a8d3d31b-9acc-4f0e-a3a0-cfcd8cf87315'
        }), callback=handleFind)
        sio.emit('create', ('reaction', {
            'serviceId': 'a8ada11c-e1dd-4997-9f4e-7e8c51775540',
            'reactor': 'Create User account API',
            'payload': {'about': '', 'name': 'barry', 'lastName': 'buck', 'dob': '1983-01-06', 'age': '38', 'gender': 'Male', 'saCitizen': 'Yes', 'password': 'asdfg', 'email': 'commissar@spacepencil.co.uk'}
        }), callback=handleCreate)
        # sio.disconnect()
    except Exception as ex:
        print('ERROR', ex)
        sio.disconnect()


@sio.event
def connect_error(data):
    print("The connection failed!")


@sio.event
def disconnect():
    print("I'm disconnected!")

# @click.group()
# def roboteur_client_python():
#     pass


# @roboteur_client_python.command()
# def user():
#     '''Command on roboteur_client_python'''
#     click.echo('create user on service https://uat.roboteur.co.uk/api/reaction')
def main():
    sio.connect('https://uat.roboteur.co.uk', headers={
        'Authorization': 'Bearer TOKEN'
    })
    # sio.wait()

    # try:
    # sio.emit('create', data={
    #     'serviceId': 'a8ada11c-e1dd-4997-9f4e-7e8c51775540',
    #     'reactor': 'Create User account API',
    #     'payload': {'about': '', 'name': 'barry', 'lastName': 'buck', 'dob': '1983-01-06', 'age': '38', 'gender': 'Male', 'saCitizen': 'Yes', 'password': 'asdfg', 'email': 'commissar@spacepencil.co.uk'}
    # }, namespace='/reaction')

    #     sio.disconnect()
    # except Exception as ex:
    #     print(ex)
    #     sio.disconnect()


# @roboteur_client_python.command()
# def cmd2():
#     '''Command on roboteur_client_python'''
#     click.echo('roboteur_client_python cmd2')


if __name__ == '__main__':
    main()
    # roboteur_client_python()
