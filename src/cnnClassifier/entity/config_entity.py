# We use dataclasses as decorator to define user defined return type.
from dataclasses import dataclass
from pathlib import Path

# this dataclass will be used for accesing config for data ingestion that we defined.
@dataclass (frozen=True)
class DataIngestionConfig:
    root_dir: Path 
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# this dataclass will be used for accesing config for model prameters that we defined.
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

# For creating callsbacks to evaluate using tensorboard.
@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_dir: Path
    tensorboard_root_log_dir: Path
    checkpoint_model_filepath: Path

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

@dataclass(frozen= True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    params_image_size: list
    params_batch_size: int