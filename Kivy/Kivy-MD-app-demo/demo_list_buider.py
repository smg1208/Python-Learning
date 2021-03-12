from kivy.lang import Builder
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


KV = '''
<ListItemWithCheckbox>:

    IconLeftWidget:
        icon: root.icon

    RightCheckbox:


BoxLayout:

    ScrollView:

        MDList:
            id: scroll
'''


class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons = list(md_icons.keys())        
        print(len(icons))
        for i in range(len(icons)):
            if icons[i].count('language') != 0:
                self.root.ids.scroll.add_widget(
                    ListItemWithCheckbox(text=icons[i], icon=icons[i])
                )


if __name__ == "__main__":
    DemoApp().run()
