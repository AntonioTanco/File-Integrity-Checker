from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List

# Using dataclasses to define the JSON Log Structure

@dataclass
class Jsonlog:
    UUID: str
    timestamp: datetime
    hostname: str
    targeted_services: List[str]
    targeted_paths: List[str]
    hashes_generated: List[str]

@dataclass
class JsonLogData:
    hashing_operations: List[Jsonlog] = field(default_factory=list)
