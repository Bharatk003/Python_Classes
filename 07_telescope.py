
"""
@Author: Bharat Kshiragar
@Date : 30/12/2024
@Goal : To implement class telescope

@link : https://www.amazon.com/dp/B0C5HZ5R5T/ref=sspa_dk_detail_6?pd_rd_i=B0C5HZ5R5T&pd_rd_
w=l0TsS&content-id=amzn1.sym.f734d1a2-0bf9-4a26-ad34-2e1b969a5a75&pf_rd_p=f734d1a2-0bf9-4a26-
ad34-2e1b969a5a75&pf_rd_r=5AMZPGMFZ9KDQG4JCC2V&pd_rd_wg=i67sr&pd_rd_r=cdf70168-4238-4f34-a71b-be0c4c876
03f&s=photo&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1

"""
import sys
from DimensionUDD import Dimension
class Telescope:
    """
    class represent the telescope class 

    raise : 
    - type error: if any attribute has invalid type
    - value error: if any attribute missing it value range

    method():
    - show(): it prints all the properties of class Battery

    """
    

    def __init__(self,
                Brand:str,
                Optical_tube_Length:float,	 
                Eye_Piece_Lens_description:str, 
                Objective_Lens_Diameter:float,
                Telescope_Mount_Description	: str,
                Product_Dimensions	: Dimension,
                Focus_Type :str,
                Finderscope	: str,
                Item_Weight	: int,
                Compatible_Devices:list	 
                 )->None:
        """
        constructor of class telescope

        """
        if type(Brand) != str:
            raise TypeError("bad type: it should be str")
        
        if type(Optical_tube_Length) != float:
            raise TypeError("bad type: it should be float")
        
        if type(Eye_Piece_Lens_description) != str:
            raise TypeError("bad type: it should be str")

        if type(Objective_Lens_Diameter) != float:
            raise TypeError("bad type: it should be str")

        if type(Telescope_Mount_Description) != str:
            raise TypeError("bad type: it should be str")
        
        if type(Product_Dimensions) != Dimension:
            raise TypeError("bad type: it should be Dimesion")
        
        if type(Focus_Type) != str:
            raise TypeError("bad type: it should be str")

        if type(Finderscope) != str:
            raise TypeError("bad type: it should be str")

        if type(Item_Weight) != int:
            raise TypeError("bad type: it should be int ")

        if type(Compatible_Devices) != list:
            raise TypeError("bad type : it should be list")
        


        self.Brand = Brand

        self.Optical_tube_Length = Optical_tube_Length

        self.Eye_Piece_Lens_description = Eye_Piece_Lens_description

        self.Objective_Lens_Diameter = Objective_Lens_Diameter

        self.Telescope_Mount_Description = Telescope_Mount_Description

        self.Product_Dimensions = Product_Dimensions

        self.Focus_Type = Focus_Type

        self.Finderscope = Finderscope

        self.Item_Weight = Item_Weight

        self.Compatible_Devices = Compatible_Devices


    def show(self)->None:

        """
        These function print out all the properties of class telescope
        
        """

        print("Brand: ",self.Brand) 

        print("Optical_tube_Length: ",self.Optical_tube_Length) 

        print("Eye_Piece_Lens_description: ",self.Eye_Piece_Lens_description) 

        print("Objective_Lens_Diameter: ",self.Objective_Lens_Diameter) 

        print("Telescope_Mount_Description: ",self.Telescope_Mount_Description) 

        print("Product_Dimensions: ", end=""),self.Product_Dimensions.getDimension() 

        print("Focus_Type: ",self.Focus_Type) 

        print("Finderscope: ",self.Finderscope) 

        print("Item_Weight: ",self.Item_Weight) 

        print("Compatible_Devices: ",self.Compatible_Devices)    




def main()->None:

    HAWKKO_Telescopes = Telescope(
                                    "hawkoo",
                                    700.3,
                                    "Kellner",
                                    90.34,
                                    "Altazimuth Mount",
                                    Dimension(31.6,5.5,10.5,10),
                                    "manual Focus",
                                    "reflex",
                                    10, 
                                    ["smartPhone", "laptop", "pc", "supercomputers"]              

                                )
    
    HAWKKO_Telescopes.show()
    sys.exit(0)

main()
 