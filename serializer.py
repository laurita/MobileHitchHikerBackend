"""
Journey class serializor
"""

import json

def journeys(journeys):
    data = []

    for j in journeys:
        d = {
            'start': j[0],
            'end': j[1],
            'start_lat': j[2],
            'start_long': j[3],
            'end_lat': j[4],
            'end_long': j[5],
            'comment': j[6],
            'start_date': j[7]}

        if len(j) == 9:
            d['distance'] = j[8]

        data.append(d)

    return json.dumps(data)
