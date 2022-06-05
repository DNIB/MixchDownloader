import time

from HttpCode import HttpCode
from components.vo.MixchStreamMap import MixchStreamMap
from repositories.FileWriter import FileWriter
from repositories.MixchClient import MixchClient


class DownloadService:
    def __init__(self):
        self.mixch_client = MixchClient()
        self.file_writer = FileWriter()

    def downloadMixchStream(self, channel_id: int):
        stream_map = MixchStreamMap(str(channel_id))
        while True:
            map_request = self.mixch_client.getMapFile(channel_id)
            if map_request.status_code != HttpCode.OK.value:
                print("Download finished")
                return

            file_name = map_request.content.decode("utf-8").split("\n")[-2]
            if file_name == stream_map.last():
                continue
            stream_map.append(file_name)
            print("Downloading: " + file_name)

            file_response = self.mixch_client.getFile(file_name)
            if file_response.status_code != HttpCode.OK.value:
                print("Warning: Unexpected Response Code - " + str(file_response.status_code))
                return

            self.file_writer.saveResponse(file_response, str(channel_id), file_name)
            time.sleep(1)

        print("Download finish")
        if stream_map.isNotEmpty():
            self.file_writer.saveStream(stream_map)
