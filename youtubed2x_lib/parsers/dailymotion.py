import re
from youtubed2x_lib.parsers import Parser_Helper


class Dailymotion_Parser (Parser_Helper):
    """Parser for Dailymotion pages. Updated 04/19/2009"""
    const_video_url_re = re.compile (r'^(?:http://)?(?:www\.)?dailymotion\.com/(?:\S+)?video/([\w-]+)')
    video_url_str = 'http://www.dailymotion.com/video/%s/'
    video_title_re = re.compile (r'vs_videotitle:"([\S ]+)",vs_user:')
    video_url_params_re = re.compile (r"addVariable\(\"video\", \"([\w\-%\.]+)%40%40spark%7C")
    video_url_real_str = "http://www.dailymotion.com%s"
    parser_type = "Dailymotion"

    def __init__ (self, video_id):
        super (Dailymotion_Parser, self).__init__ (video_id)


    def _parseRealURL (self, commands):
        """Get the real url for the video"""
        from urllib2 import unquote
        real_url = self.video_url_real_str % unquote (commands[0])
        return real_url

