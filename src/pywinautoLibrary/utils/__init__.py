# Copyright 2023-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import timedelta
from typing import Union


def is_noney(value):
    """Check if value is None or empty string.

    :param value: Value to check.
    :type value: Any
    :return: True if value is None or empty string, False otherwise.
    :rtype: bool
    """
    return value is None or value == ''


def is_truthy(value):
    """Check if value is considered truthy.

    :param value: Value to check.
    :type value: Any
    :return: True if value is truthy, False otherwise.
    :rtype: bool
    """
    if value is None:
        return False
    if isinstance(value, str):
        return value.lower() not in ('false', 'no', 'off', '0', '')
    return bool(value)


from .librarylistener import LibraryListener
from .dynamiccore import DynamicCore


def _convert_timeout(timeout: Union[str, int, float, timedelta]) -> float:
    """Convert timeout to seconds.

    :param timeout: Timeout in seconds, Robot Framework time format, or timedelta.
    :type timeout: str, int, float, or timedelta
    :return: Timeout in seconds.
    :rtype: float
    """
    if isinstance(timeout, timedelta):
        return timeout.total_seconds()
    if isinstance(timeout, (int, float)):
        return float(timeout)
    if not isinstance(timeout, str):
        raise TypeError(f"Timeout must be string, number or timedelta, got {type(timeout).__name__}.")
    timeout = timeout.strip().lower()
    if not timeout:
        return 0.0
    # Handle Robot Framework time format (e.g. '1s', '1min 30s', '2h 30min 45s')
    factors = {
        'h': 3600,
        'hour': 3600,
        'hours': 3600,
        'm': 60,
        'min': 60,
        'minute': 60,
        'minutes': 60,
        's': 1,
        'sec': 1,
        'second': 1,
        'seconds': 1,
        'ms': 0.001,
        'millisec': 0.001,
        'millisecond': 0.001,
        'milliseconds': 0.001,
    }
    total = 0.0
    current_num = ''
    for char in timeout:
        if char.isdigit() or char == '.':
            current_num += char
        elif char.isalpha() or char == ' ':
            if current_num:
                num = float(current_num)
                current_num = ''
            else:
                continue
            unit = ''
            if char.isalpha():
                unit = char
                # Collect full unit name
                for next_char in timeout[timeout.index(char) + 1:]:
                    if next_char.isalpha():
                        unit += next_char
                    else:
                        break
            if unit in factors:
                total += num * factors[unit]
    if current_num:
        total += float(current_num)
    return total


def _convert_delay(delay: Union[str, int, float, timedelta]) -> float:
    """Convert delay to seconds.

    :param delay: Delay in seconds, Robot Framework time format, or timedelta.
    :type delay: str, int, float, or timedelta
    :return: Delay in seconds.
    :rtype: float
    """
    return _convert_timeout(delay)
