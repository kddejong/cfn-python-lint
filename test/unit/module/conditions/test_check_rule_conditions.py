"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from unittest import TestCase

from cfnlint.decode import decode_str
from cfnlint.template import Template


class TestCheckRuleConditions(TestCase):
    """Test check_rule_conditions method"""

    def test_check_rule_conditions_basic(self):
        """Test basic check_rule_conditions functionality"""
        template = decode_str(
            """
        Parameters:
          Environment:
            Type: String
            AllowedValues: ["prod", "dev", "stage"]
        Conditions:
          IsProduction: !Equals [!Ref Environment, "prod"]
          IsUsEast1: !Equals [!Ref "AWS::Region", "us-east-1"]
          IsProdAndUsEast1: !And [!Condition IsProduction, !Condition IsUsEast1]
        """
        )[0]

        cfn = Template("", template)

        # Test with matching parameter values
        self.assertTrue(
            cfn.conditions.check_rule_conditions(
                {"IsProduction": True}, {"Environment": "prod"}
            )
        )

        # Test with non-matching parameter values
        self.assertFalse(
            cfn.conditions.check_rule_conditions(
                {"IsProduction": True}, {"Environment": "dev"}
            )
        )

        # Test with multiple conditions
        self.assertTrue(
            cfn.conditions.check_rule_conditions(
                {"IsProdAndUsEast1": True},
                {"Environment": "prod", "AWS::Region": "us-east-1"},
            )
        )

        # Test with empty conditions
        self.assertTrue(
            cfn.conditions.check_rule_conditions({}, {"Environment": "prod"})
        )

        # Test with empty parameter values
        self.assertTrue(
            cfn.conditions.check_rule_conditions({"IsProduction": True}, {})
        )
