from urlparse import urlparse
from urllib import urlopen

from captionstransformer.registry import REGISTRY

YOUTUBE_TIMEDTEXT = "http://video.google.com/timedtext?lang=%(lang)s&v=%(vid)s"


def get_video_id(url):
    """Return the video ID if the url is a video from youtube.
    Return None if not a youtube URL."""
    parsed = urlparse(url)
    domain = parsed.netloc == 'www.youtube.com'
    scheme = parsed.scheme in ('http', 'https')
    path = parsed.path == '/watch'
    qs = parsed.query
    params = dict([x.split("=") for x in qs.split("&")])
    vid = params.get('v', False)

    if not (domain and scheme and path and vid):
        return

    return vid


def get_captions(url, language):
    """Download captions from youtube. Return a list of core.Caption"""
    youtube = get_video_id(url)

    if youtube:
        #download caption and save it to extra
        reader = get_reader(url, language)
        if reader:
            captions = reader.read()
            return captions

    return []


def get_reader(url, language):
    youtube = get_video_id(url)

    if youtube:
        #download caption and save it to extra
        url = YOUTUBE_TIMEDTEXT % {'lang': language,
                                   'vid': youtube}
        try:
            flike = urlopen(url)
            reader = REGISTRY['transcript']['reader'](flike)
        except IOError:
            reader = None
    else:
        reader = None

    return reader
