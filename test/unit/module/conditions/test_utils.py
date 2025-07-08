"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import hashlib
from unittest import TestCase

from cfnlint.conditions._utils import _cached_hash, _make_hashable, get_hash


class TestUtils(TestCase):
    """Test utility functions for conditions"""

    def test_make_hashable(self):
        """Test _make_hashable function"""
        # Test with dict
        self.assertEqual(_make_hashable({"a": 1, "b": 2}), (("a", 1), ("b", 2)))

        # Test with nested dict
        self.assertEqual(_make_hashable({"a": {"b": 1}}), (("a", (("b", 1),)),))

        # Test with list
        self.assertEqual(_make_hashable([1, 2, 3]), (1, 2, 3))

        # Test with nested list
        self.assertEqual(_make_hashable([1, [2, 3]]), (1, (2, 3)))

        # Test with object that has _value attribute
        class TestObj:
            def __init__(self):
                self._value = "test"

        obj = TestObj()
        self.assertEqual(_make_hashable(obj), "test")

        # Test with simple value
        self.assertEqual(_make_hashable(1), 1)
        self.assertEqual(_make_hashable("test"), "test")
        self.assertEqual(_make_hashable(None), None)

    def test_cached_hash(self):
        """Test _cached_hash function"""
        # Test with simple types
        self.assertEqual(
            _cached_hash("test"), hashlib.sha1("test".encode("utf-8")).hexdigest()
        )

        # Test with complex types
        complex_obj = (("a", 1), ("b", 2))
        self.assertEqual(
            _cached_hash(complex_obj),
            hashlib.sha1(str(complex_obj).encode("utf-8")).hexdigest(),
        )

        # Test caching (call twice, should return same result)
        result1 = _cached_hash("test")
        result2 = _cached_hash("test")
        self.assertEqual(result1, result2)

    def test_get_hash(self):
        """Test get_hash function"""
        # Test with simple types
        self.assertEqual(
            get_hash("test"), hashlib.sha1("test".encode("utf-8")).hexdigest()
        )

        # Test with dict
        dict_obj = {"a": 1, "b": 2}
        dict_hash = get_hash(dict_obj)
        self.assertTrue(isinstance(dict_hash, str))
        self.assertEqual(len(dict_hash), 40)  # SHA-1 hash is 40 chars

        # Test with list
        list_obj = [1, 2, 3]
        list_hash = get_hash(list_obj)
        self.assertTrue(isinstance(list_hash, str))
        self.assertEqual(len(list_hash), 40)

        # Test with complex nested structure
        complex_obj = {"a": [1, {"b": 2}]}
        complex_hash = get_hash(complex_obj)
        self.assertTrue(isinstance(complex_hash, str))
        self.assertEqual(len(complex_hash), 40)

        # Test consistency (same object should produce same hash)
        self.assertEqual(get_hash(dict_obj), get_hash(dict_obj))

        # Test different objects produce different hashes
        self.assertNotEqual(get_hash(dict_obj), get_hash(list_obj))
