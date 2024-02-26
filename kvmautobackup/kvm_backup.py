#!/usr/bin/env python3
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

"""
Project Name: 'backup-kvm'
Version: 1.2

Description: Backup and restore script KVM VM

Ihor Cheberiak (c) 2021-2024
https://www.linkedin.com/in/ihor-cheberiak/
"""

import argparse


class KVMBackup:
    def __init__(self) -> None:
        pass


if __name__ == '__main__':
    help_parser = argparse.ArgumentParser(description="Backup and Restore Virtual Machines and Folders")
    help_parser.add_argument("-settings_name_json", type=str, default="settings.json", help="Example: settings.json")

    args_parser = help_parser.parse_args()
