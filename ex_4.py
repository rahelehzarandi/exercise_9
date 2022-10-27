class car:
    def __init__(self,registration_number,maximum_speed,current_speed=0,travelled_distance=0):

        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=travelled_distance

    def accerelate(self,speed):
        self.current_speed=self.current_speed + speed

    def drive(self,hours=1):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours
        if self.travelled_distance >= 10000:
            print(vars(car_name))



import random
car_list=[]
register_num_list=['ABC-1','ABC-2','ABC-3','ABC-4','ABC-5','ABC-6','ABC-7','ABC-8','ABC-9','ABC-10']
#car_name_list=['Ford','Ferrari','Porsche','Lamborghini','Jeep','Jensen Interceptor','Land Rover','Rolls-Royce','Suzuki']
maximum_speed_list=[]

for i in range(0,10):

    maximum_speed= random.randrange(100,200)
    maximum_speed_list.append(maximum_speed)

    car_name=car(register_num_list[i],maximum_speed_list[i])
    speed=random.randrange(-10,15)

    car_name.accerelate(speed)
    car_name.drive(1)
