# Испорт библиотек
# Kivy - для граф. интерфейса
# Pandas - для работы с базами данных
# Re - для работы с регулярными выражениями
# Dfgui - для визуалтзации pandas dataframe (таблицы)
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
import pandas as pd
import re
from dfguik import DfguiWidget

Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.FadeTransition

<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            # source: '.data//fon.png'
    FloatLayout:
        Label:
            text: "[b][color=#A6622B]Логин[/color][/b]"
            size_hint: (.25, .08)
            pos_hint: {'x':2, 'y':6} 
        TextInput:
            text: 'логин'
            size_hint: (.25, .08)
            pos_hint: {'x':2, 'y':5} 
        Label:
            text: "Пароль"
            size_hint: (.25, .08)
            pos_hint: {'x':2, 'y':4} 
        TextInput:
            text: 'пароль'
            size_hint: (.25, .08)
            pos_hint: {'x':2, 'y':3} 
        Button:
            text: "Вход"
            size_hint: (.25, .08)
            pos_hint: {'x':2, 'y':2} 

""")

class LoginScreen(Screen):
    pass

sm = ScreenManager(transition=FadeTransition(duration=.4))
sm.add_widget(LoginScreen(name='login'))

class CoffeeApp(App):

    def build(self):
        self.title = 'Ростелеком'
        #self.icon = '.data\\Rostelecom_logo.png'
        Window.clearcolor = (.5, .5, .5, 1)
        Window.size = (800, 600)

        return sm

        
if __name__ == "__main__":
    CoffeeApp().run()
