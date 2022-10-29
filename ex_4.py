class car:
    def __init__(self,registration_number,maximum_speed,current_speed=0):

        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=0


    def accerelate(self,speed):
            self.current_speed=self.current_speed + speed

    def drive(self,hours=1):
            self.travelled_distance = self.travelled_distance + self.current_speed * hours




import random
car_list=[]
register_num_list=['ABC-1','ABC-2','ABC-3','ABC-4','ABC-5','ABC-6','ABC-7','ABC-8','ABC-9','ABC-10']

maximum_speed_list=[]
car_race=[]

for i in range(0,10):
    maxSpeed=random.randrange(100,200)
    regNum=register_num_list[i]
    car_list.append(car(regNum,maxSpeed))


win_distance=0
while win_distance <10000:
    for car_race in car_list:
        speed=random.randrange(-10,15)
        car_race.accerelate(speed)
        car_race.drive(1)
        win_distance=max(car_race.travelled_distance,win_distance)

for car_race in car_list:
    print(vars(car_race))

