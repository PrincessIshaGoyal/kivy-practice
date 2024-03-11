import kivy      
from kivy.app import App     
kivy.require('1.9.0')   
from kivy.uix.switch import Switch #import switch Module   
from kivy.uix.gridlayout import GridLayout     
from kivy.uix.label import Label   
    
class SimpleSwitch(GridLayout):   
     def __init__(self, **kwargs):   
          super(SimpleSwitch, self).__init__(**kwargs)
          self.cols = 2
          self.add_widget(Label(text ="Switch"))
          self.settings_sample = Switch(active = False)
          self.add_widget(self.settings_sample)
          self.settings_sample.bind(active = switch_callback)
   
def switch_callback(switchObject, switchValue):
    if(switchValue):
        print('Switch is ON:):):)')   
    else:
        print('Switch is OFF:(:(:(')
  
class SwitchApp(App):
     def build(self):
          return SimpleSwitch()
     
  
if __name__ == '__main__':   
     SwitchApp().run()  
