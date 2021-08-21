from os import path

from youtube_dl import YoutubeDL

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError
ydl_opts = {
    "format": "bestaudio[ext=m4a]",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}

ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"لا استطيع تحميل فيديو بهذا الحجم"
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"لا استطيع تحميل فيديو بهذا الحجم"
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
