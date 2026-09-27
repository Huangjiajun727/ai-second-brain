import pytest

from week4.notes import count_notes, create_notes, get_note


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
    order.append(4.0)

    # Assert
    assert order == expected_list


def f():
    raise OSError("1111")


def test_mytest():
    with pytest.raises(OSError):
        f()


def test_create_notes():
    create_notes("测试", "测试pytest", "pytest")
    count = count_notes()
    assert count == 6


def test_search_id():
    item = get_note("666")
    assert item == {
        "title": "测试",
        "content": "测试pytest",
        "tag": "pytest",
        "id": "0810241f-ac84-4a6c-9d61-1fa257f54bb3",
        "created_at": "2026-09-26 11:09:42",
        "updated_at": "2026-09-26 11:09:42",
    }
