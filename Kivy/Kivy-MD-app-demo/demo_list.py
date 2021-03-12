from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem,ThreeLineAvatarListItem
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    def build(self):
        scr = MDScreen()
        list_view = MDList()
        scrool_view = ScrollView()
        scrool_view.add_widget(list_view)
        for r in range(20):
            image = ImageLeftWidget(source = 'location.png')
            # icon = IconLeftWidget(icon = 'language-python')
            items = ThreeLineAvatarListItem(                
                text='Item '+str(r+1),
                secondary_text='Hello line, ' + str(r+1),
                tertiary_text='Third text, ' + str(r+1)

            )
            items.add_widget(image)
            list_view.add_widget(items)

        scr.add_widget(scrool_view)
        return scr


if __name__ == "__main__":
    DemoApp().run()
