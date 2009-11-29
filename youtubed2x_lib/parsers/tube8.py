import re
import datetime
from youtubed2x_lib.parsers import Parser_Helper


class Tube8_Parser (Parser_Helper):
    """Parser for Tube8 pages. Updated 07/04/2009"""
    const_video_url_re = re.compile (r'^(?:http://)?(?:www\.)?tube8\.com/(\S+/\S+/\d+)(?:/)?$')
    video_url_str = 'http://www.tube8.com/%s/'
    video_title_re = re.compile (r'">([\S ]+)</h1>')
    video_url_params_re = re.compile (r'param name="FlashVars" value="videoUrl=(\S+)&amp;imageUrl=')
    parser_type = "Tube8"
    domain_str = "http://www.tube8.com/"
    host_str = "tube8.com"
    version = datetime.date (2009, 11, 28)


    def _parseRealURL (self, commands):
        """Get the real url for the video"""
        real_url = commands[0]
        return real_url


    @staticmethod
    def getImageData ():
        image_data = """\xff\xe9\xed\xff\xf4\xca\xce\xff\xfd\xff\xf5\xff\xfb\xff\xf6\xff\xff\xff\xf6\xff\xfe\xff\xf6\xff\xd2\xb6\xb5\xff\xff\xf8\xf6\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff\xfa\xf7\xf3\xff\xd6\xb8\xb8\xff\xf4\xd5\xd7\xff\xfe\xfc\xf9\xff\xfe\xf6\xf1\xff\xff\xf2\xf5\xff\x82ei\xff\xb5\xba\xb3\xff\x86\x8b\x84\xffPHE\xff\xc7\xc6\xc1\xff\x8dsv\xff\xff\xed\xee\xff\xea\xe9\xe0\xff\xf1\xf0\xe9\xff\xff\xff\xff\xff\xf2\xe9\xe2\xff\xa9\x8a\x8e\xff\xe5\xc4\xc6\xff\xff\xff\xff\xff\xfe\xfc\xf9\xff\xff\xfd\xfd\xff<23\xff\xa5\xae\xa9\xff\xb8\xbd\xb9\xffA=<\xff\')&\xffYOP\xff\xff\xff\xfd\xff_YV\xffxpm\xff\xb8\xbb\xb3\xff\xc4\xb7\xb3\xff\x9d\x83\x86\xff\xdd\xc3\xc5\xff\xfe\xf3\xf5\xff\xfe\xfc\xf9\xff\xf1\xf2\xf4\xff\xaa\xaa\xac\xff\x10\x1a\x19\xff\'10\xff\xc9\xd3\xd2\xff)85\xff\x00\x04\x02\xff\xf4\xff\xff\xffiba\xff\x19\r\x0e\xff\x0f\x0c\r\xff_YV\xff\xce\xb8\xbb\xff\xfe\xf3\xf5\xff\xf9\xed\xec\xff\xfa\xf7\xf3\xff\xbd\xbb\xbe\xff\xbe\xc2\xc3\xff &&\xffR^\\\xff\xe8\xf7\xf4\xff\x1d&%\xff\x00\x01\x02\xff\xf6\xf1\xf5\xffKJI\xff2.-\xff\x18\x1a\x1a\xff\t\x0b\x08\xffc][\xff\xf1\xf0\xe9\xff\xff\xff\xff\xff\xfa\xf7\xf3\xff\xff\xfe\xff\xff9=<\xff\x82|~\xff\\\\\\\xff\x8b\x89\x8a\xff\x1b\x06\r\xff \x05\x0e\xff\xd3\xa3\xb3\xffrut\xff=?>\xff!&#\xff\x08\x0f\r\xff\x18\x1a\x1a\xff\x94\x96\x96\xff\xf6\xfe\xfe\xff\xf6\xfe\xfa\xff\xfb\xfa\xf6\xff\xb8\xbd\xb7\xff\x0e\x00\x00\xff\x1f\x0c\x0e\xff\x12\x02\x03\xff#\x00\x07\xff\xce\xad\xb4\xff\xff\xdd\xeb\xff\xb8\xc2\xc0\xfft\x7fx\xff*32\xff\x11\x1e\x1b\xff\x03\x04\x04\xffNZW\xff\xef\xfb\xfa\xff\xf6\xfe\xfe\xff\xff\xff\xf8\xff\xf5\xfb\xf1\xff\xbe\xa1\xa3\xff\xf5\xdb\xdc\xff\xf3\xe4\xe1\xff\xff\xf7\xf8\xff\xff\xfe\xf8\xff\xff\xf6\xf5\xff\xda\xe8\xe5\xff\x83\x90\x8d\xff\x19)&\xff\x13#\x1f\xff\x03\x04\x04\xff*32\xff\xde\xed\xea\xff\xf6\xfe\xfe\xff\xb2\xb4\xb6\xffegg\xff\xac\xad\xab\xffBKI\xff)-*\xff\x96\x9e\x9b\xffT`^\xff\x83\x90\x8d\xff\xde\xed\xea\xff\x83\x90\x8d\xff )(\xff\x18\x1a\x1a\xff\x00\x00\x00\xff455\xff\xec\xeb\xec\xff\xff\xff\xff\xff\xdd\xdc\xdf\xffEFD\xffrut\xffUVV\xff=?>\xffopm\xff\x1a#!\xffT`^\xff\xd0\xd6\xd5\xffegg\xff\x1d\x1a\x1d\xff\x1e\x15\x15\xff\n\x02\x07\xffI8>\xff\xd8\xc1\xcb\xff\xfd\xf6\xf8\xff\xf5\xf4\xf5\xffjig\xff9<<\xffzxw\xffzxw\xffSON\xff`a_\xff\xa7\xa8\xa6\xff\x87\x88\x89\xff2.-\xff\x1c\x06\x0c\xff\x11\x01\x02\xff)\x10\x14\xff\x97t\x7f\xff\xd9\xab\xbb\xff\xd5\xa2\xb1\xff\xfe\xfc\xf9\xff\xc9\xc7\xc4\xff)-*\xff!&#\xffqfe\xff\x84yy\xff\x90\x8c\x89\xff_YV\xff\x1e\x15\x15\xff\x11\x01\x02\xff!\x01\x05\xff!\x01\x05\xffzW]\xff\xf7\xe0\xeb\xff\xfe\xdf\xf0\xff\xd8\x99\xaa\xff\xfe\xfc\xf9\xff\xff\xff\xff\xff\xb1\xb6\xb1\xff<:7\xff\x19\r\x0e\xff)\x10\x14\xff"\x12\x13\xff\x19\x04\x06\xff\x0b\x00\x00\xff\x11\x01\x02\xff+\x08\x0f\xffe=E\xff\xc2\xa4\xad\xff\xf9\xec\xf1\xff\xfb\xdb\xe9\xff\xdc\x9e\xad\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff\xfc\xfd\xf5\xff\xe0\xdd\xd8\xff~gi\xff3\x15\x18\xff2\x1c \xff7$#\xff>,,\xffyfe\xff\xaf\x90\x95\xff\xc6\xa8\xab\xff\xba\xa2\xa4\xff\xa8\x90\x92\xff\xd2\xab\xb6\xff\xec\xbe\xc4\xff\xfe\xfc\xf9\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfc\xf9\xff\xc6\xa8\xab\xff\xa6\x84\x86\xff\xe6\xcc\xcd\xff\xd9\xc9\xc8\xff\xed\xdb\xdb\xff\xfe\xf6\xf1\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff\xfa\xf7\xf3\xff\xfe\xfc\xf9\xff\xf9\xed\xec\xff\xfc\xfd\xf5\xff\xf6\xf6\xed\xff\xfc\xfd\xf5\xff\xfc\xfd\xf5\xff\xed\xcf\xce\xff\xe5\xc4\xc6\xff\xfe\xf6\xf1\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff\xfe\xf6\xf1\xff\xfe\xfc\xf9\xff\xfe\xf6\xf1\xff\xfc\xfd\xf5\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff\xfe\xfc\xf9\xff"""

        return image_data


