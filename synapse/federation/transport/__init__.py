# -*- coding: utf-8 -*-
# Copyright 2014-2016 OpenMarket Ltd
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

"""The transport layer is responsible for both sending transactions to remote
homeservers and receiving a variety of requests from other homeservers.

By default this is done over HTTPS (and all homeservers are required to
support HTTPS), however individual pairings of servers may decide to
communicate over a different (albeit still reliable) protocol.
"""
