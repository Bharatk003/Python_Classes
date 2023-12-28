"""
@Author : Bharat Kshirsagar
@Date : 26-12-2023
@Goal : implement class SmartPhone

@Link : https://www.amazon.in/Samsung-Galaxy-Ultra-Cream-Storage/dp/B0BTYSZ429/ref=sr_1_3?keywords=samsung+s24&qid=1703741664&s=electronics&sr=1-3

"""
class Dimension:
    """"
    A class representing the dimensions and weight of a product.

    Attributes:
    - length (float): The length of the product.
    - breadth (float): The breadth or width of the product.
    - height (float): The height of the product.
    - weight (float): The weight of the product.

    Raises:
    - TypeError: If any dimension or weight is not a float.
    - ValueError: If any dimension or weight is non-positive.
    """
    def __init__(self,
                 length: int|float,
                 breadth:int|float,
                 height: int|float,
                 weight: int|float,
                 )->None:
        # type and value checks     
        """
        constructor
        """
        if type(length) != int  and type(length) != float:
            raise TypeError("bad type: it should be float or int")
        
        if type(breadth) != int  and type(breadth) != float:
            raise TypeError("bad type: it should be float or int")
        
        if type(height) != int and type(height) != float:
            raise TypeError("bad type: it should be float or int")
        
        if type(weight) != int  and type(weight) != float:
            raise TypeError("bad type: it should be float or int")
        
        if length <= 0 and breadth <= 0 and height <= 0 and weight <= 0:
            raise ValueError("One or more argument contain invalid value")
        
        self.length = length
        self.breadth = breadth
        self.height = height
        self.weight = weight

    def getlength(self)->float|int:
        return self.length

    def getbreadth(self)->float|int:
        return self.breadth
    
    def getheight(self)->float|int:
        return self.height
    
    def getweight(self)->float|int:
        return self.weight
    


    


class Rating:
    """
    This class is implemented for submitting rating of any product

    """
    def __init__(self,rate: float)->None:
        """
        constructor for rating class
        """
        # type and value checks
        if type(rate) != float and type(rate) != float:
            raise TypeError("Bad type : it should be int or float")

        if rate > 10 or rate < 0:
            raise ValueError("The rating should be on 1 to 10 scale")


        self.rate = rate

    
    def setRating(self,numeric)->None:
        """
        This function set the rating in numeric form
        """
        if type(numeric) != float and type(numeric) != float:
            raise TypeError("Bad type : it should be int or float")

        if numeric > 10 or numeric < 0:
            raise ValueError("The rating should be on 1 to 10 scale")
        
        self.rate = numeric

    def getRating(self)->float|int:
        return self.rate
    

