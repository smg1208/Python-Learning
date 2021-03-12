
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from pymongo import MongoClient
import hashlib

Builder.load_file('signin/signin.kv')

class SigninWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def validate_user(self):
        client = MongoClient()
        db = client.silverpos
        users = db.users

        user_ip = self.ids.username_field
        passw_ip = self.ids.pass_field
        info = self.ids.info        

        username = user_ip.text
        password = passw_ip.text

        # user_ip.text = ''
        passw_ip.text = ''

        if username == '' or password =='':
            info.text = '[color=#FF0000]Username and password is required![/color]'
        else:
            user = users.find_one({'user_name':username})
            if user == None:
                info.text = '[color=#FF0000]Invalid Username or password![/color]'
            else:
                password = hashlib.sha256(password.encode()).hexdigest()
                if password ==user['password']:
                    des = user['designation']                    
                    info.text = ''
                    self.parent.parent.parent\
                        .ids.scrn_op.children[0]\
                            .ids.loggedin_user.text = username
                    if des == 'Administrator':
                        self.parent.parent.current = 'scrn_admin'
                    else:
                        self.parent.parent.current = 'scrn_op'
                else:
                    info.text = '[color=#FF0000]Invalid Username or password![/color]'

class SigninApp(App):
    def builf(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()