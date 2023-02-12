# Copyright © 2023-2024 by piroxpower@Github, < https://github.com/piroxpower >.
#
# This file is part of < https://github.com/Team-Deadly/MusicUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Deadly/MusicUserbot/blob/main/LICENSE >
#
# All rights reserved ®.

from typing import Dict, List, Union

admins: Dict[int, List[int]] = {}


def set(chat_id: int, admins_: List[int]):
    admins[chat_id] = admins_


def get(chat_id: int) -> Union[List[int], bool]:
    if chat_id in admins:
        return admins[chat_id]

    return False
