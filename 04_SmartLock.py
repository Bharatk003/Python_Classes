"""
@Author : Bharat Kshirsagar
@Date : 27/12/2023
@Goat : to implement the class Lock

@product name : Godrej Digital Lock I Catus Touch Pro
@link : https://www.amazon.in/dp/B0CM98998Z/ref=sspa_dk_detail_6?pd_rd_i=B0CM98998Z&pd_rd_w=0Mukx&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_p=dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_r=ZH2W6EEMBPDN9D91VC9H&pd_rd_wg=o4sbp&pd_rd_r=f38061d0-427d-4c75-948e-6f42e67bf45c&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1


"""
class Dimension:

    """
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
                 length: float,
                 breadth: float,
                 height: float,
                 weight: float
                 )->None:
        """
        constructor
        """
        #type cheaking and value cheaking
        if type(length) != float:
            raise TypeError("bad type: it should be float")
        
        if type(breadth) != float:
            raise TypeError("bad type: it should be float")
        
        if type(height) != float:
            raise TypeError("bad type: it should be float")
        
        if type(weight) != float:
            raise TypeError("bad type: it should be float")
        
        self.length = length
        self.breadth = breadth
        self.height = height
        self.weight = weight

    def getDimensionlength(self):
        """
        It returns the Length of the product
        """
        return self.length

    def getDimensionbreadth(self):
        """
        It return the breadth of the product
        """
        return self.breadth

    def getDimensionheight(self):
        """
        It return the height of the product
        """
        return self.height
    
    def getDiemnsionweight(self):
        """
        it return the weight of the product
        """
        return self.weight
    



class Lock:
    """
    class represent the smart lock for doors in modern society

    @raises : 
    - TypeError : if any variable has invalid type

    @methods
    - show method : print all properties of the lock object

    """
    def __init__(self,
                Brand: str,
                Special_Feature: str,
                Lock_Type: str,
                Item_Dimensions: Dimension,  
                Material: str,	
                Colour: str,	
                Item_Weight: str,	 
                Control_Method: str,	
                Manufacturer: str,	    
                Item_part_number: str,	  
                Batteries_Included: bool,	
                Batteries_Required : bool,
                Battery_cell_composition: str,	
                Country_of_Origin: str,	
                Price: int 
                 )->None:
        # type and value checks :
        """
        construtor of  class smart lock
        """
        if type(Brand) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Special_Feature) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Lock_Type) != str:
            raise TypeError("bad Type: it should be str")

        if type(Item_Dimensions) != Dimension:
            raise TypeError("bad Type: it should be str")
        
        if type(Material) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Colour) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Item_Weight) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Control_Method) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Manufacturer) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Item_part_number) != str:
            raise TypeError("bad Type: it should be str")

        if type(Batteries_Included) != bool:
            raise TypeError("bad Type: it should be bool")
        
        if type(Batteries_Required) != bool:
            raise TypeError("bad Type: it should be bool")
        
        if type(Battery_cell_composition) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Country_of_Origin) != str:
            raise TypeError("bad Type: it should be str")
        
        if type(Price) != float:
            raise TypeError("bad Type: it should be float")

        self.Brand = Brand
        self.Special_Feature = Special_Feature
        self.Lock_Type = Lock_Type
        self.Item_Dimensions = Item_Dimensions  
        self.Material = Material	
        self.Colour = Colour	
        self.Item_Weight = Item_Weight	 
        self.Control_Method = Control_Method	
        self.Manufacturer = Manufacturer	    	 
        self.Item_part_number = Item_part_number	  
        self.Batteries_Included = Batteries_Included	
        self.Batteries_Required  = Batteries_Required 
        self.Battery_cell_composition = Battery_cell_composition	
        self.Country_of_Origin = Country_of_Origin	
        self.price = Price


def showOBJ(self):
    """
    printing the properties of smartLock

    """
    print("Brand:" , self.Brand)

    print("Special_Feature:" , self.Special_Feature)

    print("Lock_Type:" , self.Lock_Type)

    print("Item_Dimensions:",self.Item_Dimensions.getDimensionlength(), "x",
                            self.Item_Dimensions.getDimensionbreadth(), "x",
                            self.Item_Dimensions.getDimensionheight(), ":",
                            self.Item_Dimensions.getDiemnsionweight() )

    print("Material:" , self.Material)

    print("Colour:" , self.Colour)

    print("Item_Weight:" , self.Item_Weight)

    print("Control_Method:" , self.Control_Method)

    print("Manufacturer:" , self.Manufacturer)

    print("Item_part_number:" , self.Item_part_number)

    print("Batteries_Included:" , self.Batteries_Included)

    print("Batteries_Required:" , self.Batteries_Required)

    print("Battery_cell_composition:" , self.Battery_cell_composition)

    print("Country_of_Origin:" , self.Country_of_Origin)

    print("price:" , self.price)



def main()->None:
    """
    main function of the program

    """
    Godrej_Digital_Lock_I_Catus_Touch_Pro = Lock(
                                                "Godrej",
                                                "Scratch_Resistant",
                                                "Mortise_Lock",
                                                Dimension(27.00,22.5,12.10,1.5),
                                                "steel",
                                                "Black",
                                                "1.5 kilograms",
                                                "Touch",
                                                "Godrej adn Boyce mfg.co.Ltd",
                                                "3",
                                                True,
                                                True,
                                                "Alkaline",
                                                "China",
                                                123.42
                                                )
    
    showOBJ(Godrej_Digital_Lock_I_Catus_Touch_Pro)


main()