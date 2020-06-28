#!/usr/bin/python3
#
import datetime
import requests

URL = "https://infogram.io/p/10b3ab075a9851ccb46bbb86abd7cb54.png"

LOCALDIR = "/home/gbroiles/projects/bc-covid/images/"

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
}


def main():
    """Entry point if called as an executable"""
    timestamp = str(int(datetime.datetime.utcnow().timestamp()))

    r = requests.get(URL, headers=HEADERS)

    if r.status_code == 200:
        filename = LOCALDIR + timestamp + ".png"
        with open(filename, "wb") as fd:
            for chunk in r.iter_content(chunk_size=4096):
                fd.write(chunk)
    else:
        print(r.status_code)


if __name__ == "__main__":
    main()
