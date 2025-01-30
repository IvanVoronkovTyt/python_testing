import pytest

from main_function import delivery_cost_calculation

# Основные тесты для расчета стоимости доставки
def test_1():
    summ = delivery_cost_calculation(20, "small", False, "normal")
    assert summ == 400.0, f"Сумма равна {summ}, а не 400"



# Тесты на ограничения по типам данных
@pytest.mark.parametrize('distance', ["фыв", "asd", "#!%", " "])
def test_51(distance):
    text = delivery_cost_calculation(distance, "big", True, "increased")
    assert text == "Расстояния до пункта назначения может быть только целочисленное или число с плавающей точкой",\
        f"Текс равен '{text}'"

@pytest.mark.parametrize('dimensions', [0, "фыв", "asd", "#!%", " "])
def test_52(dimensions):
    text = delivery_cost_calculation(12, dimensions, True, "increased")
    assert text == "Габариты груза могут принимать только значения: big, small ",\
        f"Текс равен '{text}'"

@pytest.mark.parametrize('fragile', [0, "фыв", "asd", "#!%", " "])
def test_53(fragile):
    text = delivery_cost_calculation(13, "big", fragile, "increased")
    assert text == "Информацию о хрупкости груза может принимать только булевы значения",\
        f"Текс равен '{text}'"

@pytest.mark.parametrize('workload', [0, "фыв", "asd", "#!%", " "])
def test_54(workload):
    text = delivery_cost_calculation(13, "big", True, workload)
    assert text == "Информацию о загруженности службы доставки может принимать только значения:" \
                   " very high, high, increased, normal", f"Текс равен '{text}'"

def test_55():
    text = delivery_cost_calculation(32, "big", True, "increased")
    assert text == "Хрупкие грузы нельзя возить на расстояние более 30 км.", f"Текс равен '{text}'"