from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager


navigation_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name:'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint:{'center_x':.5, 'center_y':.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload a photo'
        pos_hint:{'center_x':.5, 'center_y':.4}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name:'profile'
    MDLabel:
        text:'Welcome, devs'
        halign:'center'
    MDRectangleFlatButton:
        text: 'Back to Menu'
        pos_hint:{'center_x':.5, 'center_y':.4}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name:'upload'
    MDLabel:
        text:'Select a photo'
        halign:'center'
    MDRectangleFlatButton:
        text: 'Back to Menu'
        pos_hint:{'center_x':.5, 'center_y':.4}
        on_press: root.manager.current = 'menu'
    
"""
class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'
        scr = Builder.load_string(navigation_helper)

        return scr

    def navigation_draw(self):
        print('Navigation')

        

    

if __name__ == "__main__":
    DemoApp().run()
