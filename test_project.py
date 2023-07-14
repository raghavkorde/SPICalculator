
"""def test_calculate_cpi():
    assert calculate_cpi(10, 10) == 10
    assert calculate_cpi(0, 0) == 0
    assert calculate_cpi(5.5, 6.0) == 5.83"""

import pytest
from project import calculate_cpi, get_marksheet


def test_calculate_cpi():
    updated_cpi = calculate_cpi(8.5, 8.0)
    assert updated_cpi == 8.17


def test_get_marksheet():
    marksheet = [["Subject", "Type", "Credit", "Grade"],["PP", "T", "3", "AA"]]
    expected_output = """+-----------+--------+----------+---------+
| Subject   | Type   |   Credit | Grade   |
+===========+========+==========+=========+
| PP        | T      |        3 | AA      |
+-----------+--------+----------+---------+"""
    assert get_marksheet(marksheet) == expected_output
