from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (300, 500)

navigation_helper = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title:'Demo'
                        left_action_items:[['menu',lambda x: nav_drawer.toggle_nav_drawer()]]                        
                        elevation: 10

                    Widget:
        MDNavigationDrawer:
            id:nav_drawer

            BoxLayout:
                orientation:'vertical'
                spacing: 10
                padding: 10
                Image:
                    source:'location.png'

                MDLabel:
                    text:'Le Tuan Anh'
                    font_style:'Subtitle1'
                    size_hint_y:None
                    height:self.texture_size[1]
                MDLabel:
                    text:'Email'
                    font_style:'Caption'
                    size_hint_y:None
                    height:self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            IconLeftWidget:
                                icon: 'account'
                        OneLineIconListItem:
                            text:'Upload'
                            IconLeftWidget:
                                icon: 'file-upload'
                        OneLineIconListItem:
                            text:'Logout'
                            IconLeftWidget:
                                icon: 'logout'

"""


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
