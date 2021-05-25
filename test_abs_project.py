def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'


def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of number"


def main():
    test_input_text(10, 10)
    test_substring('123', '123')
    test_abs1()
    print("All tests passed!")


if __name__ == '__main__':
    main()
