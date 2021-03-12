from kivymd.app import MDApp
from kivymd.uix.label import MDLab, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

class DemoApp(MDApp):
    # def build(self):
    #     label = MDLabel(text='Hello world, Python', halign='center',
    #                     theme_text_color='Custom', text_color=(236/255.0, 98/255.0, 81/255.0, 1),
    #                     font_style='Caption')
    #     icon_label = MDIcon(icon='hinduism',halign='center')
    #     return icon_label

    def build(self):
        screen = Screen()
        btn_flat = MDRectangleFlatButton(text='Hello world', pos_hint={
                                         'center_x': 0.5, 'center_y': 0.5})
        icon_btn = MDFloatingActionButton(icon='android', pos_hint={
                                          'center_x': 0.5, 'center_y': 0.4})
        screen.add_widget(btn_flat)
        screen.add_widget(icon_btn)
        return screen


DemoApp().run()
