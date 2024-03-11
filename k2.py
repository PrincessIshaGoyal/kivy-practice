import kivy  
from kivy.app import App  
from kivy.uix.widget import Widget  
from kivy.uix.button import Button  
from kivy.uix.progressbar import ProgressBar  
from kivy.uix.boxlayout import BoxLayout  
from kivy.clock import Clock  
from time import sleep  
   
class MainMenu(BoxLayout):  
    def __init__(self):  
        super().__init__()  
        self.orientation = 'vertical'  
         
        self.btn = Button(text="Start")  
        self.btn.bind(on_release=self.trigger)  
        self.add_widget(self.btn)  
         
        self.MyList = "My Name Is Isha..."
        self.i = 0  
        self.pb = ProgressBar(max = len(self.MyList), value = 0)      
        self.add_widget(self.pb)  
                 
    def trigger(self, *args):  
      self.i = 0  
      self.pb.value = 0  
       
      Clock.schedule_interval(self.heavyFunc,0.1)
      
    def heavyFunc(self, dt):  
        sleep(0.1)
        print(self.MyList[self.i])
        self.btn.text=self.MyList[0:self.i]
        self.i += 1  
        self.pb.value +=1  
        if self.i >= len(self.MyList):  
            Clock.unschedule(self.heavyFunc)  
            print('unscheduled')  
   
class TestApp(App):  
    def build(self):  
        return MainMenu()  
   
root = TestApp()  
root.run()  
