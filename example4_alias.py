from dataclasses import dataclass, field
from enum import Enum

from marshmallow_dataclass import class_schema


class Command(Enum):
    CREATE = 'create'
    DELETE = 'delete'


@dataclass
class Config:
    bulk_size: int = field(metadata=dict(data_key='main_bulk_size'))


Config.Schema = class_schema(Config)

json_data = {
    'main_bulk_size': 20
}

config = Config.Schema().load(json_data)
print(config)

assert config.bulk_size == 20
