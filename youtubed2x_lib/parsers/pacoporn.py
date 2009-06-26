import re
from youtubed2x_lib.parsers import Parser_Helper, getPage


class PacoPorn_Parser (Parser_Helper):
    """Parser for PacoPorn pages. Updated 06/03/2009"""
    const_video_url_re = re.compile (r'^(?:http://)?(?:www\.)?pacoporn\.com/viewVideo\.php\?video_id=(\d+)(?:&title=(\S+))?')
    domain_str = "http://www.pacoporn.com/"
    video_url_str = 'http://www.pacoporn.com/viewVideo.php?video_id=%s'
    video_details_url_str = "http://www.pacoporn.com/videoConfigXmlCode.php?pg=video_%s_no_0"
    video_title_re = re.compile (r'TEXT Name=\"Header\" Value=\"([\S ]+)\" Enable=')
    video_url_params_re = re.compile (r'PLAYER_SETTINGS Name=\"FLVPath\" Value=\"(\S+)\"')
    parser_type = "PacoPorn"
    host_str = "pacoporn.com"


    def __init__ (self, video_id):
        super (PacoPorn_Parser, self).__init__ (video_id)


    def getVideoPage (self, account="", password=""):
        page, newurl = getPage (self.__class__.video_details_url_str % self.video_id)
        return page, newurl


    def _parseRealURL (self, commands):
        """Get the real url for the video"""
        real_url = commands[0]
        return real_url


    @staticmethod
    def getImageData ():
        image_data = """&s\xae\xff&s\xae\xff&s\xae\xff&s\xae\xff&s\xae\xff&s\xae\xff"p\xac\xff\x1ak\xa9\xff\x19j\xa9\xff\x19j\xa9\xff\x1en\xab\xff(r\xaa\xfffeZ\xff\xafo7\xff\xe1\x8bB\xff\xf8\x96H\xff&s\xae\xff&s\xae\xff&s\xae\xff&s\xae\xff$q\xad\xff5}\xb3\xff\xb2\xcd\xe2\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xd9\xe6\xf0\xff_\x94\xba\xff;o\x8e\xffP|\x92\xffv\x85\x84\xff\x9c\x8bs\xff&s\xae\xff&s\xae\xff&s\xae\xff\x1fn\xab\xff|\xaa\xcd\xff\xff\xff\xff\xff\x95\xba\xd7\xff)u\xaf\xff\x18j\xa9\xff\x16h\xa8\xfff\x9c\xc6\xff\xff\xff\xff\xff\x9a\xbd\xda\xff!n\xac\xff$o\xad\xffi~\x81\xff%r\xae\xff%r\xae\xff"p\xac\xff\x8d\xb5\xd4\xff\xff\xff\xff\xffN\x8c\xbd\xff"p\xad\xff%r\xad\xff<\x81\xb6\xff\xdc\xe8\xf2\xff\xa6\xc6\xde\xff\xbd\xd4\xe6\xff\xff\xff\xff\xff:r\x9d\xffmbR\xff\xaep6\xff$q\xad\xff$q\xad\xff9\x7f\xb5\xff\xff\xff\xff\xff\xa3\xc3\xdd\xff o\xab\xff#q\xad\xffG\x88\xba\xff\xff\xff\xff\xff\xff\xff\xff\xff-w\xb0\xff\xb5\xce\xe3\xff\xff\xff\xff\xff\x9a\x8c{\xff\xa5m3\xff\xce\x84=\xff\x1em\xab\xff\x1dm\xab\xff\x8f\xb6\xd5\xff\xff\xff\xff\xffk\x9f\xc8\xff n\xac\xff\x14f\xa7\xff\xe7\xef\xf6\xff\xfe\xfe\xfe\xff\xd5\xe4\xef\xff\t_\xa3\xff\xe8\xf0\xf6\xff\xff\xff\xff\xffA\x81\xb3\xffKq\x87\xff\xc5\x89K\xff\x00X\x9f\xff\x00X\x9e\xffg\x9d\xc6\xff\xff\xff\xff\xff\xdf\xea\xf3\xff\x1dm\xaa\xff(t\xae\xff\xff\xff\xff\xff\xff\xff\xff\xff\xa1\xc2\xdc\xffk\x9f\xc8\xff\xff\xff\xff\xff\xe5\xef\xf6\xff\x00Y\xa0\xff\x0ba\xa4\xff\x1bc\x9a\xff\x00Z\xa0\xff\x00Z\xa0\xff\x15g\xa7\xff\xff\xff\xff\xff\xc0\xd6\xe7\xff\x1bl\xaa\xffN\x8c\xbd\xff\xff\xff\xff\xff\xff\xff\xff\xffd\x9b\xc5\xff\xe7\xef\xf6\xff\xdb\xe9\xf3\xff/Um\xff8EE\xffKJ=\xff~U%\xff\x00Z\xa0\xff\x00Z\xa0\xff\x00Z\xa0\xff\x00P\x9a\xff\x00U\x9d\xff\x00Y\x9f\xff\x84\xaf\xd1\xff\xfe\xfe\xfe\xff\xff\xff\xff\xffE\x87\xba\xff\x00R\x9b\xff\x00S\x9c\xff\x10S\x84\xff|P\x18\xff\xa4c\x15\xff\xbbo\x1a\xff\x00Y\x9f\xff\x00Z\xa0\xff\x00Z\xa0\xff\x00Z\xa0\xff\x00Z\xa0\xff\x00V\x9d\xff\xb4\xce\xe2\xff\xff\xff\xff\xff\xff\xff\xff\xff\'s\xae\xff\x00Y\x9e\xff\x00Z\xa0\xff\x00Z\xa1\xff$Z~\xff\xc6y\x1d\xff\xe8\x8b \xff\x00Y\x9f\xff\x00X\x9f\xff\x00O\x9a\xff\x00Z\xa0\xff\x00Z\xa0\xff\x00P\x9a\xff\xf3\xf7\xfa\xff\xff\xff\xff\xff\xf5\xf8\xfb\xff\x00P\x9a\xff\x17Lo\xff Id\xff\x07V\x92\xff\x00Y\xa4\xffaeW\xff\xe9\x8b\x1f\xff\x00S\x9b\xff{\xa7\xcb\xff\xff\xff\xff\xff\x00O\x99\xff\x00X\x9f\xff\x10d\xa6\xff\xff\xff\xff\xff\xff\xff\xff\xff\x84\xaf\xd1\xff\x00X\x9f\xff\x0fR\x84\xffqN\x15\xfftP\x1b\xfffS0\xff{b8\xff\xd8\x83\x1e\xffP\x8a\xb2\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00O\x99\xff\x04Y\x98\xffj\x9e\xc4\xff\xff\xff\xff\xff\xee\xf1\xf1\xff\x1fZs\xff\x00U\x9e\xff\x00Z\xa4\xff~e+\xff\xbdw\x18\xff\xc0x\x18\xff\xc7z\x1a\xff\xe2\x8a\x1f\xff\x87qJ\xff\xff\xff\xff\xff\xff\xff\xff\xff\x1bi\xa9\xffn\x89\x89\xff\xff\xff\xff\xff\xe6\xef\xf5\xff\x1d`\x84\xffmI\r\xff1^i\xff\x00U\xa2\xffciK\xff\xd6\x87\x1a\xff\xee\x94\x1f\xff\xf0\x94 \xff\xf4\x93!\xff\xack\x11\xff\xb8\xa1q\xff\xbb\xd1\xe4\xff\xd3\xdf\xe3\xff\xe3\xd7\xc7\xff\x9b\xa5\x97\xff\x00N\x9a\xff%^t\xff\x9be\x10\xff\xa7m\x13\xff_cF\xffcmP\xff\xd6\x86\x19\xff\xf6\x99!\xff\xfa\x99!\xff\xfa\x97"\xff\xe4\x90\x1d\xff\xb7\x860\xff\x08\\\x94\xffkT\x1e\xff\xa5j\r\xff\xb0z\x1c\xff\x16_\x8d\xffNbO\xff\xb9x\x14\xff\xdc\x8f\x1b\xff\xcb\x81\x17\xff\xc5|\x16\xff\xe0\x8c\x1d\xff\xf7\x99 \xff\xfa\x98"\xff\xfa\x96#\xff"""

        return image_data


