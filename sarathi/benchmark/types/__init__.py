from typing import List, Tuple, Dict

from sarathi.utils.base_int_enum import BaseIntEnum
from sarathi.benchmark.types.request_generator_type import RequestGeneratorType
from sarathi.benchmark.types.request_interval_generator_type import RequestIntervalGeneratorType
from sarathi.benchmark.types.request_length_generator_type import RequestLengthGeneratorType

ResourceMapping = List[Tuple[str, int]]  # List of (node_ip, gpu_id)
ReplicaResourceMapping = Dict[
    str, ResourceMapping]  # Dict of replica_id -> ResourceMapping

__all__ = [
    RequestGeneratorType,
    RequestLengthGeneratorType,
    RequestIntervalGeneratorType,
    BaseIntEnum,
    ResourceMapping,
    ReplicaResourceMapping,
]
