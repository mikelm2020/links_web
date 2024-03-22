import os
import dotenv
from supabase import create_client, Client
from link_bio.model.Featured import Featured


class SupabaseAPI:

    dotenv.load_dotenv()
    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    supabase: Client

    def __init__(self) -> None:
        self.supabase = None

    def create_client(self) -> Client:
        if self.supabase is None:
            self.supabase = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def featured(self):

        if self.supabase is None:
            self.create_client()

        response = (
            self.supabase.table("featured")
            .select("*")
            .order("init_date", desc=True)
            .limit(1)
            .execute()
        )
        featured_data = []

        if len(response.data) > 0:
            for featured_item in response.data:
                featured_data.append(
                    Featured(
                        title=featured_item["title"],
                        image=featured_item["image"],
                        url=featured_item["url"],
                    )
                )

        return featured_data
