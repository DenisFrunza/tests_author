try:
    from author import print_contact
except ImportError:
    assert True, "функция 'print_contact' не удалена"


def test_class_contact_attrs(contact):
    expected_result = {"name", "phone", "birthday", "address"}
    actual_result = set(contact.__dict__.keys())
    error_text = "Хьюстон, у нас проблема, допустимые значения {0}, ваши значения {1}"
    assert actual_result.issubset(expected_result), error_text.format(
        expected_result, actual_result
    )


def test_class_methods(contact):
    assert hasattr(contact.__class__, "show_contact") and callable(
        getattr(contact.__class__, "show_contact")
    ), "Метод 'show_contact' не найден"


def test_show_contact(contact, capsys):
    contact.show_contact()
    out, _ = capsys.readouterr()

    assert out, 'Метод не выводит строку на экран'
