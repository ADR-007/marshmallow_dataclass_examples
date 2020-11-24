from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional

from marshmallow import Schema, fields
from marshmallow_dataclass import class_schema


class Command(Enum):
    CREATE = 'create'
    DELETE = 'delete'


class PathField(fields.String):
    def _serialize(self, value, attr, obj, **kwargs) -> Optional[str]:
        if isinstance(value, Path):
            value = str(value)

        return super()._serialize(value, attr, obj, **kwargs)

    def _deserialize(self, value, attr, data, **kwargs) -> Optional[Path]:
        result = super()._deserialize(value, attr, data, **kwargs)

        if result is None:
            return None

        return Path(result)


Schema.TYPE_MAPPING[Path] = PathField


@dataclass
class Config:
    file_path: Path
    command: Command = field(metadata=dict(by_value=True))
    bulk_size: int = 20


Config.Schema = class_schema(Config)

json_data = {
    'file_path': '/validators-example/file',
    'command': 'create',
}

config = Config.Schema().load(json_data)
print(config)

assert config.file_path == Path('/validators-example/file')
assert config.command is Command.CREATE
assert config.bulk_size == 20
