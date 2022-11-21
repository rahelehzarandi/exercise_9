# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5)
# increases the travelled distance to 2090 km.

class car:
    def __init__(self,registration_number, maximum_speed, current_speed,travelled_distance):
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

    def distance(self,hours):
        self.travelled_distance=self.travelled_distance+(self.current_speed*hours)
        print(f"next distance is {machin.travelled_distance}")





machin=car("ABC-123",142,60,2000)
machin.distance(1.5)
# print(f"next distance is {machin.travelled_distance}")