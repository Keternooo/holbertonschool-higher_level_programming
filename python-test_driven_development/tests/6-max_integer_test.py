#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def max_at_the_end(self):
        self.assertEqual(max_integer([1,2,3,4]), 4)

    def max_at_middle(self):
        self.assertEqual(max_interger([1,5,2]), 5)
