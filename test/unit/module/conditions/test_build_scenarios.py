"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from unittest import TestCase

from cfnlint.decode import decode_str
from cfnlint.template import Template


class TestBuildScenarios(TestCase):
    """Test build_scenarios and related methods"""

    def test_build_scenarios_on_region(self):
        """Test build_scenarios_on_region method"""
        template = decode_str(
            """
        Conditions:
          IsUsEast1: !Equals [!Ref "AWS::Region", "us-east-1"]
          IsUsWest2: !Equals [!Ref "AWS::Region", "us-west-2"]
          IsNotUsEast1: !Not [!Condition IsUsEast1]
        """
        )[0]

        cfn = Template("", template)

        # Test with matching region
        scenarios = cfn.conditions.build_scenerios_on_region("IsUsEast1", "us-east-1")
        self.assertEqual(scenarios, [True])

        # Test with non-matching region
        scenarios = cfn.conditions.build_scenerios_on_region("IsUsEast1", "us-west-2")
        self.assertEqual(scenarios, [False])

        # Test with Not condition
        scenarios = cfn.conditions.build_scenerios_on_region(
            "IsNotUsEast1", "us-east-1"
        )
        self.assertEqual(scenarios, [False])

        # Test with non-matching region for Not condition
        scenarios = cfn.conditions.build_scenerios_on_region(
            "IsNotUsEast1", "us-west-2"
        )
        self.assertEqual(scenarios, [True])

        # Test with nonexistent condition
        scenarios = cfn.conditions.build_scenerios_on_region(
            "NonExistentCondition", "us-east-1"
        )
        self.assertEqual(scenarios, [True, False])

        # Test with condition that doesn't depend on region
        template = decode_str(
            """
        Conditions:
          IsProduction: !Equals [!Ref Environment, "prod"]
        """
        )[0]

        cfn = Template("", template)
        scenarios = cfn.conditions.build_scenerios_on_region(
            "IsProduction", "us-east-1"
        )
        self.assertEqual(scenarios, [True, False])
