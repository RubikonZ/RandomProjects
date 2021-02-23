import sys
import trafaret
from trafaret_config import read_and_validate

TRAFARET = trafaret.Dict(dict)

try:
    config = read_and_validate('config.yaml', TRAFARET)
except ConfigError as e:
    e.output()
    sys.exit(1)

print(config)