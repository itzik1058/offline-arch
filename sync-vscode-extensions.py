#!/usr/bin/env python3

from pathlib import Path
# from time import sleep
# from urllib.request import urlretrieve
# from urllib.error import HTTPError
from subprocess import run
import webbrowser

extension_dir = Path("vsc-extensions")
base_uri = "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/"
target_platform = "linux-x64"


def try_download(url: str, path: Path):
    webbrowser.open(url)
    return False
    # for _ in range(5):
    #     try:
    #         print(f"attempt to retrieve {url}")
    #         urlretrieve(url, path)
    #         return True
    #     except HTTPError:
    #         sleep(1)
    # return False


if __name__ == "__main__":
    sp = run(
        ["code", "--list-extensions", "--show-versions"],
        capture_output=True,
    )
    sp.check_returncode()
    for extension in sp.stdout.decode().splitlines():
        publisher, info = extension.split(".", 1)
        name, version = info.split("@", 1)
        url = f"{base_uri}{publisher}/vsextensions/{name}/{version}/vspackage"
        path = extension_dir / f"{publisher}.{name}-{version}.vsix"
        if path.is_file():
            continue
        if try_download(f"{url}?targetPlatform={target_platform}", path):
            print(f"{extension}?targetPlatform={target_platform}")
        elif try_download(url, path):
            print(extension)
        else:
            print(f"Failed to download {extension}")
