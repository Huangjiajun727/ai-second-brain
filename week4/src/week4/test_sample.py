from week4.notes import create_notes
import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def second_entry():
    return 2


# Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string(order, expected_list):
    # Act
    order.append(3.0)

    # Assert
    assert order == expected_list


def f():
    raise OSError('1111')

def test_mytest():
    with pytest.raises(OSError):
        f()