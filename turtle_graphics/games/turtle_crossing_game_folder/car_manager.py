from turtle import *
import random
class CarManager(Turtle):
   def __init__(self,color_list,screen_width, screen_height) :
        super().__init__()
        self.hideturtle()
        self.color_list = color_list
        self.x_axis = screen_height // 2
        self.y_axis = screen_width // 2
        self.car_speed = 5
        self.cars = []
        self.penup()
   def generate_cars(self):
         car = Turtle()
         car.showturtle()
         car.penup()
         car.shape("square")
         car.shapesize(stretch_len = 2, stretch_wid = 1)
         car.speed(self.car_speed)
         car.color(random.choice(self.color_list))
         car.goto(x = self.x_axis - 40 ,y = random.randint((self.y_axis  * -1) + 20 ,self.y_axis  - 20))
         self.cars.append(car)
   def move_cars(self):
      for car in self.cars:
         car.goto(x = car.xcor() - self.car_speed, y = car.ycor())
         if car.xcor() <  self.x_axis * -1:
            car.goto(x = self.x_axis - 30 ,y = random.randint((self.y_axis  * -1) + 20 ,self.y_axis  - 20))
   def reset_cars(self):
      for car in self.cars:
         car.hideturtle()
      self.cars.clear()
      
