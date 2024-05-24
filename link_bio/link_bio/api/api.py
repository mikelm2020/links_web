import link_bio.constants as const
from link_bio.model.Live import Live

from .SupabaseAPI import SupabaseAPI
from .TwitchAPI import TwitchAPI

TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()


async def repo() -> str:
    return const.REPO_URL


async def live(user: str) -> Live:
    return TWITCH_API.live(user)


async def featured():
    return SUPABASE_API.featured()
