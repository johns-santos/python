from hello import hello


def test_string():
    assert hello("John") == "hello, John"

def test_default():
    assert hello() == "hello, world"

def test_list():
    names = ["john", "bella", "moni"]
    for name in names:
        assert hello(name) == f"hello, {name}"
