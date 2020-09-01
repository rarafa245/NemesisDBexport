import sqlite3
from typing import Dict

def insert_devices_info(message: Dict) -> bool:
    ''' Inserting data in Database - Table devices_info
        :parram message: A Dictionary holding informations
        :returns boolean indicating the succes of the operation
    '''

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()

    try:
        with conn:
            sql = '''
            INSERT INTO devices_info
                (device, type, fix, hist, ignition, date, start_time, 
                    lat, long, speed, angle, time_on)
            VALUES
                ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
            '''.format(
                    message["DEVICE"],
                    message["TYPE"],
                    message["FIX"],
                    message["HIST"],
                    message["IGNITION"],
                    message["DATE_INFOS"]["DATE"],
                    message["DATE_INFOS"]["START_TIME"],
                    message["LATITUDE"],
                    message["LONGITUDE"],
                    message["SPEED"],
                    message["ANGLE"],
                    message["TIME_ON"],
                )

            c.execute(sql)

        conn.close()
        return True
    
    except:
        return False
