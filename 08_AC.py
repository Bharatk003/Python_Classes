"""
@Author : Bharat Kshirsagar
@Date : 1/1/2024
@goal : implement class of Air conditioner

@link : https://www.amazon.in/SUPREMECOOL-1-5T-INV-EXP-S3i3ADO/dp/B0BWMX89HR/ref=sr_1_1?keywords=ac&qid=1704083992&s=kitchen&sr=1-1

"""

from DimensionUDD import Dimension
import sys
class AC:
    """
    class represent the battery

    raise : 
    - type error: if any attribute has invalid type
    - value error: if any attribute missing it value range

    method():
    - show(): it prints all the properties of class Battery

    """
    def __init__(self,
                Brand: str,
                Capacity: float,
                Special_Feature: str,
                Product_dimension: Dimension,
                Energy_star: int,
                Features: list[str],
                temp_range: range,
                price: float,
                )->None:
        """
        constructor
        """
        
        if type(Brand) != str:
            raise TypeError("bad type: it should be str ")
        
        if type(Capacity) != float:
            raise TypeError("bad type: it should be float ")

        if type(Special_Feature) != str:
            raise TypeError("bad type: it should be str ")
        
        if type(Product_dimension) != Dimension:
            raise TypeError("bad type: it should be str ")
        
        if type(Energy_star) != int:
            raise TypeError("bad type: it should be str ")
        
        if type(Features) != list:
            raise TypeError("bad type: it should be str ")
        
        if type(temp_range) != range:
            raise TypeError("bad type: it should be str ")
        
        if type(price) != float:
            raise TypeError("bad type: it should be str ")
        
        self.Brand = Brand
        self.Capacity = Capacity
        self.Special_Feature = Special_Feature
        self.Product_dimension = Product_dimension
        self.Energy_star = Energy_star
        self.Features = Features
        self.temp_range = temp_range
        self.price = price


    def show(self)->None:
        """
        print all the properties of class AC
        """

        print("Brand",self.Brand)

        print("Capacity",self.Capacity)

        print("Special_Feature",self.Special_Feature)

        print("Product_dimension",self.Product_dimension.getDimension())

        print("Energy_star",self.Energy_star)

        print("Features",self.Features)

        print("temp_range",self.temp_range)

        print("price",self.price)


def main()->None:
    """
    main function
    """
    LG_ACs = AC("LG",
                1.5,
                "Anti bacterial Filter",
                Dimension(84,30, 50,233),
                4,
                ["6th Sense Technology",
                "Xpand Cooling Technology",
                "Anti rust coil Coated condensor",
                "PM 2.5µ Filter",
                "Microblock Filter",
                "55°C Operation",
                "BLDC Fans"
                ],
                range(-25,30),
                78000.33
                )
    
    LG_ACs.show()

    sys.exit(0)

main()
