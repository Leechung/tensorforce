# Copyright 2017 reinforce.io. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
Default configuration for DQFD Agent and model.
"""

DQFDAgentConfig = {
    "expert_sampling_ratio": 0.01,
    "supervised_weight": 1.0,
    "expert_margin": 0.8,
    'batch_size': 32,
    'update_rate': 0.25,
    'target_network_update_rate': 0.0001,
    'min_replay_size': 5e4,
    'deterministic_mode': False,
    'use_target_network': False,
    'update_repeat': 1
}