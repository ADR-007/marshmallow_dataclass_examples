from dataclasses import dataclass
from typing import Any, Dict

from marshmallow import ValidationError, validates_schema, validates
from marshmallow_dataclass import class_schema


@dataclass
class Config:
    min_value: int
    max_value: int

    @validates("min_value")
    def validate_min(self, value):
        if value < 0:
            raise ValidationError("Min value must be greater than 0.")

    @validates_schema
    def validate_min_max(self, data: Dict[str, Any], partial: bool, many: bool) -> None:
        if data['min_value'] > data['max_value']:
            raise ValidationError('min_value should be less then max_value')


Config.Schema = class_schema(Config)

json_data = {
    'min_value': -20,
    'max_value': 15,
}

config = Config.Schema().load(json_data)
print(config)
