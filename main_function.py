from typing import List, Any


def delivery_cost_calculation(distance: float | int, dimensions: str, fragile: bool, workload: str) -> str | int:
    '''
    Функция расчета стоимости доставки

    Аргументы:
    -distance (float): расстояние до пункта назначения.
    -dimensions (str):  габариты груза.
    -fragile (bool):  информацию о хрупкости груза.
    -workload (str): загруженность службы на текущий момент.

    :return:
    -float: стоимость доставки
    '''

    # Словарь для хранения соответствий стоимости доставки от расстояния до пункта назначения
    distance_dict = {
        (0, 2): 50,
        (2.1, 10): 100,
        (10.1, 30): 200,
        (30.1, float('inf')): 300
    }

    # Словарь для хранения соответствий стоимости доставки от габаритов груза
    dimensions_dict = {
        "big": 200,
        "small": 100
    }

    # Словарь для хранения соответствий стоимости доставки от загруженности службы доставки
    workload_dict = {
        "very high": 1.6,
        "high": 1.4,
        "increased": 1.2,
        "normal": 1

    }

    # Базовая стоимость доставки
    price_delivery = 0

    # Проверка на типы данных
    if not isinstance(distance, (float, int)):
        return "Расстояния до пункта назначения может быть только целочисленное или число с плавающей точкой"
    if dimensions not in dimensions_dict:
        return "Габариты груза могут принимать только значения: big, small "
    if not isinstance(fragile, bool):
        return "Информацию о хрупкости груза может принимать только булевы значения"
    if workload not in workload_dict:
        return "Информацию о загруженности службы доставки может принимать только значения: " \
               "very high, high, increased, normal"
    if distance == 0:
        return "Расстояния до пункта назначения не может быть равно нулю"

    # Расчет стоимости в зависимости от расстояния до пункта назначения
    for (min_dist, max_dist), price in distance_dict.items():
        if min_dist <= distance <= max_dist:
            price_delivery += price
            break

    # Расчет стоимости в зависимости от габаритов груза
    price_delivery += dimensions_dict.get(dimensions, 0)

    # Расчет стоимости в зависимости от хрупкости груза
    if fragile and 0 <= distance <= 30:
        price_delivery += 300
    elif fragile and distance > 30:
        return "Хрупкие грузы нельзя возить на расстояние более 30 км."

    # Расчет стоимости в зависимости от загруженности службы доставки
    price_delivery *= workload_dict.get(workload, 1.0)

    # Проверка на min стоимость доставки
    price_delivery = max(price_delivery, 400.0)

    return price_delivery
