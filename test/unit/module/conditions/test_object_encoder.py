"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import json
from unittest import TestCase

from cfnlint.conditions._utils import ObjectEncoder


class TestObjectEncoder(TestCase):
    """Test ObjectEncoder class"""

    def test_object_encoder(self):
        """Test ObjectEncoder with objects that have _value attribute"""

        # Create a test object with _value attribute
        class TestObj:
            def __init__(self, value):
                self._value = value

        # Create an instance of the test object
        obj = TestObj("test_value")

        # Use ObjectEncoder to encode the object
        encoded = json.dumps(obj, cls=ObjectEncoder)

        # Verify that the _value attribute was used
        self.assertEqual(encoded, '"test_value"')

        # Test with a list containing objects with _value attribute
        obj_list = [TestObj("value1"), TestObj("value2")]
        encoded_list = json.dumps(obj_list, cls=ObjectEncoder)

        # Verify that the _value attributes were used
        self.assertEqual(encoded_list, '["value1", "value2"]')

        # Test with a dict containing objects with _value attribute
        obj_dict = {"key1": TestObj("value1"), "key2": TestObj("value2")}
        encoded_dict = json.dumps(obj_dict, cls=ObjectEncoder)

        # Verify that the _value attributes were used
        self.assertEqual(encoded_dict, '{"key1": "value1", "key2": "value2"}')
