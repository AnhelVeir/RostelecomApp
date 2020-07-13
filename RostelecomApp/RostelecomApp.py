# Испорт библиотек
# Kivy - для граф. интерфейса
# Pandas - для работы с базами данных
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
from random import randint

Builder.load_string("""
#:import SlideTransition kivy.uix.screenmanager.FadeTransition

<LoginScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//Fon.png'
    on_enter:
        root.enter_screen()
    FloatLayout:
        Image:
            source: ".data//Rostelecom_logo.png"
            size_hint: (.3, .3)
            pos_hint: {'x':.25, 'y':.65} 
        Label:
            text: "[color=#3E3A37]Логин[/color]"
            markup: True
            size_hint: (.3, .05)
            pos_hint: {'x':.13, 'y':.59}
        TextInput:
            id: login_input
            text: ''
            size_hint: (.4, .05)
            pos_hint: {'x':.25, 'y':.55} 
        Label:
            text: "[color=#3E3A37]Пароль[/color]"
            markup: True
            size_hint: (.3, .05)
            pos_hint: {'x':.135, 'y':.49} 
        TextInput:
            id: password_input
            text: ''
            size_hint: (.4, .05)
            pos_hint: {'x':.25, 'y':.445} 
            password : True
        Button:
            text: "Вход"
            size_hint: (.4, .08)
            pos_hint: {'x':.25, 'y':.35} 
            on_press:
                app.user_id = root.log_in(app.users, app.user_id)
        Button:
            text: "Регистрация"
            size_hint: (.4, .08)
            pos_hint: {'x':.25, 'y':.26} 
            on_press:
                root.sign_up(app.users)
        Button:
            text: ""
            size_hint: (.05, .05)
            pos_hint: {'x':.65, 'y':.445} 
            opacity: 0.2
            on_press:
                root.show_pass()
        Image:
            source: ".data//Show_pass.png"
            size_hint: (.05, .05)
            pos_hint: {'x':.65, 'y':.445} 
        Label:
            id: info_label
            text: ''
            markup: True
            font_size: '18sp'
            size_hint: (.6, .1)
            pos_hint: {'x':.15, 'y':.15} 

<PassesScreen>:
    on_enter:
        root.enter_screen(app.user_id)
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: '.data//Fon2.png'
    FloatLayout:
        Label:
            id: user_id
            text: '[color=#3E3A37]id:[/color]'
            size_hint: (.15, .1)
            pos_hint: {'x':.01, 'y':.9} 
            markup: True
        Label:
            text: '[b][color=#3E3A37]Просмотр пропусков сотрудников[/color][/b]'
            font_size: '24sp'
            size_hint: (.8, .1)
            pos_hint: {'x':.1, 'y':.9} 
            markup: True
        Image:
            source: ".data//report.png"
            size_hint: (1, .9)
            pos_hint: {'x':.02, 'y':0} 

        Button:
            text: "Назад"
            size_hint: (.1, .05)
            pos_hint: {'x':.9, 'y':.02} 
            on_release:
                root.manager.current = 'login'


""")


class LoginScreen(Screen):
    show_pass_status = True

    def enter_screen(self):
        """
        Очищает поля ввода
        :return: None
        """
        self.ids.login_input.text = ''
        self.ids.password_input.text = ''
        self.ids.info_label.text = ''

    def show_pass(self):
        """
        Скрывает/показывает введенный пароль
        :return: None
        """
        if self.show_pass_status:
            self.show_pass_status = False
            self.ids.password_input.password = False
        else:
            self.show_pass_status = True
            self.ids.password_input.password = True

    def log_in(self, users, user_id):
        """
        Проверка логина и пароля на соответствии инф-и в бд.
        Возвращает имя пользователя
        :return: str
        """
        try:
            temp_passw = users[users.user == self.ids.login_input.text]['pass'].tolist()[0]
            if temp_passw == self.ids.password_input.text:
                self.manager.current = 'main'
                return users[users.user == self.ids.login_input.text]['id'].tolist()[0]
            else:
                self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'
        except KeyError:
            self.ids.info_label.text = '[color=#DD1B07]Неверный пароль[/color]'
        except IndexError:
            self.ids.info_label.text = '[color=#DD1B07]Пользователь не найден[/color]'

    def sign_up(self, users):
            """
            Добавление пользователя в бд users.
            :return: None
            """
            try:
                users[users.user == self.ids.login_input.text]['pass'].tolist()[0]
            except IndexError:
                if len(self.ids.login_input.text) < 4 or len(self.ids.password_input.text) < 4:
                    self.ids.info_label.text = '[color=#DD1B07]Имя пользователя и пароль должны состоять из 4 и более ' \
                                               'символов[/color] '
                else:
                    self.last_index = users.count()[0]
                    self.id = str(randint(10000000, 99999999))
                    while len(users[users.id == self.id]) != 0:
                        self.id = str(randint(10000000, 99999999))
                    users.loc[self.last_index] = {'user': self.ids.login_input.text, 'pass': self.ids.password_input.text, 'id': self.id}
                    self.ids.info_label.text = '[color=#DD1B07]Вы зарегистрированы. Нажмите "Войти"[/color]'
                    users.to_csv('.data\\users.csv', sep=';')
            else:
                self.ids.info_label.text = '[color=#DD1B07]Пользователь с таким именем уже зарегистрирован[/color]'

class PassesScreen(Screen):
    def enter_screen(self, user_id):
        """
        Добавляет id поьзователя
        :return: None
        """
        self.ids.user_id.text = '[color=#3E3A37]id:'+str(user_id)+'[/color]'
        
sm = ScreenManager(transition=FadeTransition(duration=.4))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(PassesScreen(name='main'))

class Rostelecom(App):

    def build(self):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        self.title = 'Ростелеком'
        self.icon = '.data\\Rostelecom_icon.png'
        Window.size = (800, 600)
        Window.clearcolor = (.7, .7, .7, 1)
        self.users = pd.read_csv('.data\\users.csv', sep=';', index_col=[0])
        self.user_id = ''
        return sm

        
if __name__ == "__main__":
    Rostelecom().run()
