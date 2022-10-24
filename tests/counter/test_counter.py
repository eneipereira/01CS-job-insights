from src.counter import count_ocurrences


def test_counter():
    count_py_ocurrences = count_ocurrences("src/jobs.csv", "Python")
    count_js_ocurrences = count_ocurrences("src/jobs.csv", "Javascript")

    assert count_py_ocurrences == 1639
    assert count_js_ocurrences == 122
