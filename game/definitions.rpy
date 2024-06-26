# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Person(name="Mimoň", color="#fe0303", gender="m")
define s = Person(name="Sučan", color="#0303fe", gender="m")
define a = Person(name="Adrian", color="#03e221", gender="m")
define d = Person(name="Dante", color="#545454", gender="m")
define h = Person(name="Hana", color="#545454", gender="f")
define j = Person(name='[name]', color="#f4f803", gender=None)

# Only "default" objects are saved
default m = m
default s = s
default a = a
default d = d
default h = h
default j = j
