from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

floatlayout = FloatLayout()


floatlayout.add_widget(Label(
    text="Edit Transcations",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x':0, 'y':.85}
))

floatlayout.add_widget(Label(
    text="Code: ",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .75}
))

floatlayout.add_widget(Label(
    text="Name:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .62}
))

floatlayout.add_widget(Label(
    text="Date:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.37, .1),
    pos_hint={'x': 0, 'y': .5}
))

floatlayout.add_widget(Label(
    text="Value:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .35}
))

floatlayout.add_widget(Label(
    text="Fixed Transcation:",
    font_name="minha_fonte.ttf",
    color=(1, 1, 1, 1),
    font_size='20sp',
    size_hint=(0.55, .1),
    pos_hint={'x': 0, 'y': .20}
))

lbl = Label(
    text="",
    font_size='20sp',
    color=(1, 1, 1, 1),
    size_hint=(0.6, .1),
    pos_hint={'x': 0, 'y': .75}
)

txt_desc = TextInput(
    multiline=False,
    size_hint=(0.6, .05),
    pos_hint={'x': .3, 'y': .65}
)

txt_value = TextInput(
    multiline=False,
    input_type='number',
    size_hint=(0.3, .05),
    pos_hint={'x': .3, 'y': .38}
)
spn_day = Spinner(
    text="Day",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .30, 'y': .53}
)

spn_month = Spinner(
    text="Month",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .47, 'y': .53}
)

spn_year = Spinner(
    text="Year",
    size_hint=(0.2, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .64, 'y': .53}
)

expense_fix = CheckBox(
    size_hint=(0.27, .04),
    pos_hint={'x': .38, 'y': .23}
)
fixed_expense = CheckBox(
    size_hint=(0.27, .04),
    pos_hint={'x': .38, 'y': .23}
)

btn_ok = Button(
    text="OK",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn_cancel = Button(
    text="Cancel",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

btn_delete = Button(
    text="Delete",
    size_hint=(0.25, .05),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .40, 'y': .777}
)

floatlayout.add_widget(lbl)
floatlayout.add_widget(txt_desc)
floatlayout.add_widget(txt_value)
floatlayout.add_widget(spn_day)
floatlayout.add_widget(spn_month)
floatlayout.add_widget(spn_year)
floatlayout.add_widget(fixed_expense)
floatlayout.add_widget(btn_ok)
floatlayout.add_widget(btn_cancel)
floatlayout.add_widget(btn_delete)
