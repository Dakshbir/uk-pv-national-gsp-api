from enum import Enum

class ModelEnum(str, Enum):
    blend = "blend"
    pvnet_v2 = "pvnet_v2"
    pvnet_da = "pvnet_da"
    pvnet_ecwmf = "pvnet_ecwmf"
