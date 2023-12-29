"""
@Author: Bharat Kshiragar
@Date : 29/12/2024
@Goal : To implement class Battery

@link : https://www.amazon.in/ZyneCellTM-Lithium-Battery-Agricultural-Sprayer/dp/B0BYJMFYXC

 
Number of Batteries	1 Lithium Ion batteries required. (included)
Brand	ZYNECELL
Battery Cell Composition	Lithium Ion
Compatible Phone Models	Toy car
Recommended Uses For Product	agriculture spray pump, power tools,etc
Net Quantity	1.00 count
Voltage	11.11 Volts (DC)
Reusability	Rechargeable
Battery Weight	650 Grams
Item Dimensions LxWxH	15 x 6.5 x 10.8 Centimeters

 
"""
from DimensionUDD import Dimension

class Battery:
    """
    class represent the battery

    raise : 
    - type error: if any attribute has invalid type
    - value error: if any attribute missing it value range

    method():
    - show(): it prints all the properties of class Battery

    """

    def __init__(self,
                Number_of_Batteries: int,	 
                Brand : str,
                Battery_Cell_Composition : tuple,	 
                Compatible  : str,
                Recommended_Uses_For_Product : list ,
                Net_Quantity : int,
                Voltage	 : float,
                Reusability	: str,
                Battery_Weight : float,	 
                Item_Dimensions : Dimension,
                )->None:
        """
        constructor of class Battery
        """

        # type checks 

        if type(Number_of_Batteries) != int:
            raise TypeError("bad type: it should be int")

        if type(Brand) != str:
            raise TypeError("bad type: it should be str")
        
        if type(Battery_Cell_Composition) != tuple:
            raise TypeError("bad type: it should be tuple")

        if type(Compatible) != str:
            raise TypeError("bad type: it should be str")
        
        if type(Recommended_Uses_For_Product) != list:
            raise TypeError("bad type: it should be List")
        
        if type(Net_Quantity) != int:
            raise TypeError("bad type: it should be int")
        

        if type(Voltage) != float:
            raise TypeError("bad type: it should be float")
        
        if type(Reusability) != str:
            raise TypeError("bad type: it should be str")

        if type(Battery_Weight) != float:
            raise TypeError("bad type: it should be str")
        
        if type(Item_Dimensions) != Dimension:
            raise TypeError("bad type: it should be Dimesion")
         
        self.Number_of_Batteries = Number_of_Batteries	 
        self.Brand = Brand 
        self.Battery_Cell_Composition = Battery_Cell_Composition 	 
        self.Compatible = Compatible  
        self.Recommended_Uses_For_Product = Recommended_Uses_For_Product 
        self.Net_Quantity = Net_Quantity 
        self.Voltage = Voltage	 
        self.Reusability = Reusability	
        self.Battery_Weight = Battery_Weight 	 
        self.Item_Dimensions = Item_Dimensions


def show(self)->None:

    """
    These function represent the value of the properties of class
    in other word it print object of class
    """

    print("Number_of_Batteries: ",self.Number_of_Batteries)

    print("Brand: ",self.Brand)

    print("Battery_Cell_Composition: ",self.Battery_Cell_Composition)

    print("Compatible: ",self.Compatible)

    print("Recommended_Uses_For_Product: ",self.Recommended_Uses_For_Product)

    print("Net_Quantity: ",self.Net_Quantity)

    print("Voltage: ",self.Voltage)

    print("Reusability: ",self.Reusability)

    print("Battery_Weight: ",self.Battery_Weight)

    print("Item_Dimensions: ", end=""),self.Item_Dimensions.getDimension()


def main()->None:

    """
    implement main function
    """
    ZyneCell_12V_8Ah_Lithium_Ion_Battery  = Battery(
                                                    100,
                                                    "ZYNECELL",
                                                    ("Lithium Ion",),
                                                    "Cars",
                                                    ["agri say pump" ,"power tools", "etc"],
                                                    1,
                                                    11.11,
                                                    "Rechargeable",
                                                    650.03,
                                                    Dimension(15.00,6.5,10.8,650.34)
                                                    
                                                    )
    # print(ZyneCell_12V_8Ah_Lithium_Ion_Battery.Numbero)
    show(ZyneCell_12V_8Ah_Lithium_Ion_Battery)
main()
