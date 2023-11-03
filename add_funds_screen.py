from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout


floatlayout = FloatLayout()

floatlayout.add_widget(Label(
    text="Add Funds",
    font_size="28sp",
    size_hint=(1, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .8}
))

floatlayout.add_widget(Label(
    text="Name: ",
    font_size="20sp",
    size_hint=(.4, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .62}
))

floatlayout.add_widget(Label(
    text="Date:",
    font_size="20sp",
    size_hint=(.4, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .5}
))

floatlayout.add_widget(Label(
    text="Value:",
    font_size="20sp",
    size_hint=(.4, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .35}
))

floatlayout.add_widget(Label(
    text="Fixed Income:",
    font_size="20sp",
    size_hint=(.5, .1),
    color=(1, 1, 1, 1),
    pos_hint={'x': 0, 'y': .20}
))

txt_name = TextInput(
    multiline=False,
    size_hint=(0.6, .05),
    pos_hint={'x': .3, 'y': .65}
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
    pos_hint={'x': .63, 'y': .53}
)

txt_value = TextInput(
    multiline=False,
    input_type='number',
    size_hint=(0.3, .05),
    pos_hint={'x': .3, 'y': .38}
)

fixed_income = CheckBox(
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

floatlayout.add_widget(txt_name)
floatlayout.add_widget(txt_value)
floatlayout.add_widget(spn_day)
floatlayout.add_widget(spn_month)
floatlayout.add_widget(spn_year)
floatlayout.add_widget(fixed_income)
floatlayout.add_widget(btn)
floatlayout.add_widget(btn1)
