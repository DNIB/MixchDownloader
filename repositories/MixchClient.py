import requests
from requests import Response


class MixchClient:
    BASE_URL = "https://d2ibghk7591fzs.cloudfront.net/hls"

    def getMapFile(self, channel_id: int) -> Response:
        return self.getFile("torte_" + str(channel_id) + ".m3u8")

    def getFile(self, file_name: str) -> Response:
        return requests.get(self.BASE_URL + "/" + file_name)
