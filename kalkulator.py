#!/usr/bin/env python3

def dodawanie(a, b):
	return a + b

def odejmowanie(a, b):
	return a - b

def mnozenie(a, b):
	return a * b

def dzielenie(a, b):
	if b == 0:
		return "Nie dziel przez zero!!!"
	return a / b

def kalkulator():
	print("Kalkulator")
	print("1. Dodawanie")
	print("2. Odejmowanie")
	print("3. Mnozenie")
	print("4. Dzielenie")

	wybor = input("Wybierz co chcesz zrobic: ")
	
	if wybor in ['1', '2', '3', '4']:
		liczba1 = float(input("Podaj pierwsza liczbe: "))
		liczba2 = float(input("Podaj druga liczbe: "))
		
		if wybor == '1':
			print(f"Wynik: {dodawanie(liczba1, liczba2)}")
		elif wybor == '2':
			print(f"Wynik: {odejmowanie(liczba1, liczba2)}")
		elif wybor == '3':
			print(f"Wynik: {odejmowanie(liczba1, liczba2)}")
		elif wybor == '4':
			print(f"Wynik: {dzielenie(liczba1, liczba2)}")
	else:
		print("zly wybor")
kalkulator()
