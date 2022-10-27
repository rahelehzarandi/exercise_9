class car:
    def __init__(self,registration_number,maximum_speed,current_speed=0,travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=travelled_distance





ford=car("ABC-123",142)
Ferrari=car("CDE-456",150)
print(f"the information of Ford car is:{ford.registration_number},{ford.maximum_speed},{ford.current_speed},{ford.travelled_distance}")
print(f"the information of Ferrary car is:{Ferrari.registration_number},{Ferrari.maximum_speed},{Ferrari.current_speed},{Ferrari.travelled_distance}")
print(vars(ford))