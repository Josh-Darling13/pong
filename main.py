from unicodedata import numeric
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongBall(Widget):
    #this make the "ball move"
    # Kivy will design the ball
    # a realtionship a kin to Javascript and CSS
    
    #velocity of the ball on x & y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    
    # referancelist property to use ball.velocity
    # this is shorthand
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    
    def update(self, dt):
        """
        Purpose: 
        call ball and movie it around
        """
        # ball bounces of top and bottom
        if (self.ball.y <0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
            
        # ball bounces of left and right
        if (self.ball.x <0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        
        pass

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(gamex.update, 1.0/60.0)
        return game
    
if __name__ == '__main__':
    PongApp().run()