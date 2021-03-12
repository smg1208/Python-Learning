from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (300, 500)

scr_helper = """
Screen:
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Demo'
            left_action_items:[['menu',lambda x: app.navigation_draw()]]
            right_action_items:[['clock',lambda x: app.navigation_draw()]]
            elevation: 10
        MDLabel:
            text:'Hello, welcome!'
            halign:'center'

        MDBottomAppBar:
            MDToolbar:
                title:'Python'
                left_action_items:[['language-python',lambda x: app.navigation_draw()]]                
                mode:'end'
                type:'bottom'
                icon:'language-java'
                on_action_button: app.navigation_draw()
    

"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        self.theme_cls.theme_style = 'Dark'
        scr = Builder.load_string(scr_helper)

        return scr
    def navigation_draw(self):
        print('Navigation')

if __name__ == "__main__":
    DemoApp().run()
