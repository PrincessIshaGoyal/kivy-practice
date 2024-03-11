from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color, Line
from random import random

class scale(Widget):
    def __init__(self):
        super(scale, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect_w = Rectangle(size=self.size, pos=self.pos)
            Color(random(), random(), random(), 0.9)
            self.rect_s = Rectangle(size=(self.size[0],30), pos=(0,0))
            
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect_w.pos = self.pos
        self.rect_w.size = self.size
        self.rect_s.size = (self.size[0],30)
        with self.canvas:
            Color(0,0,0,1)
            for i in range(0,self.size[0],10):
                Line(points=[i,0,i,10])
            for i in range(5,self.size[0],10):
                Line(points=[i,0,i,5])
            for i in range(50,self.size[0],50):
                Label(text=str(i), size=(10,10), pos=(i,12))

class Test(App):
    def build(self):
        root_widget = scale()
        return root_widget

Test().run()
