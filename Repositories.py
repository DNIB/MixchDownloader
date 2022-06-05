import os

import requests
from requests import Response


class MixchClient:
    BASE_URL = "https://d2ibghk7591fzs.cloudfront.net/hls"

    def getMapFile(self, channel_id: int) -> Response:
        return self.getFile("torte_" + str(channel_id) + ".m3u8")

    def getFile(self, file_name: str) -> Response:
        return requests.get(self.BASE_URL + "/" + file_name)


class FileWriter:
    DEFAULT_FOLDER = "downloads"

    def saveResponse(self, response: Response, folder_name: str, file_name: str):
        try:
            f = open(self.DEFAULT_FOLDER + "/" + folder_name + "/" + file_name, "wb")
            f.write(response.content)
            f.close()
        except FileNotFoundError:
            print("Folder not existed. Creating...")
            os.makedirs("downloads/" + folder_name)

            self.saveResponse(response, folder_name, file_name)
