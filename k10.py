# implementation of Animation in Kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.button import Button
from random import random

class AnimationExample(App):
    def build(self):
        self.layout = FloatLayout()
        self.button = Button(text='Coding Ninjas', size_hint=(0.2,0.07), pos_hint={'x':0.001,'y':0.005}, on_press=self.animation)
        self.layout.add_widget(self.button)
        return self.layout

    def animation(self,*args):
        anim = Animation(pos_hint = {'x':random(),'y':random()}, d = random(), t='in_circ')
        anim += Animation(pos_hint = {'x':0,'y':0}, d = random() )
        anim.start(self.button)

# Run the app
if __name__ == '__main__':
    AnimationExample().run()