class SmartPhone:
    """
    A class represent SmartPhones

    Raises:
    - TypeError: If any attribute has an invalid type.

    Methods:
    - show(): Prints all the properties of the watch object.
    
    """
    def __init__(self,
                os: str,
                Product_dimension: Dimension,   
                Batteries: str,	 
                Item_model_number: int,
                Wireless_communication_technologies: tuple, 
                Connectivity_technologies: tuple,	 
                GPS: str,	 
                Special_features: list,	 
                Other_display_features: list, 
                Device_interface_primary: str,	 
                Other_camera_features: str, 
                Audio_Jack: str,	 
                Form_factor: str,	 
                Colour_set_available: set,	 
                Battery_Power_Rating: Rating,	 
                Whats_in_the_box: str,	 
                Manufacturer: str,	 
                Country_of_Origin: str,	 
                Item_Weight: float|int,
                Price: float
                )->None:
        
        if type(os) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Product_dimension) != Dimension: 
            raise TypeError("bad type: it should be Dimesion")

        if type(Batteries) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Item_model_number) != int : 
            raise TypeError("bad type: it should be int")
        
        if type(Wireless_communication_technologies) != tuple: 
            raise TypeError("bad type: it should be str")
        
        if type(Connectivity_technologies) != tuple: 
            raise TypeError("bad type: it should be str")
        
        if type(GPS) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Special_features) != list: 
            raise TypeError("bad type: it should be str")
        
        if type(Other_display_features) != list: 
            raise TypeError("bad type: it should be str")
        
        if type(Device_interface_primary) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Other_camera_features) != str: 
            raise TypeError("bad type: it should be str")

        if type(Audio_Jack) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Form_factor) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Colour_set_available) != set: 
            raise TypeError("bad type: it should be str")
        
        if type(Battery_Power_Rating) != Rating: 
            raise TypeError("bad type: it should be str")

        if type(Whats_in_the_box) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Manufacturer) != str: 
            raise TypeError("bad type: it should be str")
        
        if type(Country_of_Origin) != str: 
            raise TypeError("bad type: it should be str")   
        
        if type(Item_Weight) != int and type(Item_Weight) != float: 
            raise TypeError("bad type: it should be float or int") 
        
        if type(Price) != float: 
            raise TypeError("bad type: it should be str") 


        self.os = os
        self.Product_dimension = Product_dimension   
        self.Batteries = Batteries	 
        self.Item_model_number = Item_model_number
        self.Wireless_communication_technologies = Wireless_communication_technologies 
        self.Connectivity_technologies = Connectivity_technologies	 
        self.GPS = GPS	 
        self.Special_features = Special_features	 
        self.Other_display_features = Other_display_features 
        self.Device_interface_primary = Device_interface_primary	 
        self.Other_camera_features = Other_camera_features 
        self.Audio_Jack = Audio_Jack	 
        self.Form_factor = Form_factor	 
        self.Colour_set_available = Colour_set_available	 
        self.Battery_Power_Rating = Battery_Power_Rating	 
        self.Whats_in_the_box = Whats_in_the_box	 
        self.Manufacturer = Manufacturer	 
        self.Country_of_Origin = Country_of_Origin	 
        self.Item_Weight = Item_Weight 
        self.Price = Price


    def show(self)->None:
        """
        This function show all the field in Smartphone class

        """
        print("os:  ", self.os)

        print("Product_dimension:  ", self.Product_dimension.getlength(), "x", self.Product_dimension.getbreadth(),"x", 
                                    self.Product_dimension.getweight(), ":", self.Product_dimension.getweight())

        print("Batteries:  ", self.Batteries)

        print("Item_model_number:  ", self.Item_model_number)

        print("Wireless_communication_technologies:  ", self.Wireless_communication_technologies)

        print("Connectivity_technologies:  ", self.Connectivity_technologies)

        print("GPS:  ", self.GPS)

        print("Special_features:  ", self.Special_features)

        print("Other_display_features:  ", self.Other_display_features)

        print("Device_interface_primary:  ", self.Device_interface_primary)

        print("Other_camera_features:  ", self.Other_camera_features)

        print("Audio_Jack:  ", self.Audio_Jack)

        print("Form_factor:  ", self.Form_factor)

        print("Colour_set_available:  ", self.Colour_set_available)

        print("Battery_Power_Rating:  ", self.Battery_Power_Rating)

        print("Whats_in_the_box:  ", self.Whats_in_the_box)

        print("Manufacturer:  ", self.Manufacturer)

        print("Country_of_Origin:  ", self.Country_of_Origin)

        print("Item_Weight:  ", self.Item_Weight)

        print("Price:  ", self.Price)




def main()->None:

    """
    main function of the program
    """

    Samsung_Galaxy_S23 = SmartPhone(
                                    "Android 13.0",
                                    Dimension(50,50,28,300),
                                    "1 Lithium Ion batteries required",
                                    14342354,
                                    ("Cellular", "WAN", "LAN"),
                                    ("bluetooth", "wi-fi", "USB"),
                                    "LONASS",
                                    ["fast charging support", "Dual SIM", "fingerprint sensor", "Wireless Charging"],
                                    [],
                                    "TouchScreen",
                                    "rear, front",
                                    "USB type-C",
                                    "bar",
                                    {"cream", "grey", "black", "white"},
                                    Rating(8.3),
                                    "type_c cable, charger, earphone , silicon case, user manual",
                                    "Samsung",
                                    "india",
                                    300,
                                    8999.23
                                    )    

    Samsung_Galaxy_S23.show()

main()

 