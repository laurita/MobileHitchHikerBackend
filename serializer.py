"""
Trip class serializor
"""

import json

def trips(trips):
    data = []

    for j in trips:
        d = {
            'start': j[0],
            'end': j[1],
            'start_lat': j[2],
            'start_long': j[3],
            'end_lat': j[4],
            'end_long': j[5],
            'contact': j[7],
            'start_date': j[6]}

        if len(j) == 9:
            d['distance'] = j[8]

        data.append(d)

    return json.dumps(data)
