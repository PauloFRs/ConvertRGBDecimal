#System
import kivy    
from kivy.app import App 
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
#Ui
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

#Configs
Window.clearcolor = 0.16, 0.16, 0.21, 1
Config.set('graphics', 'width', '150')
Config.set('graphics', 'height', '200')
Config.write()

class MyApp(App):
    #Layout and settings
    box = BoxLayout(padding=10, height="20", orientation="vertical")
    bottom = BoxLayout(padding=3, orientation="vertical")

    red = TextInput(text="0",foreground_color=(0.31, 0.98, 0.48),background_color=(0.27, 0.28, 0.35,1), halign = "center", font_size="15", multiline=False)
    green = TextInput(text="0",foreground_color=(0.31, 0.98, 0.48),background_color=(0.27, 0.28, 0.35,1), halign = "center", font_size="15", multiline=False)
    blue = TextInput(text="0",foreground_color=(0.31, 0.98, 0.48),background_color=(0.27, 0.28, 0.35,1), halign = "center", font_size="15", multiline=False)

    button = Button(text="Convert", background_color=(0.38, 0.45, 0.64,1), background_normal=" ")
    button2 = Button(text="",background_normal=" ")
    label = Label(text="0.00, 0.00, 0.00", color=(1.00, 0.47, 0.78), font_size="10")
    #######################################

    #Program
    def build(self):
        self.title = "Convert"
        #Add widgets to container
        self.bottom.add_widget(self.label)
        self.bottom.add_widget(self.button2)
        self.box.add_widget(self.red)
        self.box.add_widget(self.green)
        self.box.add_widget(self.blue)
        self.box.add_widget(self.button)
        self.box.add_widget(self.bottom)
        #Event
        self.button.bind(on_press= self.convert)

        return self.box
    #######################################

    #Program Logic
    def convert(self, button):
        x = float(self.red.text) / 255
        y = float(self.green.text) / 255
        z = float(self.blue.text) / 255

        if int(self.red.text) >= 255:
            self.red.text = "255"
        if int(self.green.text) >= 255:
            self.green.text = "255"
        if int(self.blue.text) >= 255:
            self.blue.text = "255"

        self.label.text = "{:.2f}, {:.2f}, {:.2f}".format(x, y, z)
        self.button2.background_color = (int(self.red.text) / 255, int(self.green.text) / 255, int(self.blue.text) / 255, 1)
        Clipboard.copy(self.label.text)        
    #######################################

if __name__ == "__main__":
    MyApp().run()