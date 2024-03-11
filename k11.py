from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from random import choice

class Math_Test(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 2
        self.window.size_hint = (0.5, 0.5)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5 }

        self.answer, self.prob = Label(font_size=30), Label(font_size=30)
        self.cbd = {CheckBox(width=1):Label(), CheckBox(width=1):Label(), CheckBox(width=1):Label(), CheckBox(width=1):Label(), CheckBox(width=1):Label()}
        self.make_new_question()

        self.window.add_widget(self.answer)
        self.window.add_widget(self.prob)
        for i in self.cbd:
            i.bind(active = self.on_checkbox_active)
            self.window.add_widget(i)
            self.window.add_widget(self.cbd[i])
        self.next = Button(text = 'Next')
        self.next.bind(on_press = self.check)
        self.window.add_widget(self.next)
        self.points = Label(text = "0 pts", font_size = 30)
        self.window.add_widget(self.points)

        return self.window

    def on_checkbox_active(self, checkbox, value):
        if value:
            print(self.cbd[checkbox].text, "is active")
        else:
            print(self.cbd[checkbox].text, "is inactive")

    def check(self, event):
        p = int(self.points.text[:len(self.points.text)-4])
        if(self.acb.active):
            self.acb.active = False
            p += int(self.cbd[self.acb].text)
        for i in self.cbd:
            if(i.active):
                p -= int(self.cbd[i].text)
                i.active = False
        self.points.text = str(p)+" pts"
        self.make_new_question()

    def make_new_question(self):
        a = choice(range(50,10000))
        b = choice(range(a))
        self.answer.text = str(a)+' ='
        self.prob.text = str(b)+' +'
        self.acb = choice(list(self.cbd))
        self.ans = a-b
        for i in self.cbd:
            self.cbd[i].text = str(choice(range(10000)))
        self.cbd[self.acb].text = str(self.ans)

if __name__=="__main__":
    Math_Test().run()
