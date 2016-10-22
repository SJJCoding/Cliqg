
import simplegui

class ShapeAttributes:
    def __init__(self):
        self.line_width = 100
        self.line_color = "red"
        self.fill_color = "red"
        
        
    
    

class Circle:
    def __init__(self):
        self.radius = 50
        self.center_point = (100, 100)
    def update_x(self, shift_x):
        self.center_point = (
        self.center_point[0] + shift_x,
        self.center_point[1]
            )
    def update_y(self, shift_y):
        self.center_point = (
        self.center_point[0],
        self.center_point[1] + shift_y, 
            )    
    
    
class Character:
    key_map = {
        "right": 39,
        "left": 37,
        "up": 38,
        "down": 40,
    
    }

    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttributes()
        self.movement = 10
        self.movement2 = -10
        self.movement3 = 10
        self.movement4 = -10
    def draw_me(self, canvas):
        
        canvas.draw_circle(self.circle_shape.center_point,
                           self.circle_shape.radius,
                           self.shape_attributes.line_width,
                           self.shape_attributes.line_color,
                           self.shape_attributes.fill_color
                           )
                           
    def move(self, key):
        if key == 39:
            self.circle_shape.update_x(self.movement)
        if key == 37:
            self.circle_shape.update_x(self.movement2)
        if key == 40:
            self.circle_shape.update_y(self.movement3)
        if key == 38:
            self.circle_shape.update_y(self.movement4)    
        print key
                           
                           
        
              
        #canvas.draw_circle((200, 200) , 50, 100,   "red")
    

cliq = Character()
#print type(cliq)

# Handler to draw on canvas
def draw(canvas):
    cliq.draw_me(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 500, 500)



# Start the frame animation
frame.set_draw_handler(draw)
frame.set_keydown_handler(cliq.move)
frame.start()
