from {{cookiecutter.package_name}}.subpackage_a.module_a import add


def test_add():
    assert add(2, 2) == 4
