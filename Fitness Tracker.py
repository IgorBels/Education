import datetime as dt

FORMAT = "%H:%M:%S"
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2 or None in data:
        return False
    else:
        return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if len(storage_data) > 0 and time <= max(storage_data.keys()):
        return False
    else:
        return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    sum_steps = 0
    for i in storage_data.values():
        sum_steps += i
    step_day = sum_steps + steps
    return step_day


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    dist_day = get_step_day(steps) * STEP_M
    return dist_day / 1000


def get_spent_calories(dist1, current_time):
    """Получить значения потраченных калорий."""
    hours = current_time.hour + current_time.minute/60
    mean_speed = dist1 / hours
    spent_calories = ((K_1 * WEIGHT + (mean_speed**2 / HEIGHT)
                      * K_2 * WEIGHT) * hours * 60)
    return spent_calories


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return achievement


def show_message(current_time, day_steps_count, distance, day_calories,
                 say_achivement):
    output = (f'''
Время: {current_time}.
Количество шагов за сегодня: {day_steps_count}.
Дистанция составила{distance: .2f} км.
Вы сожгли{day_calories: .2f} ккал.
{say_achivement}
''')
    print(output)


def accept_package(data):
    """Обработать пакет данных."""

    if check_correct_data(data) is False:
        return 'Некорректный пакет'
    time, steps = data
    pack_time = dt.datetime.strptime(time, FORMAT).time()

    if check_correct_time(pack_time) is False:
        return 'Некорректное значение времени'
    day_steps = get_step_day(steps)
    dist = get_distance(steps)
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data[pack_time] = day_steps


package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
