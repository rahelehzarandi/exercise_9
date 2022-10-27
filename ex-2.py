class car:
    def __init__(self,registration_number,maximum_speed,current_speed=0,travelled_distance=0):
        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=travelled_distance

    def accerelate(self,change_speed):

        #while current_speed > 0 and change_speed < 142:
            if (change_speed < 0 ):

                self.current_speed = self.current_speed + change_speed
                print(self.current_speed)

            else:
                self.current_speed=self.current_speed + change_speed
                print(self.current_speed)


ford=car("ABC-123",142)
ford.accerelate(30)
ford.accerelate(70)
ford.accerelate(50)
ford.accerelate(-200)

