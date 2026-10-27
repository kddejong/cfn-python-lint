"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from __future__ import annotations

from cfnlint.rules.formats.FormatKeyword import FormatKeyword


class IamRoleName(FormatKeyword):
    id = "E1165"
    shortdesc = "Validate IAM role name format"
    description = "Validate IAM role name format for ref/getatt and string values"
    tags = []
    source_url = "https://github.com/aws-cloudformation/cfn-lint/blob/main/docs/format_keyword.md#AWS::IAM::Role.Name"

    def __init__(self):
        super().__init__(
            format="AWS::IAM::Role.Name",
            pattern=r"^(/[!-~]+/)?[a-zA-Z0-9_+=,.@-]{1,64}$",
        )
