from typing import Union

from keyboards.default.start import start, start_admin
from data.config import ADMINS


async def detect_is_admin(user_id: Union[str, int]):
    if user_id == int(ADMINS[0]):
        return start_admin
    else:
        return start
