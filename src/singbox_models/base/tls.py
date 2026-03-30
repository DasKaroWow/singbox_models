from typing import Literal

from singbox_models.base.base import BaseModel
from singbox_models.base.dial_fields import DialFields
from singbox_models.base.dns01 import DNS01
from singbox_models.base.path import PosixResolvedPath

TLSVersion = Literal["1.0", "1.1", "1.2", "1.3"]
CipherSuite = Literal[
    "TLS_RSA_WITH_AES_128_CBC_SHA",
    "TLS_RSA_WITH_AES_256_CBC_SHA",
    "TLS_RSA_WITH_AES_128_GCM_SHA256",
    "TLS_RSA_WITH_AES_256_GCM_SHA384",
    "TLS_AES_128_GCM_SHA256",
    "TLS_AES_256_GCM_SHA384",
    "TLS_CHACHA20_POLY1305_SHA256",
    "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA",
    "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA",
    "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA",
    "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA",
    "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
    "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
    "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
    "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
    "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256",
    "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256",
]


class TLSBase(BaseModel):
    enabled: bool | None = None
    server_name: str | None = None
    alpn: list[str] | None = None
    min_version: TLSVersion | None = None
    max_version: TLSVersion | None = None
    cipher_suites: list[CipherSuite] | CipherSuite | None = None
    curve_preferences: list[Literal["P256", "P384", "P521", "X25519", "X25519MLKEM768"]] | None = None
    certificate_path: PosixResolvedPath | None = None
    kernel_tx: bool | None = None
    kernel_rx: bool | None = None


# Inbound
class AcmeInboud(BaseModel):
    class ExternalAccount(BaseModel):
        key_id: str | None = None
        mac_key: str | None = None

    domain: list[str] | None = None
    data_directory: PosixResolvedPath | None = None
    default_server_name: str | None = None
    email: str | None = None
    provider: Literal["letsencrypt", "zerossl"] | str | None = None  # noqa: PYI051
    disable_http_challenge: bool | None = None
    disable_tls_alpn_challenge: bool | None = None
    alternative_http_port: int | None = None
    alternative_tls_port: int | None = None
    external_account: ExternalAccount | None = None
    dns01_challenge: DNS01 | None = None


class EchInbound(BaseModel):
    enabled: bool | None = None
    key: list[str] | None = None
    key_path: PosixResolvedPath | None = None


class RealityInbound(BaseModel):
    class Handshake(DialFields):
        server: str
        server_port: int

    enabled: bool | None = None
    private_key: str
    short_id: list[str]
    max_time_difference: str | None = None
    handshake: Handshake


class TLSInbound(TLSBase):
    certificate: list[str] | None = None
    key: str | None = None
    key_path: PosixResolvedPath | None = None
    client_authentication: Literal["no", "request", "require-any", "verify-if-given", "require-and-verify"] | None = (
        None
    )
    client_certificate: list[str] | None = None
    client_certificate_path: PosixResolvedPath | None = None
    client_certificate_public_key_sha256: list[str] | None = None
    acme: AcmeInboud | None = None
    ech: EchInbound | None = None
    reality: RealityInbound | None = None


# Outbound
class EchOutbound(BaseModel):
    enabled: bool | None = None
    config: list[str] | None = None
    config_path: PosixResolvedPath | None = None
    query_server_name: str | None = None


class RealityOutbound(BaseModel):
    enabled: bool | None = None
    public_key: str
    short_id: str


class TLSOutbound(TLSBase):
    disable_sni: bool | None = None
    insecure: bool | None = None
    certificate: str | None = None
    certificate_public_key_sha256: list[str] | None = None
    client_certificate: list[str] | None = None
    client_certificate_path: PosixResolvedPath | None = None
    client_key: list[str] | None = None
    client_key_path: PosixResolvedPath | None = None
    fragment: bool | None = None
    fragment_fallback_delay: str | None = None
    record_fragment: bool | None = None
    ech: EchOutbound | None = None
    reality: RealityOutbound | None = None


TLS = TLSInbound | TLSOutbound
