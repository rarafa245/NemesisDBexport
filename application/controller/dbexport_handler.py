import json
from typing import Dict
from application.model import insert_devices_info

def on_received_message(message: bytearray) -> bool:
    
    # Traducing message
    traduced_message = traducing_message(message)

    # Checking message
    check = checking_message(traduced_message)

    # Acting


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
