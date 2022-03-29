import types

import faker
import pytest

from author import make_divider_of

fake = faker.Faker()


DATA = [(fake.pyint(), fake.pyint()) for _ in range(6)]


@pytest.mark.parametrize("divider, divisible", DATA)
def test_make_divider_of(divider, divisible):
    func = make_divider_of(divider)
    expected = eval(f"{divisible} / {divider}")
    assert func(divisible) == expected, "Неверный результат при делении"


@pytest.mark.parametrize("divider", [1, 2, 3, 4, 5, 6])
def test_make_divider_returns_function(divider):
    func = make_divider_of(divider)
    assert isinstance(
        func, types.FunctionType
    ), "Функция 'make_divider_of' должна возвращать производную функцию"
