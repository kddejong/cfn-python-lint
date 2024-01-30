"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import pathlib

import regex as re

from cfnlint.helpers import load_plugins
from cfnlint.jsonschema._utils import ensure_list
from cfnlint.rules.jsonschema.Base import BaseJsonSchema

_pattern = re.compile(r"[\W_]+")


class CfnLint(BaseJsonSchema):
    id = "E1101"
    shortdesc = "Validate an item against additional checks"
    description = "Use supplemental logic to validate properties against"
    tags = []

    def __init__(self) -> None:
        super().__init__()
        # relative path to the parent of cfnlint.rules
        root_dir = pathlib.Path(__file__).parent.parent
        rules = load_plugins(
            str(root_dir),
            "CfnLintKeyword",
            "cfnlint.rules.jsonschema.CfnLintKeyword",
        )
        rules.extend(
            load_plugins(
                str(root_dir),
                "CfnLintJsonSchema",
                "cfnlint.rules.jsonschema.CfnLintJsonSchema",
            )
        )
        for rule in rules:
            self.child_rules[rule.id] = None

    # pylint: disable=unused-argument
    def cfnLint(self, validator, keywords, instance, schema):
        keywords = ensure_list(keywords)
        for keyword in keywords:
            for rule in self.child_rules.values():
                if rule is None:
                    continue
                if not rule.id:
                    continue

                for rule_keyword in rule.keywords:
                    if rule_keyword == keyword:
                        fn_name = _pattern.sub("", rule_keyword).lower()
                        fn = getattr(rule, fn_name)
                        if not fn:
                            raise ValueError(f"{fn_name!r} not found in {rule.id!r}")
                        yield from fn(validator, keyword, instance, schema)