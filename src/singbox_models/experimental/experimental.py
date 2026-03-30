from singbox_models.base import BaseModel, PosixResolvedPath


class CacheFile(BaseModel):
    enabled: bool | None = None
    path: PosixResolvedPath | None = None
    cache_id: str | None = None
    store_fakeip: bool | None = None
    store_rdrc: bool | None = None
    rdrc_timeout: str | None = None


class ClashAPI(BaseModel):
    external_controller: str | None = None
    external_ui: str | None = None
    external_ui_download_url: str | None = None
    external_ui_download_detour: str | None = None
    secret: str | None = None
    default_mode: str | None = None
    access_control_allow_origin: list[str] | None = None
    access_control_allow_private_network: bool | None = None

    # Deprecated
    store_mode: bool | None = None
    store_selected: bool | None = None
    store_fakeip: bool | None = None
    cache_file: str | None = None
    cache_id: str | None = None


class V2RayAPI(BaseModel):
    class Stats(BaseModel):
        enabled: bool | None = None
        inbounds: list[str] | None = None
        outbounds: list[str] | None = None
        users: list[str] | None = None

    listen: str | None = None
    stats: Stats | None = None


class Experimental(BaseModel):
    cache_file: CacheFile | None = None
    clash_api: ClashAPI | None = None
    v2ray_api: V2RayAPI | None = None
