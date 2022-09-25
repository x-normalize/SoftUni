# 4.	Задължителна литература
# За лятната ваканция в списъка със задължителна литература на Жоро има определен брой книги. Понеже Жоро предпочита да
# играе с приятели навън,
# вашата задача е да му помогнете да изчисли колко часа на ден трябва да отделя, за да прочете необходимата литература.
# Вход
# От конзолата се четат 3 реда:
# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
# Изход
# Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.


number_of_pages = int(input())
pages_for_hour = int(input())
number_of_days = int(input())

time_for_read_the_book = number_of_pages // pages_for_hour
hour_for_day_to_finish = time_for_read_the_book // number_of_days

print(hour_for_day_to_finish)