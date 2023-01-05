# Задача 2. Скелетон
# Българският състезател по скелетон Марин Бангиев се бори за олимпийска квота. Вие имате честта да напишете програмата,
# която ще изчисли дали той печели квота.
# Вашата програма получава контролата в минути, която трябва да бъде достигната или подобрена, за да може
# Марин да вземе квота. Също така програмата ще получи разстоянието на улея в метри, и времето в секунди,
# за което той изминава 100 метра.
# Трябва да се има предвид, че поради наклона на улея, на всеки 120 метра неговото време намаля с 2.5 секунди.
# Вход
# От конзолата се четат 4 реда:
# Ред 1.	Минути на контролата – цяло число в интервала [0…59]
# Ред 2.	Секунди на контролата – цяло число в интервала [0…59]
# Ред 3.	Дължината на улея в метри – реално число в интервала [0.00…50000]
# Ред 4.	Секунди за изминаване на 100 метра – цяло число в интервала [0…1000]
# Изход
# На конзолата трябва да се отпечата на един или два реда:
# •	Ако времето на Марин е по-малко или равно на контролата:
# o	"Marin Bangiev won an Olympic quota!"
# o	"His time is {времето на Марин в секунди}."
# •	Ако времето на Марин е повече от това на контролата:
# o	 "No, Marin failed! He was {недостигащи секунди} second slower."
# Резултатът трябва да е форматиран до третия знак след десетичния знак.
minutes_of_controls = int(input())
seconds_for_controls = int(input())
length_of_ul = float(input())
seconds_for_100_metres = int(input())
control_for_secs = minutes_of_controls * 60 + seconds_for_controls
Marins_time = (length_of_ul / 100) * seconds_for_100_metres - length_of_ul / 120 * 2.5
if Marins_time <= control_for_secs:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {Marins_time:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(Marins_time - control_for_secs):.3f} second slower.")