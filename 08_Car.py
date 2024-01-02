"""
@Author : Bharat Kshirsagar
@Date : 02/01/2024
@Goal : To implement class pen

@link : https://www.cardekho.com/lamborghini/urus/specs
"""
from DimensionUDD import Dimension
class Car:
    """
    represent the class car

    raise : 
    - type error: if any attribute has invalid type
    - value error: if any attribute missing it value range

    method():
    - show(): it prints all the properties of class Battery

    """

    def __init__(self,
                 fuel_type: str,
                 No_of_cylinder: int,
                 max_torque: str,
                 trasmission_type: str,
                 fuel_tank_capacity: int,
                 Engine_displacement: int,
                 max_power: int,
                 seat_capacity: int,
                 Boot_Space:int,
                 body_type: str,
                 Engine_type:str,
                 Gear_box: int,
                 suspension: str,
                 wheels: int,
                 dimesion: Dimension,

                 )->None:
        """
        constructor for the class car
        
        """
        #type check
        if type(fuel_type) != str:
            raise TypeError("bad type it should be str")

        if type(No_of_cylinder) != int:
            raise TypeError("bad type it should be int")
        
        if type(max_torque) != str:
            raise TypeError("bad type it should be str")
        
        if type(trasmission_type) != str:
            raise TypeError("bad type it should be str")

        if type(fuel_tank_capacity) != int:
            raise TypeError("bad type it should be int")

        if type(Engine_displacement) != int:
            raise TypeError("bad type it should be int")
        
        if type(max_power) != int:
            raise TypeError("bad type it should be int")
        
        if type(seat_capacity) != int:
            raise TypeError("bad type it should be int")

        if type(Boot_Space) != int:
            raise TypeError("bad type it should be int")
        
        if type(body_type) != str:
            raise TypeError("bad type it should be str")

        if type(Engine_type) != str:
            raise TypeError("bad type it should be str")
        
        if type(Gear_box) != int:
            raise TypeError("bad type it should be str")
        
        if type(suspension) != str:
            raise TypeError("bad type it should be str")
        
        if type(wheels) != int:
            raise TypeError("bad type it should be int")

        if type(dimesion) != Dimension:
            raise TypeError("bad type it should be Dimesion")

        
        self.fuel_type = fuel_type
        self.No_of_cylinder = No_of_cylinder 
        self.max_torque = max_torque 
        self.trasmission_type = trasmission_type 
        self.fuel_tank_capacity = fuel_tank_capacity 
        self.Engine_displacement = Engine_displacement
        self.max_power = max_power 
        self.seat_capacity = seat_capacity 
        self.Boot_Space = Boot_Space 
        self.body_type = body_type 
        self.Engine_type = Engine_type 
        self.Gear_box = Gear_box 
        self.suspension = suspension 
        self.wheels = wheels 
        self.dimesion = dimesion 

    def show(self)->None:
                
        """
        show the properties of class car
        """        
        print("fuel_type" ,self.fuel_type)
        print("No_of_cylinder" ,self.No_of_cylinder)
        print("max_torque" ,self.max_torque)
        print("trasmission_type" ,self.trasmission_type)
        print("fuel_tank_capacity" ,self.fuel_tank_capacity)
        print("Engine_displacement",self.Engine_displacement)
        print("max_power" ,self.max_power)
        print("seat_capacity" ,self.seat_capacity)
        print("Boot_Space" ,self.Boot_Space)
        print("body_type" ,self.body_type)
        print("Engine_type" ,self.Engine_type)
        print("Gear_box" ,self.Gear_box)
        print("suspension" ,self.suspension)
        print("wheels" ,self.wheels)
        # print("dimesion:" ,end="")
        self.dimesion.getDimension()

    
        
        
        
def main()->None:

    lamborghini_urus = Car(
                            "petrol",
                            8,
                            "850",
                            "automatic",
                            75,
                            3600,
                            657,
                            5,
                            616,
                            "SUV",
                            "petrol",
                            8,
                            "air",
                            4,
                            Dimension(51,21,16,2150)

                            )

    lamborghini_urus.show()

    exit(0)
main()
        
        
        
        