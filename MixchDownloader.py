from Services import DownloadService

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    channel_url = input("Please enter the url: ")

    url_fragments = channel_url.split("/")
    if "mixch.tv" not in url_fragments:
        print("Invalid url. Seem not from mixch.tv")
        exit(-1)

    channel_id = int(list(filter(lambda fragment: fragment.isnumeric(), url_fragments))[0])

    downloadService = DownloadService()
    downloadService.downloadMixchStream(channel_id)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
