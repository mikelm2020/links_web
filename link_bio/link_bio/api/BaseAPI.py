import link_bio.constants as const
from link_bio.model.Featured import Featured


class BaseAPI:
    def featured(self):
        featured_data = []
        featured_data.append(
            Featured(title=const.BASE_TITLE, image=const.BASE_IMAGE, url=const.BASE_URL)
        )

        return featured_data
