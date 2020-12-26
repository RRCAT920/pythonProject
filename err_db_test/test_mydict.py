# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from err_db_test.mydict import Dict


class TestDict(TestCase):
    def setUp(self) -> None:
        print('setup...')

    def tearDown(self) -> None:
        print('teardown...')

    def test_init(self):
        d = Dict(a=1, b=2)
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 2)
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_key_error(self):
        d = Dict()
        with self.assertRaises(KeyError):
            foo = d['empty']

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertTrue(d['key'], 'value')

    def test_attr_error(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            foo = d.empty


if __name__ == '__main__':
    unittest.main()
