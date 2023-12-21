
"""
@author: Bharat Kshirsagar
@Date : 21-12-2023
@Goal : implement class earphone

@link : https://www.amazon.in/Oneplus-Bluetooth-Wireless-Earphones-Bombastic/dp/B0CBTTCJL6/ref=sr_1_3?crid=CY4BRPCYBVM3&keywords=bluetooth%2Bearphones&qid=1703162874&sprefix=yearphone%2Caps%2C286&sr=8-3&th=1

"""
import sys

# server site
class ProductDimension:
    """
    This class show the dimension in the 
    length , breadth, height, and weight
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
        
        if length <= 0 or breadth <= 0 or height <= 0 or weight <=0:
            raise ValueError("Dimensions should not be negative")

        self.length = length
        self.breadh = breadth
        self.height = height
        self.weight = weight

class Earphone:
    """
    DocStrings
    """
    def __init__(self,
                product_diamensions : ProductDimension,
                Item_model_number: str,
                wireless_communication_tech: str,
                features: [str],
                form_factor: str,
                Manufacturer: str,
                color: str,
                origin_country: str
                 ):
        # type check
        if type(product_diamensions) != ProductDimension:
            raise TypeError("Bad type: it should be ProductDimension:")
        if type(Item_model_number) != str:
            raise TypeError("bad type: it should be str: ")
        if type(wireless_communication_tech) != str:
            raise TypeError("bad type: it should be str")
        
        for f in features:
            if type(f) != str:
                raise TypeError("Type in features should be str: ")
        if type(form_factor) != str:
            raise TypeError("bad type: it should be str")
        if type(Manufacturer) != str:
            raise TypeError("bad type: it should be str")
        if type(color) != str:
            raise TypeError("bad type: it should be str")
        if type(origin_country) != str:
            raise TypeError("bad type: it should be str")
        
        self.product_diamensions = product_diamensions
        self.Item_model_number = Item_model_number
        self.wireless_communication_tech = wireless_communication_tech
        self.form_factor = form_factor
        self.features = features
        self.Manufacturer = Manufacturer
        self.color = color
        self.origin_country = origin_country
            
    def show(self)->None:
        print("Dimensions: ",self.product_diamensions.length,"x",self.product_diamensions.breadh,"x",self.product_diamensions.height,"x",self.product_diamensions.weight)
        print("Item_model_number: ",self.Item_model_number)
        print("Communication_technique: ",self.wireless_communication_tech)
        print("Form_factor: ",self.form_factor)
        print("Feature of Product: ",self.features)
        print("Manufacturer: ",self.Manufacturer)
        print("product of color: ",self.color)
        print("Country of Origin: ",self.origin_country)
         
#client site
def main()->None:
    OnePlus_Bullets_Wireless_Z2 = Earphone(ProductDimension(41.3 ,10.7,2.3 ,28.9),
                                           "BWZ-2 ANC",
                                           "Bluetooth",
                                           ["Sweatproof", "Noise Cancellation", "Lightweight", "Microphone Included"],
                                           "In ear",
                                           "ANZXI RISOUND ELECTRONICS CO. LTD.",
                                           "Booming Black",
                                           "China"
                                           )
    
    OnePlus_Bullets_Wireless_Z2.show()

main()