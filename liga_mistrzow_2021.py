sklad_manchester_city = [
    ["Numer", "Zawodnik", "Pozycja"],
    ["31", "Ederson", "Bramkarz"],
    ["2", "Kyle Walker", "Obrońca"],
    ["3", "Ruben Dias", "Obrońca"],
    ["14", "Aymeric Laporte", "Obrońca"],
    ["22", "Benjamin Mendy", "Obrońca"],
    ["16", "Rodri", "Pomocnik"],
    ["17", "Kevin De Bruyne", "Pomocnik"],
    ["8", "Ilkay Gündogan", "Pomocnik"],
    ["20", "Bernardo Silva", "Pomocnik"],
    ["26", "Riyad Mahrez", "Napastnik"],
    ["7", "Raheem Sterling", "Napastnik"]
]

sklad_chelsea = [
    ["Numer", "Zawodnik", "Pozycja"],
    ["16", "Edouard Mendy", "Bramkarz"],
    ["28", "César Azpilicueta", "Obrońca"],
    ["2", "Antonio Rüdiger", "Obrońca"],
    ["6", "Thiago Silva", "Obrońca"],
    ["21", "Ben Chilwell", "Obrońca"],
    ["7", "N'Golo Kanté", "Pomocnik"],
    ["17", "Mateo Kovačić", "Pomocnik"],
    ["19", "Mason Mount", "Pomocnik"],
    ["22", "Christian Pulisic", "Pomocnik"],
    ["29", "Kai Havertz", "Napastnik"],
    ["11", "Timo Werner", "Napastnik"]
]

# Wypisanie składu Chelsea
for pozycja in sklad_chelsea:
    print("{:<5} {:<20} {:<10}".format(pozycja[0], pozycja[1], pozycja[2]))



# Wypisanie składu Manchesteru City
for pozycja in sklad_manchester_city:
    print("{:<5} {:<20} {:<10}".format(pozycja[0], pozycja[1], pozycja[2]))
    
wynik_meczu = "Manchester City 0-1 Chelsea"

print()

# Wypisanie wyniku meczu
print("Wynik meczu:")
print(wynik_meczu)