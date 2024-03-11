from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from datetime import date

class AgeCalculator(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #self.window.size_hint = (0.5, 0.5)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.img = Image(source="Flowers.png", size_hint = (2,2))
        self.window.add_widget(self.img)

        self.ageRequest = Label(
            text = "Enter your year of birth...",
            font_size = 14,
            color = 'white',
            bold = True
        )
        self.window.add_widget(self.ageRequest)

        self.date = TextInput(
            text='0000',
            multiline=False,
            padding_y = (10, 10),
            size_hint = (1, 1),
            font_size = 30
        )
        self.date.bind(on_submit = self.getAge)
        self.window.add_widget(self.date)

        self.button = Button(
        text = "Calculate Age",
        color = (0,0,0,1),
        background_color = (1,0,1),
#        background_normal='Flowers.png',
#        background_down='Flowers.png',
#        size_hint = (0.5, 0.5),
        height = 100,
        bold = True,
        font_size = 30
        )
        self.button.bind(on_press = self.getAge)
        self.button.l0 = Label(text = '0',
                        font_size = 20,
                        color = 'white')
        self.button.add_widget(self.button.l0)
        self.window.add_widget(self.button)

        self.button.bind(pos = self.update_0, size = self.update_0)

        return self.window

    def getAge(self,event):
        today=date.today().year
        dob=self.date.text
        age=int(today)-int(dob)
        self.ageRequest.text="You are "+str(age)+" years old."

    def update_0(self, instance, value):
        self.button.l0.pos = (self.button.pos[0]//2, self.button.pos[1]-20)
        self.button.l0.size = self.button.size
        print(self.window.size, self.window.pos)


if __name__=="__main__":
    AgeCalculator().run()
