# Напишете програма, която отпечатва часовете в денонощието от 0:0 до 23:59, всеки на отделен ред.
# Часовете трябва да се изписват във формат "{час} : {минути}".
for hours in range(0 , 24):
    for minutes in range(0 , 60):
        print(f'{hours} : {minutes}')

