# We use dataclasses as decorator to define user defined return type.
from dataclasses import dataclass
from pathlib import Path

# this dataclass will be used for accesing config that we defined.
@dataclass (frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_URL: str
    local_data_file: Path
    unzip_dir: Path