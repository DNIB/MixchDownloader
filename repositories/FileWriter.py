import os

from requests import Response

from components.vo.MixchStreamMap import MixchStreamMap


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

    def saveStreamMap(self, mixch_stream_map: MixchStreamMap):
        try:
            f = open(self.DEFAULT_FOLDER + "/" + mixch_stream_map.getName() + "/map.txt", "a")
            for fragment_name in mixch_stream_map.all():
                f.write("file '" + fragment_name + "'\n")
            f.close()
        except FileNotFoundError:
            print("Folder not existed. Creating...")
            os.makedirs("downloads/" + mixch_stream_map.getName())

            self.saveStreamMap(mixch_stream_map)
