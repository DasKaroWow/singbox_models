# src/singbox_models/route/route.py
from typing import Literal

from singbox_models.base import BaseModel
from singbox_models.base.dial_fields import DomainResolver
from singbox_models.route.rule import Rule
from singbox_models.route.rule_set import RuleSet


class Route(BaseModel):
    rules: list[Rule] | None = None
    rule_set: list[RuleSet] | None = None
    final: str | None = None
    auto_detect_interface: bool | None = None
    override_android_vpn: bool | None = None
    default_interface: str | None = None
    default_mark: int | None = None
    find_process: bool | None = None
    default_domain_resolver: str | DomainResolver | None = None
    default_network_strategy: Literal["default", "hybrid", "fallback"] | None = None
    default_network_type: list[Literal["wifi", "cellular", "ethernet", "other"]] | None = None
    default_fallback_network_type: list[Literal["wifi", "cellular", "ethernet"]] | None = None
    default_fallback_delay: str | None = None
