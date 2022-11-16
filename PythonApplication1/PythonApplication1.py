
#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys, codecs, kivy
# Импорт всех классов

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import pandas as pd
#kv = Builder.load_file("Main.kv")



Builder.load_string("""
<Vhod>:
    text_input: textID_input
    email : Email
    pwd : textID_input
    
    name: "VhodScreen"
    GridLayout:    
        canvas.before:
            Color:
                rgba: (0, 251, 255, 0.5)
            Rectangle:
                pos: self.pos
                size: self.size
 
        rows: 6
        padding: 30
        spacing: 30
        background_color: '#E0FFFF'
  
  
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'HunterShopClear.png' 
                size_hint: 1, 1
            Label:
                text: 'Вход'
                font_size: '60sp'
  
        BoxLayout:
            orientation: 'vertical'
            FloatLayout:
                Label:
                    text: 'E-mail'
                    pos_hint: {'center_x': 0.1, 'y':0.1}
                    font_size: '30sp'
                TextInput:
                    id: Email
                    size_hint: 0.6, 0.7
                    pos_hint: {'center_x': 0.5, 'y':0.3}
                    multiline: False
                    font_size: '30sp'
      
            FloatLayout:
                Label:
                    text: 'Номер'
                    pos_hint: {'center_x': 0.1, 'y':0.4}
                    font_size: '30sp'
                Label:
                    text: 'лицензии'
                    pos_hint: {'center_x': 0.1, 'y':0.0}
                    font_size: 30
                TextInput:
                    id: textID_input
                    size_hint: 0.6, 0.7
                    pos_hint: {'center_x': 0.5, 'y':0.3}
                    multiline: False
                    font_size:30    
    
        BoxLayout:
            pos_hint: 0.5, 0.1
            orientation: 'vertical'
            FloatLayout:
                Button:
                    size_hint: 0.4, 0.6
                    pos_hint: {'center_x': 0.5, 'y':0.2}
                    text: 'Войти'
                    font_size:30
                    on_state:
                        root.insert_text()
                    on_release: 
                        root.validate()
                        root.manager.transition.direction = "up"
                    
      
        FloatLayout:
            Button:
                size_hint: 0.4, 0.6
                pos_hint: {'center_x': 0.5, 'y':0}
                text: 'Регистрация'
                font_size:30
                on_release:
                    root.manager.transition.direction = 'left'
                    root.manager.transition.duration = 1
                    root.manager.current = 'MenuScreen'



<Menu>:
    name: "MenuScreen"

    text_input: textID_input
    email: Email2
    pwd: textID_input

    GridLayout:    
        canvas.before:
            Color:
                rgba: (0, 251, 255, 0.5)
            Rectangle:
                pos: self.pos
                size: self.size
 
        rows: 6
        padding: 30
        spacing: 30
        background_color: '#E0FFFF'
  
  
        BoxLayout:
            orientation: 'vertical'
            Image:
                source: 'HunterShopClear.png' 
                size_hint: 1, 1
            Label:
                text: 'Регистрация'
                font_size: '60sp'
  
        BoxLayout:
            orientation: 'vertical'
            FloatLayout:
                Label:
                    text: 'E-mail'
                    pos_hint: {'center_x': 0.1, 'y':0.1}
                    font_size: '30sp'
                TextInput:
                    id: Email2
                    size_hint: 0.6, 0.7
                    pos_hint: {'center_x': 0.5, 'y':0.3}
                    multiline: False
                    font_size: '30sp'
      
            FloatLayout:
                Label:
                    text: 'Номер'
                    pos_hint: {'center_x': 0.1, 'y':0.4}
                    font_size: '30sp'
                Label:
                    text: 'лицензии'
                    pos_hint: {'center_x': 0.1, 'y':0.0}
                    font_size: 30
                TextInput:
                    id: textID_input
                    size_hint: 0.6, 0.7
                    pos_hint: {'center_x': 0.5, 'y':0.3}
                    multiline: False
                    font_size:30
                    
                    
    
        BoxLayout:
            pos_hint: 0.5, 0.1
            orientation: 'vertical'
            FloatLayout:
                Button:
                    size_hint: 0.4, 0.6
                    pos_hint: {'center_x': 0.5, 'y':0.2}
                    text: 'Зарегестрироваться'
                    font_size:30
                    on_state:
                        root.insert_text()
                    on_release:
                        root.signupbtn()
                        root.manager.transition.direction = "right"
      
        FloatLayout:
            Button:
                size_hint: 0.4, 0.6
                pos_hint: {'center_x': 0.5, 'y':0}
                text: 'Вернуться в меню Входа'
                font_size:30
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.transition.duration = 1
                    root.manager.current = 'VhodScreen'
                



<Popups>:
    size_hint: 0.4, 0.4
    BoxLayout:
        padding: 15
        spacing: 15       
        orientation: 'vertical'
        size_hint: 0.5, 0.5       
        Label:
            text:"Были введены недопустимые знаки"
            font_size: '30sp'
        Button:
            text: "Закрыть предупреждение"
            
            on_release:            
                root.dismiss()

<Katalog>:
    name: "KatalogScreen"
    BoxLayout:
        padding: 15
        spacing: 15       
        orientation: 'vertical'
        size_hint: 0.5, 0.5       
        Label:
            text:"Это меню каталога"
            font_size: '60sp'
""")

kivy.config.Config.set('graphics','resizable', False)
Window.size = (1200, 800)



class Vhod(Screen):
    def insert_text(self, *args):
        data = self.text_input.text
        if data.isnumeric():
            pass
        else:
            self.text_input.text = ''
            
            show = Popups() 
            show.open()
    
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    def validate(self):
  
        # validating if the email already exists 
        if self.email.text not in users['Email'].unique():
            Popups()
        else:
  
            # switching the current screen to display validation result
            screen_manager.current = 'KatalogScreen'
  
            # reset TextInput widget
            self.email.text = ""
            self.pwd.text = ""
    pass

class Popups(Popup):
        
    pass

class Menu(Screen):
    def insert_text(self, *args):
        data = self.text_input.text
        if data.isnumeric():
            pass
        else:
            self.text_input.text = ''
            
            show = Popups() 
            show.open()


    
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    def signupbtn(self):
  
        # creating a DataFrame of the info
        user = pd.DataFrame([[self.email.text, self.pwd.text]], columns = ['Email', 'Password'])

        if self.email.text != "":
            if self.email.text not in users['Email'].unique():
  
                # if email does not exist already then append to the csv file
                # change current screen to log in the user now 
                user.to_csv('login.csv', mode = 'a', header = False, index = False)
                screen_manager.current = 'VhodScreen'
                self.email.text = ""
                self.pwd.text = ""
    pass

class Katalog(Screen):
    
    pass

class windowManager(ScreenManager):
    pass


users=pd.read_csv('login.csv')
screen_manager = windowManager()
screen_manager.add_widget(Vhod(name ="VhodScreen"))
screen_manager.add_widget(Menu(name ="MenuScreen"))
screen_manager.add_widget(Katalog(name ="KatalogScreen"))


class MainApp(App):
    

    def build(self):        
        return screen_manager
        
 
 
 
if __name__ == "__main__":
    app = MainApp()
    app.run()