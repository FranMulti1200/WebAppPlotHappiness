import random
from datetime import date, time, datetime

list_quotes = []
nombreDia = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 7: 'Domingo' }

with open('quotes.txt', 'r') as quotes:
    for quote in quotes:
        list_quotes.append(quote)

today = date.today()
dayNumberToday = today.weekday()

if nombreDia[dayNumberToday] == 'Lunes':
    print(f" It´s {nombreDia[dayNumberToday]}! Time for some motivation!  \n")
    print("📜 Motivational Quote of the Day 📜 \n")
    quoterandom = random.randint(0,6)
    print(list_quotes[quoterandom])
else:
    print(f"Today is {nombreDia[dayNumberToday]}")






