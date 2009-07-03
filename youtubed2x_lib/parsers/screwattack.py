import re
from youtubed2x_lib.parsers import Parser_Helper, getPage


class ScrewAttack_Parser (Parser_Helper):
    """Parser for ScrewAttack pages. Updated 06/26/2009"""
    const_video_url_re = re.compile (r'^(?:http://)?(?:www\.)?screwattack\.com/(\S+)')
    video_url_str = 'http://www.screwattack.com/%s'
    video_title_re = re.compile (r'<h1 class="title">([^<]*)</h1>')
    video_url_params_re = re.compile (r"gr.vau.videoURL = '(\S+)'")
    video_url_hq_params_re = re.compile (r"gr.vau.videoURLHQ = '(\S+)'")
    embed_file_extensions = {"video/mp4": "mp4"}
    parser_type = "ScrewAttack"
    host_str = "screwattack.com"

    def __init__ (self, video_id):
        super (ScrewAttack_Parser, self).__init__ (video_id)
        self.embed_file_type = "video/mp4"


    def _parsePlayerCommands (self, page_dump):
        """Get the commands needed to get the video player"""
#        match = self.__class__.video_url_hq_params_re.search (page_dump)
#        if match:
#            commands = match.groups ()
#            return commands
#        else:
#            commands = None

        match = self.__class__.video_url_params_re.search (page_dump)
        if not match:
            raise self.__class__.InvalidCommands ("Could not find flash player commands")
        else:
            commands = match.groups ()
        return commands


    def _parseRealURL (self, commands):
        """Get the real url for the video"""
        secondary_url = commands[0]
        # Follow redirect
        page, real_url = getPage (secondary_url, read_page=False)
#        print real_url
        return real_url


    @staticmethod
    def getImageData ():
        image_data = """\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xfb\xfb\xff\xe3\xe3\xe4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xfb\xfb\xfa\xff\xde\xdf\xe0\xff\xad\xad\xb2\xff\xcc\xcc\xca\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xcf\xce\xcb\xff\xb7\xb6\xc4\xff\xa8\xa7\xb7\xff\xd3\xd3\xd4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xec\xec\xea\xff\x91\x90\x97\xff\xbd\xbc\xdc\xff\xa9\xa8\xc2\xff\xd5\xd5\xd4\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfc\xfc\xfc\xff\xf6\xf6\xf6\xff\xa5\xa5\xa5\xff\x84\x83\x92\xff\xcd\xcc\xef\xff\xa3\xa2\xb6\xff\xd1\xd1\xce\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xe2\xe2\xe1\xff\xaa\xaa\xab\xff\x80\x80\x8b\xff\xa5\xa4\xbd\xff\xcd\xcc\xf0\xff\xa4\xa3\xb8\xff\xd4\xd4\xd3\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xbe\xbd\xbe\xffyw\x7f\xff\x9d\x9b\xb5\xff\xc2\xc1\xe3\xff\xc8\xc7\xec\xff\xa4\xa4\xbc\xff\xc7\xc7\xc7\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xcc\xcb\xcc\xff|{\x90\xff\xcc\xcb\xf0\xff\xc2\xc1\xe4\xff\xc3\xc2\xe5\xff\xb1\xb0\xcf\xff\xa8\xa8\xac\xff\xfa\xfa\xfa\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xf5\xf5\xf5\xff\x84\x82\x8b\xff\xbe\xbd\xdf\xff\xc2\xc1\xe4\xff\xc2\xc1\xe4\xff\xc8\xc7\xea\xffom}\xff\xe9\xe9\xea\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xbb\xbb\xbd\xff\xa4\xa3\xbf\xff\xc3\xc2\xe5\xff\xc1\xc0\xe3\xff\xcb\xca\xee\xff\xa8\xa7\xc4\xffoms\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xb9\xb9\xbb\xff\xa4\xa3\xbd\xff\xc1\xc0\xe3\xff\xcd\xcd\xf1\xff\xc4\xc3\xe6\xffvt\x87\xffD@@\xff\xf7\xf7\xf7\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xd3\xd3\xd3\xff\x91\x90\xa5\xff\xcf\xce\xf3\xff\xd3\xd2\xf8\xff\x97\x90\xb0\xffHFH\xff\xa5\xa4\xa4\xff\xef\xef\xef\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe4\xe3\xe4\xff\x84\x83\x95\xff\xdb\xda\xff\xff\xb4\xb3\xd1\xffebl\xff\x87\x87\x87\xff\xfb\xfb\xfb\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe3\xe3\xe4\xff\x9f\x98\xaf\xff\xbf\xbe\xdd\xff\x98\x96\xa5\xff\x99\x97\x98\xff\xec\xec\xeb\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe7\xe7\xe6\xff\x8d\x8b\x9a\xff\xa8\xa7\xb8\xff\xc1\xc0\xc5\xff\xe3\xe2\xe1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xef\xef\xf0\xff\x8a\x88\x8c\xff\xc5\xc4\xc8\xff\xf5\xf5\xf5\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"""

        return image_data

