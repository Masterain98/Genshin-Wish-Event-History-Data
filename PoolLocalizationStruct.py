class PoolLocalizationStruct(dict):
    def __init__(self, locale: str, pool_title: str, banner_image: str, banner_image_backup: str):
        super().__init__()
        self["locale"] = locale
        self["pool_title"] = pool_title
        self["banner_image"] = banner_image
        self["banner_image_backup"] = banner_image_backup
