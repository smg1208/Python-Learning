from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp

Builder.load_string(
    """
<ExampleButtons@BoxLayout>:
    orientation: "vertical"

    MDToolbar:
        id: toolbar
        title: app.title
        md_bg_color: app.theme_cls.primary_color
        background_palette: "Primary"
        elevation: 10
        left_action_items: [["dots-vertical", lambda x: None]]

    ScrollView:
        size_hint_x: None
        width: box.width
        pos_hint: {"center_x": .5}
        bar_width: 0

        BoxLayout:
            id: box
            padding: dp(10)
            size_hint: None, None
            size: self.minimum_size
            spacing: dp(10)
            orientation: "vertical"
            pos_hint: {"center_x": .5}

            BoxLayout:
                size_hint: None, None
                width: self.minimum_width
                height: dp(56)
                spacing: "10dp"

                MDIconButton:
                    icon: "sd"

                MDFloatingActionButton:
                    icon: "plus"
                    opposite_colors: True
                    elevation_normal: 8

                MDFloatingActionButton:
                    icon: "check"
                    opposite_colors: True
                    elevation_normal: 8
                    md_bg_color: app.theme_cls.primary_color

                MDIconButton:
                    icon: "sd"
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                
                MDFloatingActionButtonSpeedDial:
                    data: app.data
                    rotation_root_button: True
                    label_text_color:(.06,.45,.45,1)

            MDFlatButton:
                text: "MDFlatButton"
                pos_hint: {"center_x": .5}

            MDRaisedButton:
                text: "MDRaisedButton"
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {"center_x": .5}

            MDRectangleFlatButton:
                text: "MDRectangleFlatButton"
                pos_hint: {"center_x": .5}

            MDRectangleFlatIconButton:
                text: "MDRectangleFlatIconButton"
                icon: "language-python"
                width: dp(230)
                pos_hint: {"center_x": .5}

            MDRoundFlatButton:
                text: "MDRoundFlatButton"
                pos_hint: {"center_x": .5}

            MDRoundFlatIconButton:
                text: "MDRoundFlatIconButton"
                icon: "language-python"
                width: dp(200)
                pos_hint: {"center_x": .5}

            MDFillRoundFlatButton:
                text: "MDFillRoundFlatButton"
                pos_hint: {"center_x": .5}

            MDFillRoundFlatIconButton:
                text: "MDFillRoundFlatIconButton"
                icon: "language-python"
                pos_hint: {"center_x": .5}

            MDTextButton:
                text: "MDTextButton"
                pos_hint: {"center_x": .5}

            BoxLayout:
                orientation: "vertical"
                spacing: "10dp"
                size_hint: None, None
                size: self.minimum_size
                pos_hint: {"center_x": .5}

                MDSeparator:

                Label:
                    text: "Button customization"
                    color: app.theme_cls.text_color
                    font_size: "20sp"
                    size_hint: None, None
                    size: self.texture_size

                MDSeparator:

            ########################################
            #         CUSTOMIZATION BUTTONS
            ########################################

            MDRaisedButton:
                text: "MDRaisedButton"
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {"center_x": .5}
                text_color: 1, 0, 0, 1

            MDRaisedButton:
                text: "MDRaisedButton"
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {"center_x": .5}
                md_bg_color: 1, 0, 0, 1

            MDRectangleFlatButton:
                text: "MDRectangleFlatButton"
                pos_hint: {"center_x": .5}
                text_color: 1, 1, 0, 1

            MDRectangleFlatButton:
                text: "MDRectangleFlatButton"
                pos_hint: {"center_x": .5}
                md_bg_color: 1, 0, 0, 1
                text_color: 1, 1, 0, 1

            MDRoundFlatButton:
                text: "MDRoundFlatButton"
                pos_hint: {"center_x": .5}
                md_bg_color: 1, 0, 0, 1

            MDRoundFlatButton:
                text: "MDRoundFlatButton"
                pos_hint: {"center_x": .5}
                text_color: 1, 1, 0, 1

            MDRoundFlatButton:
                text: "MDRoundFlatButton"
                pos_hint: {"center_x": .5}
                text_color: 1, 1, 0, 1
                md_bg_color: 1, 0, 0, 1

            MDRoundFlatIconButton:
                text: "MDRoundFlatIconButton"
                pos_hint: {"center_x": .5}
                text_color: 1, 1, 0, 1
                width: dp(210)

            MDRoundFlatIconButton:
                text: "MDRoundFlatIconButton"
                pos_hint: {"center_x": .5}
                text_color: 1, 1, 0, 1
                md_bg_color: 1, 0, 0, 1
                width: dp(210)

            MDFillRoundFlatIconButton:
                text: "MDFillRoundFlatIconButton"
                icon: "language-python"
                pos_hint: {"center_x": .5}
                text_color: 1, 1, 0, 1

            MDFillRoundFlatIconButton:
                text: "MDFillRoundFlatIconButton"
                icon: "language-python"
                pos_hint: {"center_x": .5}
                text_color: 1, 1, 0, 1
                md_bg_color: 1, 0, 0, 1            
"""
)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD Examples - Buttons"
        self.theme_cls.primary_palette = "Blue"
        super().__init__(**kwargs)
    
    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }

    def build(self):
        self.root = Factory.ExampleButtons()


if __name__ == "__main__":
    MainApp().run()