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
import dfgui