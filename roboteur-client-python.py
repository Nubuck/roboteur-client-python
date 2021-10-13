import click
import socketio
sio = socketio.Client(logger=True, engineio_logger=True)

@sio.on('*')
def catch_all(event, sid, data):
    print('on all', event, sid, data)
    pass

@sio.on('create', namespace='/reaction')
def create(sid, data):
    print('on reaction create')
    print(sid, data)

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@click.group()
def roboteur_client_python():
    pass


@roboteur_client_python.command()
def user():
    '''Command on roboteur_client_python'''
    click.echo('create user on service https://uat.roboteur.co.uk/api/reaction')
   
    sio.connect('https://uat.roboteur.co.uk', headers={
        'Authorization': 'Bearer xxxx'
    }, namespaces=['/reaction'])

    try:     
        # sio.emit('create', data={
        #     'serviceId': 'a8ada11c-e1dd-4997-9f4e-7e8c51775540',
        #     'reactor': 'Create User account API',
        #     'payload': {'about': '', 'name': 'barry', 'lastName': 'buck', 'dob': '1983-01-06', 'age': '38', 'gender': 'Male', 'saCitizen': 'Yes', 'password': 'asdfg', 'email': 'commissar@spacepencil.co.uk'}
        # }, namespace='/reaction')
     
        sio.disconnect()
    except Exception as ex:
        print(ex)
        sio.disconnect()


@roboteur_client_python.command()
def cmd2():
    '''Command on roboteur_client_python'''
    click.echo('roboteur_client_python cmd2')


if __name__ == '__main__':
    roboteur_client_python()
