# def setup_module(module):
#     print('\nsetup_module()')
#
# def teardown_module(module):
#     print('teardown_module()')
#
# def setup_function(function):
#     print('\nsetup_function()', function)
#
# def teardown_function(function):
#     print('\nteardown_function()', function)
#
# def test_1():
#     print('-  test_1()')
#
# def test_2():
#     print('-  test_2()')

import pytest
import sys


def test_1(fixt1):
    print('-  test_1()')
    assert fixt1

@pytest.mark.skipif(sys.version_info > (3, 0), reason="skipped test")
def test_2(fixt1):
    print('-  test_2()')
    assert 1 == 1
