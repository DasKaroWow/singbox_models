# src/singbox_models/route/rule_set.py
from typing import Annotated, Literal

from pydantic import Field

from singbox_models.base import BaseModel


class DefaultHeadlessRule(BaseModel):
    query_type: list[int | str] | None = None
    network: list[Literal["tcp", "udp"]] | None = None
    domain: list[str] | None = None
    domain_suffix: list[str] | None = None
    domain_keyword: list[str] | None = None
    domain_regex: list[str] | None = None
    source_ip_cidr: list[str] | None = None
    ip_cidr: list[str] | None = None
    source_port: list[int] | None = None
    source_port_range: list[str] | None = None
    port: list[int] | None = None
    port_range: list[str] | None = None
    process_name: list[str] | None = None
    process_path: list[str] | None = None
    process_path_regex: list[str] | None = None
    package_name: list[str] | None = None
    network_type: list[Literal["wifi", "cellular", "ethernet", "other"]] | None = None
    network_is_expensive: bool | None = None
    network_is_constrained: bool | None = None
    network_interface_address: dict[str, list[str]] | None = None
    default_interface_address: list[str] | None = None
    wifi_ssid: list[str] | None = None
    wifi_bssid: list[str] | None = None
    invert: bool | None = None


class LogicalHeadlessRule(BaseModel):
    type: Literal["logical"] = "logical"
    mode: Literal["and", "or"] | None = None
    rules: list[DefaultHeadlessRule] | None = None
    invert: bool | None = None


HeadlessRule = DefaultHeadlessRule | LogicalHeadlessRule


class InlineRuleSet(BaseModel):
    type: Literal["inline"] = "inline"
    tag: str
    rules: list[HeadlessRule]


class LocalRuleSet(BaseModel):
    type: Literal["local"] = "local"
    tag: str
    format: Literal["source", "binary"] | None = None
    path: str


class RemoteRuleSet(BaseModel):
    type: Literal["remote"] = "remote"
    tag: str
    format: Literal["source", "binary"] | None = None
    url: str
    download_detour: str | None = None
    update_interval: str | None = None


RuleSet = Annotated[
    InlineRuleSet | LocalRuleSet | RemoteRuleSet,
    Field(discriminator="type"),
]
