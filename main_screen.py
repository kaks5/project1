from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


boxlayout = BoxLayout(
    orientation="vertical",
    spacing=20,
    padding=50,
    )

lbl_balance = Label(
    text="Current Balance: ",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(1, .05)
    )

lbl_total = Label(
    text="Total Expenses: ",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(1, .05)
    )

lbl_largest = Label(
    text="largest_expense: UGX 0",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(1, .05)
    )

btn_add_funds = Button(
    text="Add Funds",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_new_expense = Button(
    text="New Expense",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

btn_movements = Button(
    text="View Transcations",
    size_hint=(1, .1),
    background_color=(.5, 1.6, 3, .8)
    )

boxlayout.add_widget(lbl_balance)
boxlayout.add_widget(lbl_total)
boxlayout.add_widget(lbl_largest)
boxlayout.add_widget(btn_add_funds)
boxlayout.add_widget(btn_new_expense)
boxlayout.add_widget(btn_movements)