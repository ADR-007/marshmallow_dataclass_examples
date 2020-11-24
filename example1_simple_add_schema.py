from dataclasses import dataclass, field
from enum import Enum

from marshmallow_dataclass import add_schema


class Command(Enum):
    CREATE = 'create'
    DELETE = 'delete'


@add_schema  # <--------------
@dataclass
class Config:
    file_path: str
    command: Command = field(metadata=dict(by_value=True))
    bulk_size: int = 20


json_data = {
    'file_path': '/validators-example/file',
    'command': 'create',
}

config = Config.Schema().load(json_data)
print(config)
print(Config.Schema().dump(config))

assert config.file_path == '/validators-example/file'
assert config.command is Command.CREATE
assert config.bulk_size == 20
