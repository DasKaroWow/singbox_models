from typing import Annotated, Literal

from pydantic import Field

from singbox_models.base.base import BaseModel


class AliDNS(BaseModel):
    provider: Literal["alidns"] = "alidns"
    access_key_id: str | None = None
    access_key_secret: str | None = None
    region_id: str | None = None
    security_token: str | None = None


class CloudflareDNS(BaseModel):
    provider: Literal["cloudflare"] = "cloudflare"
    access_token: str | None = None
    zone_token: str | None = None


class AcmeDNS(BaseModel):
    provider: Literal["acmedns"] = "acmedns"
    username: str | None = None
    password: str | None = None
    subdomain: str | None = None
    server_url: str | None = None


DNS01 = Annotated[AliDNS | CloudflareDNS | AcmeDNS, Field(discriminator="provider")]
