"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from unittest import TestCase, mock

from cfnlint.decode import decode_str
from cfnlint.template import Template


class TestSatisfiableWithRules(TestCase):
    """Test satisfiable method with rules"""

    def test_satisfiable_with_rules(self):
        """Test satisfiable with rules"""
        template = decode_str(
            """
        Parameters:
          Environment:
            Type: String
            AllowedValues: ["prod", "dev", "stage"]
        Conditions:
          IsProduction: !Equals [!Ref Environment, "prod"]
        Rules:
          ProdRule:
            RuleCondition: !Equals [!Ref Environment, "prod"]
            Assertions:
              - Assert: !Equals [!Ref Environment, "prod"]
                AssertDescription: Environment must be prod
        """
        )[0]

        cfn = Template("", template)

        # Test with empty conditions and rules
        self.assertTrue(cfn.conditions.satisfiable({}, {"Environment": "prod"}))

        # Test with rules and no conditions
        # Mock the _rules attribute to be non-empty
        cfn.conditions._rules = [mock.MagicMock()]

        # Test with empty conditions and rules
        self.assertTrue(cfn.conditions.satisfiable({}, {"Environment": "prod"}))

        # Test with rules and conditions
        self.assertTrue(
            cfn.conditions.satisfiable({"IsProduction": True}, {"Environment": "prod"})
        )
