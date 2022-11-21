# Extend the program by adding an accerelate method into the new class. The method should receive the change of
# speed (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of
# the speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the
# speed and then print out the final speed. The travelled distance does not have to be updated yet.


class car:
    def __init__(self,registration_number, maximum_speed, current_speed,travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=travelled_distance

    def accerelate(self,change_speed):
        if self.current_speed+change_speed<self.maximum_speed and self.current_speed+change_speed>0:
            self.current_speed=change_speed +self.current_speed
            print(f"the speed is {self.current_speed}")


        elif(self.current_speed+change_speed>self.maximum_speed):
            print("current speed +50 is over maximum speed")
        elif(self.current_speed + change_speed < 0):
            print("current speed -200 is lower zero")





machin=car("ABC-123",142,0)
machin.accerelate(30)
# print(f"speed +30 is {machin.current_speed}")
machin.accerelate(70)
# print(f"speed +70 is {machin.current_speed}")
machin.accerelate(50)
# print(f"{machin.current_speed}")
machin.accerelate(-200)
# print(f"{machin.current_speed}")
