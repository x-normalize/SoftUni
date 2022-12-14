# Задачата ви е да напишете програма, която приема името на отбор и прави статистика за него. През един сезон всеки отбор изиграва определен брой футболни срещи, като за всяка среща на отбора се дават точки в зависимост от изхода от срещата. Има три възможни изхода от една среща:
# 	W - Отборът е победител и получава 3 точки
# 	D - Срещата е завършила без победител и отборът получава 1 точка
# 	L - Отборът е загубил срещата и не получава точки
# Напишете програма, която приема името на футболен отбор и извежда неговата статистика, на база на изиграните срещи през този сезон. Неговата статистика трябва да включва общия брой спечелени точки през настоящия сезон, подробна статистика за изхода на изиграните игри и процент победи през сезона. Ако отборът по някаква причина не е играл мачове през настоящия сезон се извежда специално съобщение.
# Вход
# От конзолата се четат два реда:
# •	Името на футболния отбор, за който водим статистика - текст
# •	Броя изиграни срещи през настоящия сезон - цяло число в интервала [0… 100]
#  За всяка изиграна среща се прочита отделен ред:
# o	Резултатът от изиграната среща в един от горепосочените формати – символ с възможности 'W', 'D' и 'L'
# Изход
# В зависимост от това дали отборът е играл мачове през настоящия сезон се извеждат два вида изход.
# •	Ако отборът не е изиграл нито един мач през настоящия сезон се извежда точно един ред в следния формат:
# o	"{името на отбора} hasn't played any games during this season."
# •	Ако отборът е изиграл един мач или повече се извеждат шест реда в следния формат:
# o	"{името на отбора} has won {брой спечелени точки} points during this season"
# o	"Total stats:"
# o	"## W: {брой спечелени игри}"
# o	"## D: {брой игри, завършили наравно}"
# o	"## L: {брой загубени игри}"
# o	"Win rate: {процент спечелени игри}%"
# Процентът спечелени игри трябва да бъде форматиран до втората цифра след десетичния знак.
team = input()
count_of_battles = int(input())
win = 0
draw = 0
lose = 0
points = 0
all_plays = 0
for c in range(1 ,  count_of_battles + 1):
    all_plays += 1
    state = input()
    if state == "W":
        points += 3
        win += 1
    elif state == "D":
        points += 1
        draw += 1
    elif state == "L":
        lose += 1
if all_plays == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    print(f"{team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {win}")
    print(f"## D: {draw}" )
    print(f"## L: {lose}" )
    print(f"Win rate: {(win / all_plays * 100):.2f}%")