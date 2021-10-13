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
        print("CLIENT CONNECTED")
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
    print("The connection failed!", data)


@sio.event
def disconnect():
    print("CLIENT DISCONNECTED")

def main():
    sio.connect('https://uat.roboteur.co.uk', headers={
        'Authorization': 'Bearer TOKEN'
    })
    # sio.wait()

if __name__ == '__main__':
    main()
