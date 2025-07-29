from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_distance_finder")
    location = geolocator.geocode(city_name)
    if location:
        return (location.latitude, location.longitude)
    else:
        print(f" Could not find coordinates for: {city_name}")
        return None

def calculate_distance():
    print(" Distance Between Two Cities Calculator")

    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")
    unit = input("Choose unit (km/mi): ").strip().lower()

    coord1 = get_coordinates(city1)
    coord2 = get_coordinates(city2)

    if not coord1 or not coord2:
        print(" Calculation failed due to invalid city input.")
        return

    distance = geodesic(coord1, coord2)

    if unit == "km":
        print(f"\n Distance between {city1} and {city2} is: {distance.kilometers:.2f} kilometers.")
    elif unit == "mi":
        print(f"\n Distance between {city1} and {city2} is: {distance.miles:.2f} miles.")
    else:
        print(" Invalid unit. Use 'km' or 'mi'.")

if __name__ == "__main__":
    calculate_distance()
