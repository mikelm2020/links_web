import link_bio.constants as const
from link_bio.model.Live import Live

from .BaseAPI import BaseAPI
from .TwitchAPI import TwitchAPI

TWITCH_API = TwitchAPI()
BASE_API = BaseAPI()


async def repo() -> str:
    return const.REPO_URL


async def live(user: str) -> Live:
    return TWITCH_API.live(user)


async def featured():
    return BASE_API.featured()
