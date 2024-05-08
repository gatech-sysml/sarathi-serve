import random
import math
from typing import Tuple

from sarathi.benchmark.request_generator.base_request_length_generator import (
    BaseRequestLengthGenerator, )


class UniformRequestLengthGenerator(BaseRequestLengthGenerator):

    def get_next_num_tokens(self) -> Tuple[float, float]:
        total_tokens = random.uniform(
            self._config.uniform_request_length_generator_min_tokens,
            self._config.uniform_request_length_generator_max_tokens,
        )

        decode_tokens = math.ceil(
            total_tokens /
            (1 + self._config.
             uniform_request_length_generator_prefill_to_decode_ratio))
        prefill_tokens = total_tokens - decode_tokens
        assert prefill_tokens > 0 and decode_tokens > 0

        return prefill_tokens, decode_tokens
