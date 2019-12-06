
from geopy.geocoders import Nominatim

class Locate:
    """
    A generic geo-localization class.
    """

    def __init__(self, latitude, longtitude):
        self.latitude = latitude
        self.longtitude = longtitude

    def locate_coordinates(self, latitude, longtitude):
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

        if (self.latitude or self.longtitude) is None:
            print('Neither of parameters can be empty')

        if self.latitude.isdigit() == False or self.longtitude.isdigit() == False:
            print('Both coordinates need to be numbers')

        if self.latitude in range(-90, 90):
            print('Latitude range not allowed')

        if self.longtitude in range(-180, 180):
            print('Longtitude range not allowed')

        else:
            # Proceed if coordinates are legit
            geolocator = Nominatim(user_agent = "my_app")
            coordinates = (self.latitude, self.longtitude)
            location = geolocator.reverse(coordinates,  addressdetails = False)

            print('Location details were found: ', location)
            return location