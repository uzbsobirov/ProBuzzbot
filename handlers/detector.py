import slugify

from typing import Union

from keyboards.default.start import start, start_admin
from data.config import ADMINS


async def detect_is_admin(user_id: Union[str, int]):
    if user_id == int(ADMINS[0]):
        return start_admin
    else:
        return start


def detect_which_messenger(text):
    if 'telegram' in text.lower():
        return 'telegram'

    elif 'instagram' in text.lower():
        return 'instagram'

    elif 'tiktok' in text.lower():
        return 'tiktok'

    elif 'youtube' in text.lower():
        return 'youtube'

    else:
        return False


def create_slug(text):
    slug = slugify.slugify(text)
    return slug
