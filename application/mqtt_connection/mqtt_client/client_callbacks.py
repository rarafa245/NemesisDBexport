from application.controller import on_received_message

def on_connect(client, userdata, flags, rc):
    ''' Callback - Client Connect:
        - Print information about the sucessfull of the process.
        - Subscribe in /messager topic
    '''

    if rc == 0:
        print('Client Sucessfuly Connected\n {}'.format(client))
        client.subscribe('/DB')
    else:
        print('Bad Connection Returned Code={}'.format(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    ''' Callback - Client Subscribed:
        - Print information about the sucessfull of the process
    '''

    print('Client Subscribed at /DB')
    print('QOS : {}'.format(granted_qos))


def on_disconnect(client, userdata, rc):
    ''' Callback - Client Disconnect:
        - Print information about the sucessfull of the process
    '''
    
    if rc == 0:
        print("Client Sucessfuly Disconnected")
    else:
        print("Unexpected disconnection.")


def on_message(client, userdata, message):
    ''' Callback - Receave Message:
        - Redirect Message to parseing process
    '''

    on_received_message(message.payload)
