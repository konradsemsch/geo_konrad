import pandas as pd
from geopy.geocoders import Nominatim

def locate_coordinates(latitude, longtitude):
    """
    This function returns the country found under the specified geo-coordinates.
    Please provide inputs in DDS (Decimal Degree System). 

    Example:
        locate_coordinates(52.375, 13.667)
        locate_coordinates(52.375, -13.667)

    Args:
        latitude (float): The latitude of the location.
        longtitude (float): The longtitude of the location.

    Returns:
        string: Country of the following geo-coordinates.
    """

    if (latitude or longtitude) is None:
        print('Neither of parameters can be empty')

    # if latitude < 0 or latitude > 90:
    if latitude in range(-90, 90):
        print('Latitude range not allowed')

    # if longtitude < 0 or longtitude > 180:
    if longtitude in range(-180, 180):
        print('Longtitude range not allowed')

    else:
        # Proceed if coordinates are legit
        geolocator = Nominatim(user_agent = "my_app")
        coordinates = (latitude, longtitude)
        location = geolocator.reverse(coordinates,  addressdetails = False)

        # print(pd.isnull(location))
        print('Location details were found: ', location)
        return location

### Quick testing
# locate_coordinates(52.375, 13.667)
