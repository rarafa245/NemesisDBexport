import json
from typing import Dict
from application.model import insert_devices_info

def on_received_message(message: bytearray) -> bool:
    ''' Callback function to process the received message:
            Traducing, Checking, Acting
        :parram - message: raw message in bytearray
        :return - boolean with success/failure of all processes
    '''
    
    # Traducing message
    traduced_message = traducing_message(message)

    # Checking message
    checker = checking_message(traduced_message)

    # Acting
    confirm = registering_message(traduced_message, checker)

    return confirm


def traducing_message(message: bytearray) -> Dict:
    ''' Traducing a bytearray json message into a Dictionary message
        :parram - message: bytearray json message
        :return - dictionary with traduced message
    '''

    json_message = message.decode('utf8')
    traduced_message = json.loads(json_message)
    
    return traduced_message


def checking_message(traduced_message: Dict) -> bool:
    ''' Checking if the message can be storage (LOC Type)
        :parram - Dictionary with messages
        :return - boolean with the check of the message
    '''
    
    if traduced_message["TYPE"] == 'LOC':
        return True
    
    return False


def registering_message(message: Dict, checker: bool) -> bool:
    ''' Registering message in DB
        :parram - message: Dictionary with the message
                - checker: Boolean with the confirmation 
                            of the message
        :return - boolean with the success/faluir of the message
    '''
    
    if checker:
        # If Message is checked
        inserting = insert_devices_info(message)
        return inserting
    
    return False