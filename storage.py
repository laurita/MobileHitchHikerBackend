import sqlite3
import math

class Trip:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def find_closest(self, location, date, count=5):
        """
        Return list of closest trips.
        TODO: add finish to comparision
        """
        trips = map(
            lambda x: tuple(list(x) + [distance(x[2:4], location)]),
            self.all(date))

        return sorted(trips, key=lambda x: x[8])[:count]

    def all(self, date):
        if date == 0:
            self.c.execute("SELECT * FROM trips")
        else:
            self.c.execute("SELECT * FROM trips WHERE start_date = ?", (date,))
        return self.c.fetchall()

    def store(self, j):
        self.c.execute(
            "INSERT INTO trips VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (j['start'], j['end'], j['start_lat'], j['start_long'],
                j['end_lat'], j['end_long'], j['start_date'],
                j['contact'],))
        self.conn.commit()

    def close(self):
        self.c.close()
        self.conn.close()

def distance(origin, destination):
    """
    Calculate distance between two points described in lat/long.
    Taken from: http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d

#a = Trip("hitch.db")
#location = (44.010101, 11.69240,)
#print a.find_closest(location)
