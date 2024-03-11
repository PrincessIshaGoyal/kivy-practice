from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color

class pp(App):
    def build(self):
        self.layout_main = GridLayout(cols=2, size=(800,600), pos_hint={'center_x':0.5, 'center_y':0.5})
        self.layout = ScrollView(size_hint_x=None, size_hint_y=None, width=200, height=600)
        self.mini = GridLayout(cols = 1, size_hint_x=None, width=200, size_hint_y=None, size=(200,600), pos_hint={"center_x":0.5,"center_y":0.5})
        self.mini.bind(minimum_height = self.mini.setter('height'))
        with self.mini.canvas:
            Color(1,1,1,1)
            self.rect = Image(source="White.png", allow_stretch=True, keep_ratio=False, size_hint = (1,1), pos_hint = {'center_x':0.5, 'center_y':0.5})
        self.mini.bind(pos = self.update_rect, size = self.update_rect)
        for i in range(100):
            self.mini.add_widget(Label(text=str(i), color="black", size_hint=(1,None), size=(200,100)))
        self.layout.add_widget(self.mini)
        self.mini.add_widget(Label(text=str(100), size_hint=(1,None), size=(200,50)))
        self.layout_main.add_widget(self.layout)

        self.layout2 = ScrollView(size_hint_x=None, size_hint_y=None, width=600, height=600)
        self.mini2 = GridLayout(cols = 1, size_hint_x=None, width=600, size_hint_y=None, size=(600,600), pos_hint={"center_x":0.5,"center_y":0.5})
        self.mini2.bind(minimum_height = self.mini2.setter('height'))
        with self.mini2.canvas:
            Color(1,1,1,1)
            self.rect2 = Image(source="White.png", allow_stretch=True, keep_ratio=False, size_hint = (1,1), pos_hint = {'center_x':0.5, 'center_y':0.5})
        self.mini2.bind(pos = self.update_rect2, size = self.update_rect2)
        for i in range(100):
            self.mini2.add_widget(Label(text=str(i), color="black", size_hint=(1,None), size=(600,50)))
        self.layout2.add_widget(self.mini2)
        self.mini2.add_widget(Label(text=str(100), size_hint=(1,None), size=(600,50)))
        self.layout_main.add_widget(self.layout2)
        self.mini2.cols = 2

        return self.layout_main

    def update_rect(self, instance, value):
        self.rect.pos = self.mini.pos
        self.rect.size = self.mini.size

    def update_rect2(self, instance, value):
        self.rect2.pos = self.mini2.pos
        self.rect2.size = self.mini2.size

pp().run()
