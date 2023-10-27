# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock


class Background(Widget):
    cloud_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cloud_texture = Image(source="cloud.png").texture
        self.cloud_texture.wrap = "repeat"
        self.cloud_texture.uvsize = (Window.width/self.cloud_texture.width, -1)

    def scroll_textures(self, time_passed):
        self.cloud_texture.uvpos = ((time_passed + self.cloud_texture.uvpos[1]) % self.parent.width, self.cloud_texture.uvpos[1])
        texture = self.property("cloud_texture")
        texture.dispatch(self)


class PaltfromreApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.background.scroll_textures, 1/20)


class Display(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def scale(self, size):
        R = (7, 4)
        width, height = size
        new_width = width
        new_height = height
        if width/R[0] < height/R[1]:
            new_height = int((R[1]/R[0])*width)
        elif width/R[0] > height/R[1]:
            new_width = int((R[0]/R[1])*height)
        return new_width, new_height


PaltfromreApp().run()
