import reflex as rx
from link_bio.api.api import featured
from link_bio.model.Featured import Featured


USER = "mikelm2024"


class PageState(rx.State):

    featured_info: list[Featured]

    async def featured_links(self):
        self.featured_info = await featured()
