"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from __future__ import annotations

from typing import Any

from cfnlint.jsonschema import ValidationError
from cfnlint.rules.jsonschema.CfnLintJsonSchema import CfnLintJsonSchema


class SecurityGroupProtocolsAndPortsExclusive(CfnLintJsonSchema):
    id = "W3687"
    shortdesc = "Validate that ports aren't specified for certain protocols"
    description = (
        "When using a protocol other than icmp, icmpv6, tcp, or udp "
        "the port ranges properties are ignored"
    )
    tags = ["resources"]

    def __init__(self) -> None:
        super().__init__(
            keywords=["aws_ec2_securitygroup/protocols_and_port_ranges_exclude"]
        )

    def message(self, instance: Any, err: ValidationError) -> str:
        if not isinstance(instance, dict):
            return self.description

        return (
            "['FromPort', 'ToPort'] are ignored when using "
            f"'IpProtocol' value {instance.get('IpProtocol')!r}"
        )