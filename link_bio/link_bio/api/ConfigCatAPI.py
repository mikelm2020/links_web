import os
import dotenv
import configcatclient


class ConfigCatAPI:

    dotenv.load.dotenv()
    CONFIGCAT_SDK_KEY = os.environ.get("CONFIGCAT_SDK_KEY")

    def __init__(self) -> None:
        if self.CONFIGCAT_SDK_KEY is not None:
            self.configcat = configcatclient.get(self.CONFIGCAT_SDK_KEY)

    def schedule(self) -> str:
        self.configcat.get_value("live_schedule", "")
