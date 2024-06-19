# TASK 1 AIRLINE COMPARISONS
# find out what desitnations are in both lists
# find out what destinations are in only one list
# find out what destinations are in neither list

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def find_destinations(our_routes, competitor_routes):
    
    print(f"Destinations in both lists: {our_routes.intersection(competitor_routes)}")
    print(f"Destinations in only one list: {our_routes.symmetric_difference(competitor_routes)}")
    print(f"Destinations in neither list: {our_routes.difference(competitor_routes)}")
    
find_destinations(our_routes, competitor_routes)


# TASK 2 set operations in data analysis

# Removing repeated data
def remove_repeats(data):
     return set(data)
 
print(remove_repeats(["C001", "C002", "C003", "C002", "C001", "C004"]))