from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button

floatlayout = FloatLayout()

floatlayout.add_widget(Label(
    text="Expense Registration",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='30sp',
    size_hint=(1, .1),
    pos_hint={'x': 0, 'y': .8}
))

floatlayout.add_widget(Label(
    text="Name:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .6}
))

floatlayout.add_widget(Label(
    text="Date:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.37, .1),
    pos_hint={'x': 0, 'y': .459}
))

floatlayout.add_widget(Label(
    text="Value:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.4, .1),
    pos_hint={'x': 0, 'y': .35}
))

floatlayout.add_widget(Label(
    text="Fixed Expense:",
    color=(1, 1, 1, 1),
    font_name="minha_fonte.ttf",
    font_size='20sp',
    size_hint=(0.55, .1),
    pos_hint={'x': 0, 'y': .20}
))

txt_desc = TextInput(
    size_hint=(0.6, .05),
    multiline=False,
    pos_hint={'x': .3, 'y': .623}
)

txt_value = TextInput(
    size_hint=(0.3, .05),
    multiline=False,
    pos_hint={'x': .3, 'y': .38},
    input_type='number'
)

spn_day = Spinner(
    text="Day",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .30, 'y': .485}
)

spn_month = Spinner(
    text="Month",
    size_hint=(0.15, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .47, 'y': .485}
)

spn_year = Spinner(
    text="Year",
    size_hint=(0.2, .04),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .64, 'y': .485}
)

expense_fix = CheckBox(
    size_hint=(0.27, .04),
    pos_hint={'x': .35, 'y': .23}
)

btn = Button(
    text="OK",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .2, 'y': .05}
)

btn1 = Button(
    text="Back",
    size_hint=(0.25, .1),
    background_color=(.5, 1.6, 3, .8),
    pos_hint={'x': .55, 'y': .05}
)

floatlayout.add_widget(txt_desc)
floatlayout.add_widget(txt_value)
floatlayout.add_widget(spn_day)
floatlayout.add_widget(spn_month)
floatlayout.add_widget(spn_year)
floatlayout.add_widget(expense_fix)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)

