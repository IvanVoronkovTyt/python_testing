import pytest

from main_function import delivery_cost_calculation


# Основные тесты для расчета стоимости доставки
def test_1():
    summ = delivery_cost_calculation(0.1, "big", True, "very high")
    assert summ == 880.0, f"Сумма равна {summ}, а не 880.0"


def test_2():
    summ = delivery_cost_calculation(1.9, "small", True, "very high")
    assert summ == 720.0, f"Сумма равна {summ}, а не 720.0"


def test_3():
    summ = delivery_cost_calculation(2.0, "small", True, "high")
    assert summ == 630.0, f"Сумма равна {summ}, а не 630.0"


def test_4():
    summ = delivery_cost_calculation(2.1, "big", False, "high")
    assert summ == 420.0, f"Сумма равна {summ}, а не 420.0"


def test_5():
    summ = delivery_cost_calculation(9.9, "small", True, "increased")
    assert summ == 600.0, f"Сумма равна {summ}, а не 600.0"


def test_6():
    summ = delivery_cost_calculation(10.0, "big", True, "normal")
    assert summ == 600.0, f"Сумма равна {summ}, а не 600.0"


def test_7():
    summ = delivery_cost_calculation(10.1, "big", False, "very high")
    assert summ == 640.0, f"Сумма равна {summ}, а не 640.0"


def test_8():
    summ = delivery_cost_calculation(29.9, "small", True, "very high")
    assert summ == 960.0, f"Сумма равна {summ}, а не 960.0"


def test_9():
    summ = delivery_cost_calculation(30.0, "big", True, "increased")
    assert summ == 840.0, f"Сумма равна {summ}, а не 880.0"


def test_10():
    summ = delivery_cost_calculation(30.1, "big", False, "normal")
    assert summ == 500.0, f"Сумма равна {summ}, а не 500.0"


def test_11():
    summ = delivery_cost_calculation(67.0, "small", False, "normal")
    assert summ == 400.0, f"Сумма равна {summ}, а не 400.0"


def test_min_cost():
    summ = delivery_cost_calculation(4.0, "small", False, "normal")
    assert summ == 400.0, f"Сумма равна {summ}, а не 400.0"


# Тесты на ограничения по типам данных
@pytest.mark.parametrize('distance', ["фыв", "asd", "#!%", " "])
def test_distance_limited_value(distance):
    text = delivery_cost_calculation(distance, "big", True, "increased")
    assert text == "Расстояния до пункта назначения может быть только целочисленное или число с плавающей точкой", \
        f"Текс равен '{text}'"


@pytest.mark.parametrize('dimensions', [0, "фыв", "asd", "#!%", " "])
def test_dimensions_limited_value(dimensions):
    text = delivery_cost_calculation(12, dimensions, True, "increased")
    assert text == "Габариты груза могут принимать только значения: big, small ", \
        f"Текс равен '{text}'"


@pytest.mark.parametrize('fragile', [0, "фыв", "asd", "#!%", " "])
def test_fragile_limited_value(fragile):
    text = delivery_cost_calculation(13, "big", fragile, "increased")
    assert text == "Информацию о хрупкости груза может принимать только булевы значения", \
        f"Текс равен '{text}'"


@pytest.mark.parametrize('workload', [0, "фыв", "asd", "#!%", " "])
def test_workload_limited_value(workload):
    text = delivery_cost_calculation(13, "big", True, workload)
    assert text == "Информацию о загруженности службы доставки может принимать только значения:" \
                   " very high, high, increased, normal", f"Текс равен '{text}'"


def test_distance_for_fragile_cargo():
    text = delivery_cost_calculation(90, "small", True, "high")
    assert text == "Хрупкие грузы нельзя возить на расстояние более 30 км.", f"Текс равен '{text}'"
