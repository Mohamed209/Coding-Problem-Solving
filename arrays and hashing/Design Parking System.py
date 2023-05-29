# https://leetcode.com/problems/design-parking-system/
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots = {"big": big, "med": medium, "sml": small}

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.slots["big"] > 0:
                self.slots["big"] -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.slots["med"] > 0:
                self.slots["med"] -= 1
                return True
            else:
                return False
        else:
            if self.slots["sml"] > 0:
                self.slots["sml"] -= 1
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
