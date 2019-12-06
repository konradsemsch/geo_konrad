
from geopy.geocoders import Nominatim

class Locate:
    # I'm keeping this class for the time being. Perhaps for some further examples
    """
    A generic geo-localization class.
    """

    def __init__(self, latitude, longtitude):
        self.latitude = latitude
        self.longtitude = longtitude

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

    if isinstance(latitude, float) == False or isinstance(longtitude, float) == False:
        print('Both coordinates need to be float numbers. For example: 50.0')

    if latitude in range(-90, 90):
        print('Latitude range not allowed')

    if longtitude in range(-180, 180):
        print('Longtitude range not allowed')

    else:
        # Proceed if coordinates are legit
        geolocator = Nominatim(user_agent = "my_app")
        coordinates = (latitude, longtitude)
        
        # Find the location
        location = geolocator.reverse(coordinates,  addressdetails = False)

        print('Location details were found: ', location)
        return location