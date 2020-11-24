from dataclasses import dataclass, field
from enum import Enum

from marshmallow_dataclass import class_schema


class Command(Enum):
    CREATE = 'create'
    DELETE = 'delete'


@dataclass
class Config:
    file_path: str
    command: Command = field(metadata=dict(by_value=True))
    bulk_size: int = 20


Config.Schema = class_schema(Config)

json_data = [
    {
        'file_path': '/validators-example/file1',
        'command': 'create',
    },
    {
        'file_path': '/validators-example/file2',
        'command': 'delete',
    },
]

configs = Config.Schema().load(json_data, many=True)
print(configs)

assert len(configs) == 2
assert configs[0].file_path == '/validators-example/file1'
assert configs[0].command is Command.CREATE
assert configs[0].bulk_size == 20
