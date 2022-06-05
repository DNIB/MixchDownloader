from services.DownloadService import DownloadService

if __name__ == '__main__':
    channel_url = input("Please enter the url: ")

    url_fragments = channel_url.split("/")
    if "mixch.tv" not in url_fragments:
        print("Invalid url. Seem not from mixch.tv")
        exit(-1)

    channel_id = int(list(filter(lambda fragment: fragment.isnumeric(), url_fragments))[0])
    print("Downloading channel id: " + str(channel_id))

    downloadService = DownloadService()
    downloadService.downloadMixchStream(channel_id)
