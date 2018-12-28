# -*- coding: utf-8 -*-
import pytest

from dongsam.basic import *
from dongsam import basic


word_type = {
    0: 'eng',
    1: 'kor',
    2: 'chi'
}


class TestBasic:

    def test_get_key_from_value(self):
        assert get_key_from_value(word_type, 'kor') == 1

    def test_get_key_from_value_not_exist(self):
        assert get_key_from_value(word_type, 'kor2') == None

    def test_basic_get_key_from_value(self):
        assert basic.get_key_from_value(word_type, 'kor') == 1

    def test_basic_list_get_key_from_value(self):
        assert basic.struct.get_key_from_value(word_type, 'kor') == 1