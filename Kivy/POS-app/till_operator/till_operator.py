import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

import re
from pymongo import MongoClient

Builder.load_file('till_operator/operator.kv')

class OperatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        client = MongoClient()
        self.db = client.silverpos
        self.stocks = self.db.stocks

        self.cart = []
        self.qty = []
        self.total = 0.00
    
    def logout(self):
        self.parent.parent.current = 'scrn_si'


    def update_purchase(self):
        pcode = self.ids.code_input.text
        product_container = self.ids.products

        target_code = self.stocks.find_one({'product_code':pcode})
        if target_code == None:
            pass
        else:        
            details = BoxLayout(size_hint_y=None, height=30,pos_hint={'top': 1})
            product_container.add_widget(details)

            code = Label(text=pcode, size_hint_x=0.2, color=(0.06, 0.45, 0.45, 1))
            name = Label(text=target_code['product_name'], size_hint_x=0.3,color=(0.06, 0.45, 0.45, 1))
            qty = Label(text='1', size_hint_x=0.1, color=(0.06, 0.45, 0.45, 1))
            disc = Label(text='0.00', size_hint_x=0.1,color=(0.06, 0.45, 0.45, 1))
            price = Label(text=str(target_code['product_price']), size_hint_x=0.1,color=(0.06, 0.45, 0.45, 1))
            total = Label(text='0.00', size_hint_x=0.2,color=(0.06, 0.45, 0.45, 1))
            details.add_widget(code)
            details.add_widget(name)
            details.add_widget(qty)
            details.add_widget(disc)
            details.add_widget(price)
            details.add_widget(total)

            # update Preview:
            pname = target_code['product_name']
            
            pprice = float(price.text)
            pqty = str(1)
            self.total += pprice
            purchase_total = '`\n\nTotal\t\t\t\t\t' + str(self.total)
            self.ids.cur_product.text = pname
            self.ids.cur_price.text = str(pprice)
            preview = self.ids.receipt_preview
            prev_text = preview.text
            _prev = prev_text.find('`')
            if _prev > 0:
                prev_text = prev_text[:_prev]

            ptarget = -1
            for i,c in enumerate(self.cart):
                if c == pcode:
                    ptarget = i
            if ptarget >=0:
                # print('-------------------')
                pqty = self.qty[ptarget]+1
                self.qty[ptarget] = pqty
                expr = '%s\tx\d\t'%(pname)
                # print(expr)
                rexpr = pname+'\tx'+str(pqty)+'\t'
                # print(rexpr)
                # print(prev_text)
                new_text = re.sub(expr, rexpr, prev_text)
                # print(new_text)
                preview.text = new_text + purchase_total
            else:
                self.cart.append(pcode)
                self.qty.append(1)
                new_preview='\n'.join([prev_text,pname+'\tx'+pqty+'\t'+str(pprice),purchase_total])
                preview.text = new_preview
            self.ids.disc_input.text = '0.00'
            self.ids.disc_perc_input.text = '0'
            self.ids.qty_input.text =str(pqty)
            self.ids.price_input.text =str(pprice)
            self.ids.VAT_input.text = '10%'
            self.ids.total_input.text = str(pprice*float(pqty))
            

class OperatorApp(App):
    def build(self):
        return OperatorWindow()


if __name__ == "__main__":
    oa = OperatorApp()
    oa.run()
