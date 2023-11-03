from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import database_functions as fb
import new_name_screen as tnn
import new_value_screen as tnv
import main_screen as tp
import add_expense_screen as tcg
import view_expenses_screen as tcgs
import add_funds_screen as taf
import edit_expense_screen as teg
from functools import partial
import random
import os
Window.size =(350,600)

def go_new_value(self):
    if tnn.txt1.text == "":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        sm.switch_to(new_value, direction="left")


def go_new_expense(self):
    sm.switch_to(new_expense, direction="left")


def go_add_funds(self):
    sm.switch_to(add_funds, direction="left")


def go_main_screen(self):
    carry_main_screen()
    sm.switch_to(main_screen, direction="right")


def go_view_expenses(self):
    carry_view_expenses_screen()
    sm.switch_to(view_Expenses_screen, direction="left")


def go_new_name(self):
    sm.switch_to(new_name, direction="right")



def carry_main_screen():
    
    result = fb.check_balance()
    balance = result["balance"]
    total_expenses = 0
    try:
        largest_expense = result["largest_expense"]
    except:
        pass
    try:
        if balance.is_integer() is False:
            balance = round(balance, 2)
            balance = str(balance)
            if len(balance) == 5:
                balance = balance.replace(".", ",")
                balance = "UGX" + balance + ""
            else:
                balance = balance.replace(".", ",")
                balance= "UGX " + balance
        else:
            balance = int(balance)
            balance= "UGX " + str(balance) + ""
    except:
        balance = "UGX " + str(balance) + ""

    for i in result["total_expense"]:
        total_expenses = total_expenses + float(i)

    try:
        if total_expenses.is_integer() is False:
            total_expenses = round(total_expenses, 2)
            total_expenses = str(total_expenses)
            if len(total_expenses) == 5:
                total_expenses = total_expenses.replace(".", ",")
                total_expenses = "UGX " + total_expenses + ""
            elif len(total_expenses) == 1:
                total_expenses = "UGX "
            else:
                total_expenses = total_expenses.replace(".", ",")
                total_expenses = "UGX " + total_expenses
        else:
            total_expenses = int(total_expenses)
            total_expenses = "UGX" + str(total_expenses) + ""
    except:
        total_expenses = "UGX " + str(total_expenses) + ""

    try:
        if largest_expense.is_integer() is False:
            largest_expense = str(largest_expense)
            if len(largest_expense) == 5:
                largest_expense = largest_expense.replace(".", ",")
                largest_expense = "UGX " + largest_expense + ""
            else:
                largest_expense = largest_expense.replace(".", ",")
                largest_expense = "UGX " + largest_expense
        else:
            largest_expense = int(largest_expense)
            largest_expense = "UGX " + str(largest_expense) + ""
    except:
        largest_expense = "UGX "

    tp.lbl_balance.text = "Current balance: " + str(balance)
    tp.lbl_total.text = "Total Expense: " + str(total_expenses)
    tp.lbl_largest.text = "Largest Expense: " + str(largest_expense)


