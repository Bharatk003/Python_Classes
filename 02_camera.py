
"""
@Author : Bharat Kshirsagar
@Date   : 23/12/2023
@Goal   : implement class camera

@link   : https://www.amazon.in/gp/product/B0BCW1S7XR/ref=s9_bw_cg_hpcg1_2a1_w?pf_rd_m=AT95IG9ONZD7S&pf_rd_s=merchandised-search-8&pf_rd_r=DGR45RH7PPZEKM3GYGFD&pf_rd_t=101&pf_rd_p=51dc881b-8213-49aa-9353-1522bbff412f&pf_rd_i=1388977031&th=1

"""

import sys
# from tabnanny import check

# # server site
# Date(23,12,2023),
# Product_Dimenstion(11.4,2.3,4.6),
def is_date_valid(day: int, month: int, year:int)->bool:
    """
    Check if the given combination of day, month, and year forms a valid date in the Gregorian Calendar.

    Args:
        day (int): Day value.
        month (int): Month value.
        year (int): Year value.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    is_leap = (year % 4 ==0 ) and (year % 400 == 0 or year % 100 != 0)
    return (
        (is_leap == True and month == 2 and day in range(1,30)) or
        (is_leap == False and month == 2 and day in (1,29)) or 
        (month in (1,23,5,7,8,10,12) and day in (1,32))
            
    )


class Date:
    """
    This class implements an entity 'Date' as per 
    Gregorian Calender
    @__init__Constructor.

    """
    def __init__(self, init_day: int, init_month: int, init_year: int):
        """
        constructor or data class.
        @self:
        init_day:
        init_month:
        init_year:clinet specific value for attribute year

        """
        if type(init_day) != int:
            raise TypeError("day must be an integer")
        
        if type(init_month) != int:
            raise TypeError("mont must be an integer")
        
        if type(init_year) != int:
            raise TypeError("year must be an integer")
        
        self.day = init_day
        self.month = init_month
        self.year = init_year

    def get_date(self)->None:
        """
        It print the data in form formate:
        DD/MM/YYYY

        """
        print(self.day, "/", self.month,"/", self.year)

class Resolution:
    """
    This class implements the resolution type where 
    @length and @ width is the parameter

    """

    def __init__(self, length: float, width: float)->None:
        """
        Initialize a Resolution object.

        Args:
            length (float): Length of the display.
            width (float): Width of the display.
        """
        # type check
        if type(length) != float:
            raise TypeError("bad type: it should be float")
        
        if type(width) != float:
            raise TypeError("bad type: it should be float")
        
        self.length = length
        self.width = width

    def get_resolution(self)->None:

        """
        It prints the resolution of display in the from
        pixel x pixel

        @ex. 1920x1080P
        
        """
        print(self.length, "x", self.width,end="P \n") 

class Product_Dimension:
 
    """
        Initialize a Product_Dimension object.

        Args:
            length (int | float): Length of the product.
            breadth (int | float): Breadth of the product.
            height (int | float): Height of the product.
            weight (int | float): Weight of the product.
    """
    
    def __init__(self, length:(int|float),
                    breadth:(int|float),
                    height:(int|float),
                    weight: (int|float)):
        
        # type checking
        if type(length) != int and type(length) != float:
            raise TypeError("len should be in float or int")
        
        if type(breadth) != int and type(breadth) != float:
            raise TypeError("breadth should be in float or int")
        
        if type(height) != int and type(height) != float:
            raise TypeError("height must be in float or int")
        
        if type(weight) != int and type(weight) != float:
            raise TypeError("weigh must be in float or int")
        
        #value checks
        if length <= 0 or breadth <= 0 or height <= 0 or weight <=0:
            raise ValueError("Dimensions should not be negative")

        self.length = length
        self.breadh = breadth
        self.height = height
        self.weight = weight


    def get_Product_Dimension(self)->None:
        """
        this function print the dimension of the product in the 
        lengtu x breadth x height x weight
        """
        print(self.length, "x", self.breadh, "x", self.height, "x", self.weight)

class camera:
    """
        Represents a camera with various properties.
    """
    def __init__(self, 
                Product_information: str,
                Technical_Details: str, 
                Brand: str,
                Manufacturer: str,
                Model: str,
                Model_year: Date,
                product_diamensions: Product_Dimension,
                Batteries : str,
                item_model_number: str,
                resolution : Resolution,
                Compatible_devices: str,
                Special_Feature: str,
                Num_of_items: int,
                Display_technology: str,
                Has_img_Stabilization: bool,
                min_focal_len: float,
                Batteries_included: bool,
                wireless_type: str,
                Material: str,
                Media_type: str,
                country_of_Origin: str,
                weight: float
                )->None:

        #type and value checks

        if type(Product_information) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Technical_Details) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Brand) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Manufacturer) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Model) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Model_year) != Date:
            raise TypeError("Bad Type: it should be Date")

        if type(product_diamensions) != Product_Dimension:
            raise TypeError("Bad Type: it should be str")
        
        if type(resolution) != Resolution:
            raise TypeError("Bad Type: it should be str")
        
        if type(Model_year) != Date:
            raise TypeError("Bad Type: it should be str")
        
        if type(Batteries) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(item_model_number) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Compatible_devices) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Special_Feature) != str:
            raise TypeError("Bad Type: it should be str")

        if type(Num_of_items) != int:
            raise TypeError("Bad Type: it should be str")
        
        if type(Display_technology) != str:
            raise TypeError("Bad Type: it should be str")
        
        if type(Has_img_Stabilization) != bool:
            raise TypeError("Bad Type: it should be bool")
        
        if type(min_focal_len) != float:
            raise TypeError("Bad Type: it should be flaot")
        
        if type(Batteries_included) != bool:
            raise TypeError("Bad Type: it should be str")
        
        if type(wireless_type) != str:
            raise TypeError("Bad type: it should be str")

        if type(Material) != str:
            raise TypeError("Bad type: it should be str")
        
        if type(Media_type) != str:
            raise TypeError("Bad type: i`t should be str")
        
        if type(country_of_Origin) != str:
            raise TypeError("Bad type: it should be str")
        
        if type(weight) != float:
            raise TypeError("Bad type: it should be str")
        

        self.Product_information = Product_information
        self.Technical_Details = Technical_Details
        self.Brand = Brand
        self.Manufacturer = Manufacturer
        self.Model = Model
        self.Model_year = Model_year
        self.product_diamensions = product_diamensions
        self.Batteries  = Batteries
        self.item_model_number = item_model_number
        self.resolution  = resolution
        self.Compatible_devices = Compatible_devices
        self.Special_Feature = Special_Feature
        self.Num_of_items = Num_of_items
        self.Display_technology = Display_technology
        self.Has_img_Stabilization = Has_img_Stabilization
        self.min_focal_len = min_focal_len
        self.Batteries_included = Batteries_included
        self.wireless_type = wireless_type
        self.Material = Material
        self.Media_type = Media_type
        self.country_of_Origin = country_of_Origin
        self.weight = weight


    def show(self)->None:
        """
        shows/print all the properties of the class camera
        
        """
        print("Product_information: ",self.Product_information) 

        print("Technical_Details: ",self.Technical_Details)  

        print("Brand: ",self.Brand) 

        print("Manufacturer: ",self.Manufacturer) 

        print("Model: ",self.Model) 

        print("Model_year: ")
        
        self.Model_year.get_date()

        print("product_diamensions: "),
        
        self.product_diamensions.get_Product_Dimension()

        print("Batteries: ",self.Batteries) 

        print("item_model_number: ",self.item_model_number) 

        print("resolution: ")

        self.resolution.get_resolution()  

        print("Compatible_devices: ",self.Compatible_devices) 

        print("Special_Feature: ",self.Special_Feature) 

        print("Num_of_items",self.Num_of_items)

        print("Display_technology",self.Display_technology)

        print("Has_img_Stabilization",self.Has_img_Stabilization)

        print("min_focal_len: ",self.min_focal_len) 

        print("Batteries_included: ",self.Batteries_included)

        print("wireless_type: ",self.wireless_type) 

        print("Material: ",self.Material) 

        print("Media_type",self.Media_type)

        print("country_of_Origin: ",self.country_of_Origin) 

        print("weight: ",self.weight)       







# client site
def main()->None:
    """
    main function to demonstrate the Camera class.

    """
        
    insta360_X3_Action_Camera = camera(
                                        "it is 360 degree camera made for tourism perpose",
                                        "it has 8k bluetooth features",
                                        "insta360",
                                        "Shenzhen Arashi Vision Company Limited Floor 6, Block A Logan Century Center, Shenzhen China 518000",
                                        "INSTA360",
                                        Date(23,12,2023),
                                        Product_Dimension(11.4,2.3,4.6,180.21),
                                        "1 Lithium Polymer batteries required",
                                        "b",
                                        Resolution(1080.00, 1980.00),
                                        "SmartPhone",
                                        "360 degree",
                                        1,
                                        "LED",
                                        False,
                                        32.34,
                                        True,
                                        "bluetooth",
                                        "plastic/rubber",
                                        "Micro SD",
                                        "Bharat",
                                        180.32

                                        )

    insta360_X3_Action_Camera.show()
    sys.exit(0)

main()
