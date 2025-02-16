import os
from yt_dlp import YoutubeDL
from colorama import Fore, Style


def download_youtube_audio(url: str, yt_dlp_options: dict) -> bool:
    try:
        with YoutubeDL(yt_dlp_options) as ydl:
            ydl.download([url])
            return True
    except Exception as e:
        return False


def batch_download_youtube_audio(urls: list[str], yt_dlp_options: dict) -> None:
    for i in range(len(urls)):
        title = extract_title_from_url(urls[i], yt_dlp_options)
        print(f"{Fore.CYAN}[{i + 1}/{len(urls)}] Downloading: {title}{Style.RESET_ALL}")
        
        success = download_youtube_audio(urls[i], yt_dlp_options)
        if success:
            print(f"{Fore.GREEN}[{i + 1}/{len(urls)}] Downloading: {title} - success!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[{i + 1}/{len(urls)}] Downloading:  {title} failed.{Style.RESET_ALL}")


def extract_title_from_url(url: str, yt_dlp_options: dict) -> str:
    try:
        with YoutubeDL(yt_dlp_options) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get("title", "Unknown Title")
            return title
    except Exception as e:
        return "Unknown Title"


def get_single_song_from_url(url: str) -> str:
    # song is single
    if "&" not in url:
        return url

    end_index = url.index("&")
    return url[:end_index]


def get_links_from_file(file_path_with_links: str) -> list[str]:
    try:
        with open(file_path_with_links, "r") as file:
            return [url.strip() for url in file]
    except FileNotFoundError:
        return []


def main(file_path_with_links: str, output_dir: str, download_playlists_too=False) -> None:
    # yt-dlp options for downloading audio
    ydl_opts = {
        "format": "bestaudio/best",
        # os.path.join(output_directory, "%(title)s.%(ext)s")
        # output_directory - where it will be saved
        # %(title)s.%(ext)s - name of the file after download.
        "outtmpl": os.path.join(output_directory, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    links_from_file = get_links_from_file(file_path_with_links)
    if not links_from_file:
        print(f"{Fore.RED}Empty file or file not found. File name: ({file_path_with_links}){Style.RESET_ALL}")
        print(f"{Fore.RED}Nothing to download. Exiting...{Style.RESET_ALL}")
        return

    for url in links_from_file:
        if not download_playlists_too:
            url = get_single_song_from_url(url)

        batch_download_youtube_audio([url], ydl_opts)


if __name__ == "__main__":
    text_file_path_with_urls = "links.txt.example"
    # songs will be saved at - disk D/youtube_songs folder
    output_directory = "/mnt/d/youtube_songs"
    main(text_file_path_with_urls, output_directory, download_playlists_too=False)