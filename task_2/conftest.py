import faker
import pytest

from author import Contact
faker.Faker.seed(1)
fake = faker.Faker()


@pytest.fixture(scope='function')
def contact():
    return Contact(fake.name(), fake.phone_number(), fake.date_time(), fake.address())
