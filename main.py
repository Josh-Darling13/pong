from unicodedata import numeric
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector

class PongBall(Widget):
    #this make the "ball move"
    # Kivy will design the ball
    # a realtionship a kin to Javascript and CSS
    
    #velocity of the ball on x & y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    
    # referancelist property to use ball.velocity
    # this is shorthand
    velocity = ReferanceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()
    
if __name__ == '__main__':
    PongApp().run()