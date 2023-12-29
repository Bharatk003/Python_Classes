"""
 
@Author : Bharat Kshirsagar
@Date : 29-12-2023
@Goal : implement class Dimension for the reusability of the user define datatype
 
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
        print("Dimension: ", self.getlength(), "x", self.getbreadth(), "x", self.getheight(), ":", self.getweight())

