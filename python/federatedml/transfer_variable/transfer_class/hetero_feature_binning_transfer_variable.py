#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

################################################################################
#
# AUTO GENERATED TRANSFER VARIABLE CLASS. DO NOT MODIFY
#
################################################################################

from federatedml.transfer_variable.base_transfer_variable import BaseTransferVariables


# noinspection PyAttributeOutsideInit
class HeteroFeatureBinningTransferVariable(BaseTransferVariables):
    def __init__(self, flowid=0):
        super().__init__(flowid)
        self.bucket_idx = self._create_variable(name='bucket_idx', src=['guest'], dst=['host'])
        self.encrypted_bin_sum = self._create_variable(name='encrypted_bin_sum', src=['host'], dst=['guest'])
        self.optimal_info = self._create_variable(name='optimal_info', src=['host'], dst=['guest'])
        self.encrypted_label = self._create_variable(name='encrypted_label', src=['guest'], dst=['host'])
        self.paillier_pubkey = self._create_variable(name='paillier_pubkey', src=['guest'], dst=['host'])
        self.transform_stage_has_label = self._create_variable(
            name="transform_stage_has_label", src=['guest'], dst=['host'])
        self.host_anonymous_header_dict = self._create_variable(name='host_anonymous_header_dict',
                                                                src=['host'],
                                                                dst=['guest'])
