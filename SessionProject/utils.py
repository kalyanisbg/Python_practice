def search_flights(fid, flights):
    for flight in flights:
        if flight['flight_id'] == fid:
            return flight
    return None

def get_index(fid, flights):
    for i, flight in enumerate(flights):
        if flight['flight_id'] == fid:
            return i
    return -1