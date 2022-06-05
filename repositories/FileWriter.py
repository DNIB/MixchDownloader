import os
from datetime import datetime

from requests import Response

from components.builders.PathBuilder import PathBuilder
from components.vo.MixchStreamMap import MixchStreamMap


class FileWriter:
    DEFAULT_FOLDER = "downloads"
    DEFAULT_COMPONENT_FOLDER = "components"
    DEFAULT_MAP = "map"

    def saveResponse(self, response: Response, folder_name: str, file_name: str):
        try:
            path = PathBuilder(self.DEFAULT_FOLDER)\
                .append(folder_name)\
                .append(self.DEFAULT_COMPONENT_FOLDER)\
                .append(file_name)\
                .getRaw()
            f = open(path, "wb")
            f.write(response.content)
            f.close()
        except FileNotFoundError:
            print("Folder not existed. Creating...")
            path = PathBuilder(self.DEFAULT_FOLDER)\
                .append(folder_name)\
                .append(self.DEFAULT_COMPONENT_FOLDER)\
                .getRaw()
            os.makedirs(path)

            self.saveResponse(response, folder_name, file_name)

    def saveStream(self, mixch_stream_map: MixchStreamMap):
        try:
            content = ""
            for fragment_name in mixch_stream_map.all():
                content += "file '" + self.DEFAULT_COMPONENT_FOLDER + "/" + fragment_name + "'\n"

            map_path = PathBuilder(self.DEFAULT_FOLDER)\
                .append(mixch_stream_map.getName())\
                .append(self.DEFAULT_MAP)\
                .getTxt()

            f = open(map_path, "w")
            f.write(content)
            f.close()

            now = int(datetime.today().timestamp())
            output_path = PathBuilder(self.DEFAULT_FOLDER)\
                .append(mixch_stream_map.getName())\
                .append(str(now) + "_" + mixch_stream_map.getName())\
                .getTs()

            command = "ffmpeg -f concat -safe 0 -i " \
                      + map_path \
                      + " -c copy " \
                      + output_path
            os.system(command)

        except FileNotFoundError:
            print("Folder not existed. Creating...")
            os.makedirs(self.DEFAULT_FOLDER + "/" + mixch_stream_map.getName())

            self.saveStream(mixch_stream_map)
