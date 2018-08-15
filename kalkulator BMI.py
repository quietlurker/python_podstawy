# -*- coding: utf-8 -*-

print("Kalculator BMI\n Podaj swój wzrost w metrach:")
wzrost = float(input())

print("Podaj swoją wagę w kilogramach:")
waga = float(input())

print("Twoje BMI wynosi", round(waga / (wzrost **2),4))
#let's not use round. it doesn't round rumbers - it rounds the displayed number (think trim)
