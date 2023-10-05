from datetime import datetime
from PoolLocalizationStruct import PoolLocalizationStruct


class PoolStruct(dict):
    def __init__(self, version: str, start_time: datetime, end_time: datetime, uigf_type: int, order: int,
                 up_orange1_item: int, up_purple1_item: int, up_purple2_item: int, up_purple3_item: int,
                 up_orange2_item: int = 0, up_purple4_item: int = 0, up_purple5_item: int = 0,
                 timezone: int = 8):
        super().__init__()
        self["version"] = version
        self["start_time"] = start_time
        self["end_time"] = end_time
        self["timezone"] = timezone
        self["uigf_type"] = uigf_type
        self["order"] = order
        self["up_orange1_item"] = up_orange1_item
        self["up_purple1_item"] = up_purple1_item
        self["up_purple2_item"] = up_purple2_item
        self["up_purple3_item"] = up_purple3_item
        self["up_orange2_item"] = up_orange2_item
        self["up_purple4_item"] = up_purple4_item
        self["up_purple5_item"] = up_purple5_item
        self["localization"] = {}

    def add_localization(self, locale: str, this_localization: PoolLocalizationStruct):
        self["localization"][locale] = this_localization
