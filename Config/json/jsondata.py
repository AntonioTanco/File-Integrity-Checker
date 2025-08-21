from dataclasses import dataclass
from datetime import time
from typing import List

# Using dataclasses to define the JSON Log Structure

@dataclass
class Jsonlog:
    hostname: str
    uuid: str
    targeted_services: List[str]
    targeted_paths: List[str]
    hashes_generated: List[str]
