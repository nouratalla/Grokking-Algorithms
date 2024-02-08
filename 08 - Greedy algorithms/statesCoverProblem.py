states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])




def cover(states_needed, stations):
    #hold final stations
    finalStations = set()
  
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            # to get instersection between states we want to cover and states staions cover
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered) and station not in finalStations:
                best_station = station
                states_covered = covered
        if best_station is not None:
            states_needed -= states_covered
            finalStations.add(best_station)
            stations.pop(best_station)
        else:
            return None
    return finalStations

print(cover(states_needed, stations))