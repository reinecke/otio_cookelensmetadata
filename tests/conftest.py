# Copyright 2020 Netflix, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from pathlib import Path

import pytest


SAMPLE_DATA_PATH = Path(__file__).parent / "sample_data"


@pytest.fixture
def sample_lmd_path():
    return SAMPLE_DATA_PATH / "lens-data-2020052713471590587226.yml"


@pytest.fixture
def sample_lmd_data():
    with open(SAMPLE_DATA_PATH / "lens-data-2020052713471590587226.yml") as f:
        return f.read()
