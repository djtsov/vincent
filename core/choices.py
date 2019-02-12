from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.name, x.value) for x in cls)


class PriorityEnum(ChoiceEnum):
    HIGH = "High"
    NORM = "Normal"
    LOW = "Low"
