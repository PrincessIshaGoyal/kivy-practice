from kivy.app import App  
from kivy.uix.slider import Slider  
from kivy.uix.gridlayout import GridLayout  
from kivy.uix.label import Label  
      
class Slider_Demo(GridLayout):  
    def __init__(self):  
        super().__init__()  
   
        self.cols = 2  
   
        self.slider = Slider(min = 0, max = 100, value=50)  
        self.add_widget(self.slider)  
        self.slider.bind(value = self.on_value_change)  
   
        self.label = Label(text = "50")  
        self.add_widget(self.label)  
   
    def on_value_change(self, instance, value):  
        self.label.text = "Value Is : {} ".format(int(value))  
   
   
class SliderWindow(App):  
    def build(self):  
   
        return Slider_Demo()  
   
   
   
root = SliderWindow()  
root.run()  
