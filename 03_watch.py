"""
@Author : Bharat Kshirsagar
@Date : 26-12-2023
@Goal : implement class watch

@Link : https://www.amazon.in/Timex-Analog-Blue-Dial-Watch-TW00ZR262E/dp/B07H3K85H5/ref=sr_1_10?
crid=FCJV6JJSFIKG&keywords=watches&qid=1703562582&s=watches&sprefix=analog%2Bwatches%2Cwatches%2C281&sr=1-10&th=1

"""

# server site
class Dimension:
    """
    These class implement the Dimenstion class

    """
    def __init__(self,
                 length: float,
                 breadth: float,
                 height: float,
                 weight: float,
                 )->None:
        # type and value checks     
        """
        constructor
        """
        if type(length) != float:
            raise TypeError("bad type: it should be float")
        
        if type(breadth) != float:
            raise TypeError("bad type: it should be float")
        
        if type(height) != float:
            raise TypeError("bad type: it should be float")
        
        if type(weight) != float:
            raise TypeError("bad type: it should be float")
        
        if length <= 0 and breadth <= 0 and height <= 0 and weight <= 0:
            raise ValueError("One or more argument contain invalid value")
        
        self.length = length
        self.breadth = breadth
        self.height = height
        self.weight = weight

    def get_Dimension(self)->None:
        """
        It prints the dimension of product case in the form of 

        length x breadth x height : weight

        """
        print(self.length, "x", self.breadth, "x", self.height, ":", self.weight)
    

class watch:
    """
    These class implement the watch 
    """
    def __init__(self,
                BandColour: str,	
                BandMaterial: [str],	
                BandWidth: str,	 
                BezelMaterial: str,	
                Brand: str,	
                CaseDiameter: Dimension,	 
                CaseMaterial: str,	
                CaseThickness: str, 
                DialColour: str,	
                CrystalMaterial: str,	
                DisplayType: str,	
                CaseShape: str,	
                ItemWeight: str,	 
                ModelNumber: str,	
                PartNumber: str,	
                SpecialFeature: [str],	    
                WarrantyType: str,	
                WaterResistanceDepth: str,
                price: float
                )->None:
        # type and value checking

        if type(BandColour) != str:
            raise TypeError("bad type: it should be str")
        
        if type(BandMaterial) != list:
            raise TypeError("bad type: it should be list")
        
        if type(BandWidth) != str:
            raise TypeError("bad type: it should be str")
        
        if type(BezelMaterial) != str:
            raise TypeError("bad type: it should be str")

        if type(Brand) != str:
            raise TypeError("bad type: it should be str")
        
        if type(CaseDiameter) != Dimension:
            raise TypeError("bad type: it should be Dimension")
        
        if type(CaseMaterial) != str:
            raise TypeError("bad type: it should be str")
        
        if type(CaseThickness) != str:
            raise TypeError("bad type: it should be str")
        
        if type(DialColour) != str:
            raise TypeError("bad type: it should be str")
        
        if type(CrystalMaterial) != str:
            raise TypeError("bad type: it should be str")
        
        if type(DisplayType) != str:
            raise TypeError("bad type: it should be str")
        
        if type(CaseShape) != str:
            raise TypeError("bad type: it should be str")

        if type(ItemWeight) != str:
            raise TypeError("bad type: it should be str")

        if type(ModelNumber) != str:
            raise TypeError("bad type: it should be str")
        
        if type(PartNumber) != str:
            raise TypeError("bad type: it should be str")

        if type(SpecialFeature) != list:
            raise TypeError("bad type: it should be str")
        
        if type(WarrantyType) != str:
            raise TypeError("bad type: it should be str")
        
        if type(WaterResistanceDepth) != str:
            raise TypeError("bad type: it should be str")
        
        if type(price) != float:
            raise TypeError("bad type: it shoud be float")


        self.BandColour = BandColour
        self.BandMaterial = BandMaterial
        self.BandWidth = BandWidth
        self.BezelMaterial = BezelMaterial
        self.Brand = Brand
        self.CaseDimension = CaseDiameter
        self.CaseMaterial = CaseMaterial
        self.CaseThickness = CaseThickness
        self.DialColour = DialColour
        self.CrystalMaterial = CrystalMaterial
        self.DisplayType = DisplayType
        self.CaseShape = CaseShape
        self.ItemWeight = ItemWeight
        self.ModelNumber = ModelNumber
        self.PartNumber = PartNumber
        self.SpecialFeature = SpecialFeature
        self.WarrantyType = WarrantyType
        self.WaterResistanceDepth = WaterResistanceDepth
        self.price = price

    def show(self)->None:

        print("BandColour:", self.BandColour)

        print("BandMaterial:", self.BandMaterial)

        print("BandWidth:", self.BandWidth)

        print("BezelMaterial:", self.BezelMaterial)

        print("Brand:", self.Brand)

        print("CaseDimension:", end=" "),
        self.CaseDimension.get_Dimension()

        print("CaseMaterial:", self.CaseMaterial)

        print("CaseThickness:", self.CaseThickness)

        print("DialColour:", self.DialColour)

        print("CrystalMaterial:", self.CrystalMaterial)

        print("DisplayType:", self.DisplayType)

        print("CaseShape:", self.CaseShape)

        print("ItemWeight:", self.ItemWeight)

        print("ModelNumber:", self.ModelNumber)

        print("PartNumber:", self.PartNumber)

        print("SpecialFeature:", self.SpecialFeature)

        print("WarrantyType:", self.WarrantyType)

        print("WaterResistanceDepth:", self.WaterResistanceDepth)

        print("Price", self.price)

def main()->None:

    """main function"""

    Fossil_Chronograph_White_Dial_Mens_Watch = watch(
                                                "Brown",
                                                ["leader","brass", "steel"],
                                                "20 millimeter",
                                                "brass",
                                                "TIMEX",
                                                Dimension(25.3,25.3,14.33,128.00),
                                                "Brass",
                                                "8.8 millimeter",
                                                "BLUE",
                                                "Mineral",
                                                "Analog",
                                                "Round",
                                                "52 grams",
                                                "TW00ZR26E",
                                                "TW0003red",
                                                ["water Resistant", "Chronograph", "Scratch Resistance"],
                                                "manufacturer",
                                                "30 meters",
                                                9992.34
                                                )

 
    Fossil_Chronograph_White_Dial_Mens_Watch.show()

main()