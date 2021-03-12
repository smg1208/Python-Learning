from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.lang import Builder
from helper import user_helper


class DemoApp(MDApp):
    def build(self):
        scr = MDScreen()
        self.theme_cls.primary_palette = 'Green'
        btn = MDRoundFlatButton(text='Show',
                                pos_hint={'center_x': .5, 'center_y': .4},
                                on_release=self.show_data)
        self.username = Builder.load_string(user_helper)
        scr.add_widget(self.username)
        scr.add_widget(btn)
        return scr

    def show_data(self, obj):
        if self.username.text is '':
            check_string = 'Please enter username!'
        else:
            check_string = self.username.text + ' does not exist!'
        btn_close = MDFlatButton(text = 'X', on_release = self.close_dialog)
        btn_more = MDFlatButton(text = 'More')
        self.dialog = MDDialog(title='Username Check',
                          text=check_string,
                          size_hint=(.7, 1),
                          buttons=[btn_close, btn_more])
        self.dialog.open()
    
    def close_dialog(self, obj):
        self.dialog.dismiss()


if __name__ == "__main__":
    DemoApp().run()
