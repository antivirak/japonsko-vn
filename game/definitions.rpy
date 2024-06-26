# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Person(name="Mimoň", name_2p="Mimoně", name_4p="Mimoně", name_5p="Mimoni", color="#fe0303", gender="m")
define s = Person(name="Sučan", name_2p="Sučana", name_4p="Sučana", name_5p="Sučane", color="#0303fe", gender="m")
define a = Person(name="Adrian", name_2p="Adriana", name_4p="Adriana", name_5p="Adriane", color="#03e221", gender="m")
define d = Person(name="Dante", name_2p="Danteho", name_4p="Danteho", name_5p="Dante", color="#545454", gender="m")
define h = Person(name="Hana", name_2p="Hany", name_4p="Hanu", name_5p="Hano", color="#545454", gender="f")
define j = Person(name='[name]', color="#f4f803", gender=None)

# Only "default" objects are saved
default m = m
default s = s
default a = a
default d = d
default h = h
default j = j
