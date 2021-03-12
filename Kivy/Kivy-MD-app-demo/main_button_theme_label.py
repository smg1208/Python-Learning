from kivymd.app import MDApp
# from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class DemoApp(MDApp):    
    def build(self):
        # MDLabel, MDIcon
        # label = MDLabel(text = 'Hello, this is kivy MD App', halign = 'center', theme_text_color = 'Custom', text_color=(.06,.45,.45,1), font_style= 'Caption')
        # iconLabel = MDIcon(icon='language-python', halign='center', theme_text_color = 'Custom', text_color=(.06,.45,.45,1))
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = '500'
        self.theme_cls.theme_style  = 'Dark'
        screen = MDScreen()
        btn_flat = MDFlatButton(text = 'Hello, this is flat button!',pos_hint=({'center_x':.5,'center_y':.5}))
        btn_recflat = MDRectangleFlatButton(text = 'Hello, this is flat button!',pos_hint=({'center_x':.5,'center_y':.6}))
        btn_icon = MDIconButton(icon = 'android',pos_hint=({'center_x':.5,'center_y':.7}))
        btn_FAB = MDFloatingActionButton(icon = 'android',elevation_normal=12,pos_hint=({'center_x':.5,'center_y':.8}))
        btn_FAB_2 = MDFloatingActionButton(icon = 'android',elevation_normal=6,pos_hint=({'center_x':.5,'center_y':.9}))
        screen.add_widget(btn_flat)
        screen.add_widget(btn_recflat)        
        screen.add_widget(btn_icon)
        screen.add_widget(btn_FAB)
        screen.add_widget(btn_FAB_2)
        return screen
    
if __name__ == "__main__":
    DemoApp().run()
