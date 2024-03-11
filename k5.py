import kivy  
from kivy.app import App  
from kivy.uix.button import Button  
from kivy.uix.label import Label  
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout  

class Popup_Demo(App):  
  
    def build(self):  
  
        layout = GridLayout(cols = 1, padding = 10)  
  
        self.button = Button(text="Click Here to view Popup")  
  
        layout.add_widget(self.button)  
  
        self.button.bind(on_press = self.onButtonPress)   
  
        return layout  
  
    def onButtonPress(self, button):

        sv = ScrollView()
  
        layout      = GridLayout(cols = 2, padding = 10, size_hint_y = None)
        layout.bind(minimum_height = layout.setter('height'))
  
        popupLabel  = Label(text  = "a"*50+"\n"+"-"*100, font_size=20, height=40, size_hint=(1, None))

        for i in range(20):
            l = Label(text  = str(i)+"a"*50+"\n"+"-"*100, font_size=20, height=40, size_hint=(1, None))
            layout.add_widget(l)

        closeButton = Button(text = "Close the pop-up window")  
  
        layout.add_widget(popupLabel)
  
        layout.add_widget(closeButton)

        sv.add_widget(layout)
  
        popup = Popup(title = 'Demo Popup',  
  
                      content = sv)    
  
                   
  
        popup.open()     
  
        closeButton.bind(on_press = popup.dismiss)
  
root = Popup_Demo()  
root.run()

