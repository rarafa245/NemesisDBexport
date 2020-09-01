import json
from typing import Dict

def on_received_message(message: bytearray) -> bool:
    
    # Traducing message
    traducing_message(message)


def traducing_message(message: bytearray) -> Dict:
    '''
        Traducing a bytearray json message into a Dictionary message
        :parram - message: bytearray json message
        :return - dictionary with traduced message
    '''

    json_message = message.decode('utf8')
    traduced_message = json.loads(json_message)
    
    return traduced_message


def checking_message(traduced_message: Dict) -> bool:
    
    if traduced_message["TYPE"] == 'LOC':
        return True
    
    return False