def carry_view_expenses_screen():
    tcgs.gridlayout.clear_widgets()
    movements = fb.check_movements()
    if movements == []:
        tcgs.gridlayout.add_widget(Label(text="No transaction found!", font_size="20sp",
                                         color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movements:
            value = j[2]
            try:
                if value.is_integer() is True:
                    value = int(value)
                    value = str(value) + ""
            except:
                value = str(value) + ""
            if j[4] == "f":
                buttons.append(
                    Button(text="Code: " + str(j[0]) + "\n" + "Name: " + j[1] + "\n" + "Value: UGX +" + str(value) + "\n"
                                + "Data: " + j[3], background_color=(0, 1, 0, 1), size_hint_y=None, height=200))
            else:
                buttons.append(
                    Button(text="Code: " + str(j[0]) + "\n" + "Name: " + j[1] + "\n" + "Value: UGX -" + str(value) + "\n"
                                + "Data: " + j[3], background_color=(1, 0, 0, 1), size_hint_y=None, height=200))
            buttons[movements.index(j)].bind(on_press=partial(fill_edit_form, j))
            tcgs.gridlayout.add_widget(buttons[movements.index(j)])
            tcgs.gridlayout.add_widget(Label(text="\n", size_hint_y=None, height=1))


def clear_edit_expense(self):
    popup4.dismiss()
    go_main_screen(self)


def fill_edit_form(self, j,):
    j = str(j.text)
    sm.switch_to(edit_expense)
    j = j.split('\n')
    j = j[0].split(": ")
    j = j[1]
    j = fb.select_and_fill_edit(j)
    j = j[0]
    teg.lbl.text = str(j[0])
    teg.txt_desc.text = j[1]
    teg.txt_value.text = str(j[2])
    teg.spn_day.values = list_day
    teg.spn_month.values = list_month
    teg.spn_year.values = list_year
    if j[4] == "1":
        teg.expense_fix.active = True
    else:
        teg.expense_fix.active = False

class YourClassName:
    def delete_expense(self):
        rowid = teg.lbl.text
        fb.delete_expense(rowid)
        popup5.open()
        Clock.schedule_once(self.clear_delete_expense, 1.5)

    def clear_delete_expense(self, dt):
        
        pass
    def bind_delete_expense(self):
        teg.btn_delete.bind(on_press=self.delete_expense)


def update_expense(self,*args):
    rowid = teg.lbl.text
    name = teg.txt_desc.text
    value = teg.txt_value.text
    day = teg.spn_day.text
    month = teg.spn_month.text
    year = teg.spn_year.text
    expense_fix = teg.expense_fix.active
    if name == "" or value == "" or day == "Day" or month == "Month " or year == "year":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        value = value.replace('-', '')
        month = list_month.index(month)
        month = month + 1
        if month < 10:
            month = '0' + str(month)
        data = str(day) + "/" + str(month) + "/" + str(year)
        if expense_fix is False:
            expense_fix = 0
        else:
            expense_fix = 1
        fb.edit_expense(rowid, name, value, data, expense_fix)
        popup4.open()
        Clock.schedule_once(clear_edit_expense, 1.5)


def search_movements(self):
    tcgs.gridlayout.clear_widgets()
    movements = str(tcgs.txt_search.text)
    movements = fb.search_movements(movements)
    if movements == []:
        tcgs.gridlayout.add_widget(Label(text="No transaction found!", font_size="20sp",
                                         color=(1, 1, 1, 1), size_hint_y=None, height=25))
    else:
        buttons = []

        for j in movements:
            value = j[2]
            try:
                if value.is_integer() is True:
                    value = int(value)
                    value = str(value) + ""
            except:
                value = str(value) + ""
            if j[4] == "f":
                buttons.append(
                    Button(text="Code: " + str(j[0]) + "\n" + "Name: " + j[1] + "\n" + "Value: UGX +" + value + "\n"
                                + "Data: " + j[3], background_color=(0, 1, 0, 1), size_hint_y=None, height=200))
            else:
                buttons.append(
                    Button(text="Code: " + str(j[0]) + "\n" + "Name: " + j[1] + "\n" + "Value: UGX -" + value + "\n"
                                + "Data: " + j[3], background_color=(1, 0, 0, 1), size_hint_y=None, height=200))

            buttons[movements.index(j)].bind(on_press=partial(fill_edit_form, j))
            tcgs.gridlayout.add_widget(buttons[movements.index(j)])
            tcgs.gridlayout.add_widget(Label(text="\n", size_hint_y=None, height=1))


def update_bar(self):
    rand = random.randint(0, 20)
    pb.value = pb.value + rand


def update():
    Clock.schedule_interval(update_bar, 0.2)


def wait_screen(self):
    popup1.dismiss()
    go_main_screen(self)


def clear_new_expense(self):
    popup2.dismiss()
    tcg.txt_desc.text = ""
    tcg.txt_value.text = ""
    tcg.spn_day.values = ""
    tcg.spn_day.values = list_day
    tcg.spn_month.values = ""
    tcg.spn_month.values = list_month
    tcg.spn_year.values = ""
    tcg.spn_year.values = list_year
    tcg.expense_fix.active = False


def clear_add_funds(self):
    popup3.dismiss()
    taf.txt_name.text = ""
    taf.txt_value.text = ""
    taf.spn_day.values = list_day
    taf.spn_month.values = list_month
    taf.spn_year.values = list_year


def clear_delete_expense(self):
    rowid = teg.lbl.text
    fb.delete_expense(rowid)
    popup5.dismiss()
    carry_main_screen()
    sm.switch_to(main_screen, direction="right")


def insert_user(self):
    if tnv.txt1.text == "":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        name = tnn.txt1.text
        value = tnv.txt1.text
        fb.insert_user(name, value)
        popup1.open()
        for i in range(5):
            update()
        Clock.schedule_once(wait_screen, 1.5)


def insert_expenses(self):
    name = tcg.txt_desc.text
    value = tcg.txt_value.text
    day = tcg.spn_day.text
    month = tcg.spn_month.text
    year = tcg.spn_year.text
    expense_fix = tcg.expense_fix.active
    if name == "" or value == "" or day == "Day" or month == "Month" or year == "year":
        popup_gen.open()
        Clock.schedule_once(popup_gen.dismiss, 1.5)
    else:
        value = value.replace('-', '')
        month = list_month.index(month)
        month = month + 1
        if month < 10:
            month = '0' + str(month)
        date = f"{day}/{month}/{year}"
        if expense_fix is False:
            expense_fix = 0
        else:
            expense_fix= 1
        fb.insert_expense(name, value, date, expense_fix)
        popup2.open()
        Clock.schedule_once(clear_new_expense, 1.5)
        tcg.spn_day.text = "Day"
        tcg.spn_month.text = "Month"
        tcg.spn_year.text = "Year"
        
def add_funds_immediately  (self):
    name = taf.txt_name.text
    value = taf.txt_value.text
    day = taf.spn_day.text
    month = taf.spn_month.text
    year = taf.spn_year.text
    
    print(f"Month value: {month}")
    print(f"List of months: {list_month}")
    
    value = value.replace('-', '')
    
    if month not in list_month:
        print(f"Invalid month: {month}")
        return
    
    month_index = list_month.index(month) + 1
    
    if month_index < 10:
        month_index = '0' + str(month_index)
    
    data = day + "/" + str(month_index) + "/" + year
    fb.add_funds(name, value, data)

    taf.txt_name.text = ""
    taf.txt_value.text = ""
    taf.spn_day.text = "Day"
    taf.spn_month.text = "Month"
    taf.spn_year.text = "Year"


    popup3.open()
    


list_day = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15",
            "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
list_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
list_year = []
for i in range(1900, 2029):
    list_year.append(str(i))
list_year.reverse()

sm = ScreenManager()

popup1 = Popup(title='Loading...', size_hint=(.6, .4))
pb = ProgressBar(value=0, max=100)
popup1.add_widget(pb)

popup2 = Popup(title='Alert!', content=Label(text="Expense inserted\n successfully!"), size_hint=(.5, .2))
popup3 = Popup(title='Alert!', content=Label(text="Funds added\n successfully!"), size_hint=(.5, .2))
popup4 = Popup(title='Alert!', content=Label(text="All set! :)"), size_hint=(.5, .2))
popup5 = Popup(title='Alert!', content=Label(text="Movement deleted\n successfully! :)"), size_hint=(.5, .2))
popup_gen = Popup(title='Alert!', content=Label(text="Fields cannot be empty!"), size_hint=(.5, .2))


new_name = Screen(name="new_name")
new_name.add_widget(tnn.floatlayout)
tnn.btn.bind(on_press=go_new_value)


new_value = Screen(name="new_value")
new_value.add_widget(tnv.floatlayout)
tnv.btn.bind(on_press=insert_user)
tnv.btn1.bind(on_press=go_new_name)

    
main_screen = Screen(name="main_screen")
main_screen.add_widget(tp.boxlayout)
tp.btn_add_funds.bind(on_press=go_add_funds)
tp.btn_new_expense.bind(on_press=go_new_expense)
tp.btn_movements.bind(on_press=go_view_expenses)




add_funds = Screen(name="add_funds")
add_funds.add_widget(taf.floatlayout)
taf.spn_day.values = list_day
taf.spn_month.values = list_month
taf.spn_year.values = list_year
taf.btn.bind(on_press=add_funds_immediately)
taf.btn1.bind(on_press=go_main_screen)


new_expense = Screen(name='new_expense')
new_expense.add_widget(tcg.floatlayout)
tcg.spn_day.values = list_day
tcg.spn_month.values = list_month
tcg.spn_year.values = list_year
tcg.btn.bind(on_press=insert_expenses)
tcg.btn1.bind(on_press=go_main_screen)


view_Expenses_screen = Screen(name='view_expense')
view_Expenses_screen.add_widget(tcgs.floatlayout)
tcgs.btn_search.bind(on_press=search_movements)
tcgs.btn_back.bind(on_press=go_main_screen)

edit_expense = Screen(name='edit_expense')
edit_expense.add_widget(teg.floatlayout)
teg.btn_ok.bind(on_press=update_expense)
teg.btn_cancel.bind(on_press=go_main_screen)
teg.btn_delete.bind(on_press=clear_delete_expense)


if os.path.exists("database.db") is False:
    fb.create_database()
    sm.add_widget(new_name)
else:
    sm.add_widget(main_screen)
    carry_main_screen()


class HelloApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 0)
        return sm


if __name__ == '__main__':
    HelloApp().run()
