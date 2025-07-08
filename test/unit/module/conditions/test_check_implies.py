"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from unittest import TestCase

from cfnlint.decode import decode_str
from cfnlint.template import Template


class TestCheckImplies(TestCase):
    """Test check_implies method"""

    def test_check_implies_basic(self):
        """Test basic check_implies functionality"""
        template = decode_str(
            """
        Conditions:
          IsProduction: !Equals [!Ref Environment, "prod"]
          IsUsEast1: !Equals [!Ref "AWS::Region", "us-east-1"]
          IsProdAndUsEast1: !And [!Condition IsProduction, !Condition IsUsEast1]
        """
        )[0]

        cfn = Template("", template)

        # Test that IsProdAndUsEast1 implies IsProduction
        self.assertTrue(
            cfn.conditions.check_implies({"IsProdAndUsEast1": True}, "IsProduction")
        )

        # Test that IsProdAndUsEast1 implies IsUsEast1
        self.assertTrue(
            cfn.conditions.check_implies({"IsProdAndUsEast1": True}, "IsUsEast1")
        )

        # Test that IsProduction does not imply IsProdAndUsEast1
        self.assertFalse(
            cfn.conditions.check_implies({"IsProduction": True}, "IsProdAndUsEast1")
        )

        # Test with multiple conditions
        self.assertTrue(
            cfn.conditions.check_implies(
                {"IsProduction": True, "IsUsEast1": True}, "IsProdAndUsEast1"
            )
        )

    def test_check_implies_with_nonexistent_condition(self):
        """Test check_implies with nonexistent condition"""
        template = decode_str(
            """
        Conditions:
          IsProduction: !Equals [!Ref Environment, "prod"]
          IsUsEast1: !Equals [!Ref "AWS::Region", "us-east-1"]
        """
        )[0]

        cfn = Template("", template)

        # Test with nonexistent condition
        # When the condition doesn't exist, check_implies returns True
        self.assertTrue(
            cfn.conditions.check_implies({"IsProduction": True}, "NonExistentCondition")
        )

        # Test with nonexistent condition in scenarios
        self.assertTrue(
            cfn.conditions.check_implies({"NonExistentCondition": True}, "IsProduction")
        )
