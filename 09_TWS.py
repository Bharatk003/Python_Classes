"""
@Author : Bharat Kshirsagar
@Date : 03/01/2023
@Goal : implement the class TWS earphone

@link : https://www.amazon.in/OnePlus-Wireless-Earbuds-Drivers-Playback/dp/B0C8JB3G5W/ref=sr_1_2?_encoding=UTF8&content-id=amzn1.sym.b40a0c50-2220-4a6c-880a-12af507a8ec0&pd_rd_r=566a96a4-5615-416d-9e26-eb99d2130840&pd_rd_w=NLfSM&pd_rd_wg=QacGj&pf_rd_p=b40a0c50-2220-4a6c-880a-12af507a8ec0&pf_rd_r=3VM27ZFHARNFC6ZK88HB&qid=1704263770&refinements=p_n_condition-type%3A8609960031%2Cp_72%3A1318476031&s=electronics&sr=1-2&th=1

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
    

    def getDimension(self)->None:

        """
        it print out the Dimension of the product
        """
        dim = "{} x {} x {} : {}".format(self.length, self.breadth, self.height, self.weight)
        return dim

class Time: 
    """
    It implement the time in form of 
    day/hr/min/sec
    """
    def __init__(self,
                day : int,
                hrs : int,
                min : int, 
                sec : int,
                )->None:
        """
        constructor for class time
        """
        

        if type(day) != int:
            raise TypeError("bad type it should be int")

        if type(hrs) != int:
            raise TypeError("bad type it should be int")
    
        if type(min) != int:
            raise TypeError("bad type it should be int")
        
        if type(sec) != int:
            raise TypeError("bad type it should be int")
        
        # value check

        if hrs < 0 or hrs > 24: 
            raise ValueError("value of hrs should be in between 0 to 24")

        if min < 0 or min > 60:
            raise ValueError("value of min should be in between 0 to 60")

        if sec < 0 or sec > 60:
            raise ValueError("value of hrs should be in between 0 to 60:")

        self.day = day
        self.hrs = hrs
        self.min = min
        self.sec = sec

    def getTime(self)->None:
        """
        getter method for time class
        """
        Time = "{} day : {} hrs : {} min : {} sec".format(self.day,self.hrs,self.min, self.sec)
        
        return Time
        


class TWS: 
    """
 
    represent the class TWS

    raise : 
    - type error: if any attribute has invalid type
    - value error: if any attribute missing it value range

    method():
    - show(): it prints all the properties of class Battery

    """
    def __init__(self,
                Manufacturer: str,
                Model: str,
                Model_Name: str,
                Product_dimension: Dimension,
                Item_model_number: str,
                Hardware_platform: str,
                Compatible_Devices: list,
                Special_features: tuple,
                Mounting_Hardware: tuple,
                Num_of_items: int,
                Microphone_formate: str,
                Headphones_form_factor: str,
                Battery_Average_Life : Time,
                Charging_Time	 : Time,
                Batteries_Required : bool,
                Cable_feature	: str,
                Connector_Type	: str,
                Material	 : str,
                Maximum_Operating_Distance : int,  
                Form_Factor : str,
                Includes_Rechargeable_Battery : bool,
                Country_of_Origin	 : str,
                Item_Weight	 : float
                ) -> None:
        """
        constructor for the class TWS
        """
        if type(Manufacturer) != str:
            raise TypeError("bad type it should be str")
        
        if type(Model) != str:
            raise TypeError("bad type it should be str")
        
        if type(Model_Name) != str:
            raise TypeError("bad type it should be str")
            
        if type(Product_dimension) != Dimension:
            raise TypeError("bad type it should be Dime")

        if type(Item_model_number) != str:
            raise TypeError("bad type it should be str")    

        if type(Hardware_platform) != str:
            raise TypeError("bad type it should be str")

        if type(Compatible_Devices) != list:
            raise TypeError("bad type it should be list")

        if type(Special_features) != tuple:
            raise TypeError("bad type it should be tuple")    

        if type(Mounting_Hardware) != tuple:
            raise TypeError("bad type it should be tuple")
        
        if type(Num_of_items) != int:
            raise TypeError("bad type it should be int")
        
        if type(Microphone_formate) != str:
            raise TypeError("bad type it should be str")
        
        if type(Headphones_form_factor) != str:
            raise TypeError("bad type it should be str")
        
        if type(Battery_Average_Life) != Time:
            raise TypeError("bad type it should be time")
        
        if type(Charging_Time) != Time:
            raise TypeError("bad type it should be time")
        
        if type(Batteries_Required) != bool:
            raise TypeError("bad type it should be boll")

        if type(Cable_feature) != str:
            raise TypeError("bad type it should be str")
        
        if type(Connector_Type) != str: 
            raise TypeError("bad type it should be str")

        if type(Material) != str: 
            raise TypeError("bad type it should be str")
        
        if type(Maximum_Operating_Distance) != int: 
            raise TypeError("bad type it should be int")
        
        if type(Form_Factor) != str: 
            raise TypeError("bad type it should be str")
        
        if type(Includes_Rechargeable_Battery) != bool: 
            raise TypeError("bad type it should be bool")
        
        if type(Country_of_Origin) != str: 
            raise TypeError("bad type it should be str")

        if type(Item_Weight) != float: 
            raise TypeError("bad type it should be float")
        



        self.Manufacturer = Manufacturer

        self.Model = Model

        self.Model_Name = Model_Name

        self.Product_dimension = Product_dimension

        self.Item_model_number = Item_model_number

        self.Hardware_platform = Hardware_platform

        self.Compatible_Devices = Compatible_Devices

        self.Special_features = Special_features

        self.Mounting_Hardware = Mounting_Hardware

        self.Num_of_items = Num_of_items

        self.Microphone_formate = Microphone_formate

        self.Headphones_form_factor = Headphones_form_factor

        self.Battery_Average_Life = Battery_Average_Life

        self.Charging_Time = Charging_Time

        self.Batteries_Required = Batteries_Required

        self.Cable_feature = Cable_feature

        self.Connector_Type = Connector_Type

        self.Material = Material

        self.Maximum_Operating_Distance = Maximum_Operating_Distance

        self.Form_Factor = Form_Factor

        self.Includes_Rechargeable_Battery = Includes_Rechargeable_Battery

        self.Country_of_Origin = Country_of_Origin

        self.Item_Weight = Item_Weight



    def show(self)->None:
        """
        These function is used to print the properties of TWS

        """
        print(" Manufacturer: ",   self.Manufacturer)

        print(" Model: ",   self.Model)

        print(" Model_Name: ",   self.Model_Name)

        print(" Product_dimension: ",   self.Product_dimension.getDimension())

        print(" Item_model_number: ",   self.Item_model_number)

        print(" Hardware_platform: ",   self.Hardware_platform)

        print(" Compatible_Devices: ",   self.Compatible_Devices)

        print(" Special_features: ",   self.Special_features)

        print(" Mounting_Hardware: ",   self.Mounting_Hardware)

        print(" Num_of_items: ",   self.Num_of_items)

        print(" Microphone_formate: ",   self.Microphone_formate)

        print(" Headphones_form_factor: ",   self.Headphones_form_factor)

        print(" Battery_Average_Life: ",   self.Battery_Average_Life.getTime())

        print(" Charging_Time: ",   self.Charging_Time.getTime())

        print(" Batteries_Required: ",   self.Batteries_Required)

        print(" Cable_feature: ",   self.Cable_feature)

        print(" Connector_Type: ",   self.Connector_Type)

        print(" Material: ",   self.Material)

        print(" Maximum_Operating_Distance: ",   self.Maximum_Operating_Distance)

        print(" Form_Factor: ",   self.Form_Factor)

        print(" Includes_Rechargeable_Battery: ",   self.Includes_Rechargeable_Battery)

        print(" Country_of_Origin: ",   self.Country_of_Origin)

        print(" Item_Weight: ",   self.Item_Weight)



def main()->None:
    """
    This is the main function
    """
    OnePlusTWS = TWS(
                    "OnePlus",
                    "E510A",
                    "NORD",
                    Dimension(2.9,2.0,2.3,38),
                    "34eed",
                    "SmartPhone",
                    ["laptop", "mobile", "smartTV","Tables", "all bluetooth devices"],
                    ("Oneplus Fast Pair", "Dolby Atmos Support", "Dirac Toner", "Sound Master Equalizer",
                    "Compatibility With Hey Melody App", "With Built In Microphone", "IP55 Water Resistant",
                    "Up to 38 Hrs of Playtime", "Bluetooth"),
                    ("1 x Earbuds", "1 x Charging Case", "1 x Extra Ear Tips", "1 x Charging Cable", "1 x User Manual", "1 x Warranty Card"),
                    1,
                    "Buidin",
                    'tws',
                    Time(0,8,0,0),
                    Time(0,0,38,0),
                    True,
                    "without cable",
                    "Wireless",
                    "Plastic",
                    10,
                    "True wireless",
                    True,
                    "Bharat",
                    38.83
                    )
    
    OnePlusTWS.show()
    exit(0)

main()