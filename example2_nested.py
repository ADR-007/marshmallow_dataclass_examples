from dataclasses import dataclass, field
from enum import Enum

from marshmallow_dataclass import class_schema


class Command(Enum):
    CREATE = 'create'
    DELETE = 'delete'


@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str


@dataclass
class Config:
    file_path: str
    command: Command = field(metadata=dict(by_value=True))
    database_config: DatabaseConfig
    bulk_size: int = 20


DatabaseConfig.Schema = class_schema(DatabaseConfig)
Config.Schema = class_schema(Config)

json_data = {
    'file_path': '/validators-example/file',
    'command': 'create',
    'database_config': {
        'host': 'localhost',
        'port': 5432,
        'username': 'root',
        'password': 'qwerty'
    }
}

config = Config.Schema().load(json_data)
print(config)

assert config.file_path == '/validators-example/file'
assert config.command is Command.CREATE
assert config.bulk_size == 20
assert config.database_config.host == 'localhost'
assert config.database_config.port == 5432
assert config.database_config.username == 'root'
assert config.database_config.password == 'qwerty'
