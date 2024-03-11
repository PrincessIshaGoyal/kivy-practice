from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

dd = DropDown()
for i in range(10):
    b = Button(text = str(i), size_hint_y=None, height=20)
    b.bind(on_release = lambda b: dd.select(b.text))
    dd.add_widget(b)

mainbtn = Button(text = "Hello", size_hint=(None,None), pos_hint={'center_x':0.5, 'center_y':0.9})
mainbtn.bind(on_release = dd.open)

dd.bind(on_select = lambda instance, x: setattr(mainbtn, 'text', x))

runTouchApp(mainbtn)
