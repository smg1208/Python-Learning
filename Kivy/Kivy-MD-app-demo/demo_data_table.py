from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable

from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        scr = MDScreen()
        table = MDDataTable(
            pos_hint=({'center_x': .5, 'center_y': .5}),
            size_hint=(.9, .6),
            check= True,
            rows_num=15,
            column_data=[
                ('No.', dp(20)),
                ('Food', dp(20)),
                ('Calories', dp(20)),
                ('Price', dp(20)),
            ],
            row_data=[
                ('1', 'Burger', '300', '0.00'),
                ('2', 'Meat', '300', '0.00'),
                ('3', 'Meat', '300', '0.00'),
                ('4', 'Meat', '300', '0.00'),
                ('5', 'Meat', '300', '0.00'),
                ('6', 'Meat', '300', '0.00'),
                ('7', 'Meat', '300', '0.00'),
                ('8', 'Meat', '300', '0.00'),
                ('9', 'Meat', '300', '0.00'),
                ('10', 'Meat', '300', '0.00'),
                ('11', 'Meat', '300', '0.00'),
                ('12', 'Meat', '300', '0.00'),
                ('13', 'Meat', '300', '0.00'),
            ])

        table.bind(on_check_press = self.check_press)
        table.bind(on_row_press = self.row_press)
        scr.add_widget(table)

        return scr
    
    def check_press(self, instance_table, current_row):
        print(instance_table, current_row)
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)
        


if __name__ == "__main__":
    DemoApp().run()
