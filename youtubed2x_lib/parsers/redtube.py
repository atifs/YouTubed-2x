import re
from youtubed2x_lib.parsers import Parser_Helper, getPage


class RedTube_Parser (Parser_Helper):
    """Parser for RedTube pages. Updated 06/14/2009"""
    const_video_url_re = re.compile (r'^(?:http://)?(?:www\.)?redtube\.com/(\d+)$')
    domain_str = "http://www.redtube.com/"
    video_url_str = 'http://www.redtube.com/%s'
    video_url_real_str = 'http://dl.redtube.com/_videos_t4vn23s9jc5498tgj49icfj4678/%s/%s.flv'
    video_title_re = re.compile (r'<h1 class=\'videoTitle\'>([^<]*)</')
    # Mapped translation characters
    video_map_table = ['R', '1', '5', '3', '4', '2', 'O', '7', 'K', '9', 'H', 'B', 'C', 'D', 'X', 'F', 'G', 'A', 'I', 'J', '8', 'L', 'M', 'Z', '6', 'P', 'Q', '0', 'S', 'T', 'U', 'V', 'W', 'E', 'Y', 'N']
    parser_type = "RedTube"
    host_str = "redtube.com"

    def __init__ (self, video_id):
        super (RedTube_Parser, self).__init__ (video_id)


    # TODO: Fix to use dynamic expires date
    def getVideoPage (self, account="", password=""):
        page, newurl = getPage (self.page_url, additional_headers={"Cookie": r'pp="1"; expires="Fri, 16-Dec-2011 02:15:58 PM"; path="/"; domain=.redtube.com; secure=""'}) # Should use a dynamic date
        return page, newurl


    def _parsePlayerCommands (self, page_dump):
        """Get the parent folder index number and file index number for the download url"""
        # Weird ass algorithm used to help figure out the path for the .flv file.
        # Python interpretation of algorithm used for RedTube Downloader

        video_id = int (self.video_id) # Typecast from string (ex. 752)
        parent_index = "%.7d" % (video_id/1000) # 7-digit num. with quotient (int division) padded with 0s (ex. '0000000')
        subindex = "%.7d" % video_id # 7-digit id padded with 0s (ex. '0000752')

        # Add all the results from multiplying integer components of each subindex by i+1
        # and place the string representation in helper. Result is '79' in example
        temp = 0
        for i in range (7):
            temp += int (subindex[i]) * (i+1)
        helper = str (temp)

        # Add integer components of helper. Result is 16 in example
        temp = 0
        for i in helper:
            temp += int (i)

        # 2-digit string that holds the 2nd and 7th characters characters for the file id
        helper = "%.2d" % temp # (ex. '16')
        # Translate the original video id number into the proper file id code
        # Result of example is the string 'J6IA0L1UM'
        file_id = ''
        file_id += self.video_map_table[ord(subindex[3]) - 48 + temp + 3] # table[48-48+16+3] = table[19] = 'J'
        file_id += helper[1] # '6'
        file_id += self.video_map_table[ord(subindex[0]) - 48 + temp + 2] # table[48-48+16+2] = table[18] = 'I'
        file_id += self.video_map_table[ord(subindex[2]) - 48 + temp + 1] # table[48-48+16+1] = table[17] = 'A'
        file_id += self.video_map_table[ord(subindex[5]) - 48 + temp + 6] # table[53-48+16+6] = table[27] = '0'
        file_id += self.video_map_table[ord(subindex[1]) - 48 + temp + 5] # table[48-48+16+5] = table[21] = 'L'
        file_id += helper[0] # '1'
        file_id += self.video_map_table[ord(subindex[4]) - 48 + temp + 7] # table[55-48+16+7] = table[30] = 'U'
        file_id += self.video_map_table[ord(subindex[6]) - 48 + temp + 4] # table[50-48+16+4] = table[22] = 'M'
        commands = (parent_index, file_id)
        return commands


    def _parseRealURL (self, commands):
        """Get the real url for the video"""
        real_url = self.video_url_real_str % commands
        return real_url


    @staticmethod
    def getImageData ():
        image_data = """\xff\xfa\xfa\xff\xf6sw\xff\xf4]b\xff\xf6_c\xff\xf8\\b\xff\xf8]c\xff\xf5Y_\xff\xf3T[\xff\xf3QV\xff\xf3PT\xff\xf2HN\xff\xf1BG\xff\xef<A\xff\xedAG\xff\xf0bf\xff\xff\xfa\xfa\xff\xf5sx\xff\xf6\\b\xff\xf6^e\xff\xf4`f\xff\xf8^c\xff\xf7Z]\xff\xf6V\\\xff\xf5QW\xff\xf3JP\xff\xf2GJ\xff\xf1@F\xff\xef7=\xff\xef18\xff\xeb*1\xff\xea#)\xff\xefW\\\xff\xf3\\`\xff\xf7[_\xff\xf7\\b\xff\xf5^b\xff\xf7in\xff\xf8kq\xff\xf7gl\xff\xf5ag\xff\xf5Y_\xff\xf2NT\xff\xef>E\xff\xee.4\xff\xec\'-\xff\xea &\xff\xea\x1c#\xff\xe9-3\xff\xf4[a\xff\xf6[b\xff\xf6\\a\xff\xf8kp\xff\x10\n\n\xff\x07\x04\x04\xff\x07\x04\x04\xff\x07\x04\x04\xff\t\x05\x06\xff\x1e\x11\x11\xff}78\xff\xee>D\xff\xeb \'\xff\xe9\x19 \xff\xe6\x14\x1b\xff\xe3\x10\x17\xff\xf4X]\xff\xf4X]\xff\xf6V\\\xff\xf6kp\xff\x02\x01\x01\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xffJ"$\xff\xea+1\xff\xe7\x14\x1b\xff\xe4\x10\x17\xff\xe1\x0c\x13\xff\xf2QW\xff\xf2PV\xff\xf2MS\xff\xf5hm\xff\x02\x01\x01\xff\x00\x00\x00\xff\x04\x03\x03\xffn9;\xffS+,\xff\x02\x01\x01\xff\x00\x00\x00\xff\x00\x00\x00\xff\xe1:>\xff\xe4\x0f\x16\xff\xe1\x0c\x13\xff\xdf\n\x11\xff\xf2JP\xff\xf2JO\xff\xf1GM\xff\xf2`e\xff\x02\x01\x01\xff\x00\x00\x00\xff\x0b\x06\x06\xff\xf0bg\xff\xef_d\xff\x1d\x10\x11\xff\x00\x00\x00\xff\x00\x00\x00\xff\xbb48\xff\xe3\r\x14\xff\xdf\x08\x0f\xff\xdd\x06\r\xff\xf0DI\xff\xefCI\xff\xefBH\xff\xf1\\b\xff\x02\x01\x01\xff\x00\x00\x00\xff\x01\x00\x00\xff\x1a\x0e\x0f\xff\x0e\x08\x08\xff\x00\x00\x00\xff\x00\x00\x00\xff\x06\x03\x03\xff\xe5-3\xff\xe2\t\x10\xff\xde\x05\x0c\xff\xd9\x05\x0c\xff\xed=C\xff\xec;B\xff\xec;A\xff\xefU[\xff\x02\x01\x01\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\x00\x00\x00\xff\n\x05\x06\xff\xb9<@\xff\xe5\x12\x19\xff\xde\x04\x0b\xff\xda\x03\n\xff\xd5\x02\t\xff\xeb3:\xff\xeb29\xff\xeb/6\xff\xefNR\xff\x02\x01\x01\xff\x00\x00\x00\xff\x04\x02\x02\xffN*+\xff\x00\x00\x00\xff\x00\x00\x00\xff\x11\t\t\xff\xe95:\xff\xdf\x03\n\xff\xd9\x01\x08\xff\xd4\x01\x08\xff\xcf\x01\x08\xff\xea)0\xff\xea)/\xff\xeb&,\xff\xeeDJ\xff\x02\x01\x01\xff\x00\x00\x00\xff\n\x05\x06\xff\xefRW\xff\x16\x0b\x0b\xff\x00\x00\x00\xff\x00\x00\x00\xffr*,\xff\xdc\x11\x15\xff\xd4\x00\x04\xff\xcd\x00\x04\xff\xc8\x00\x06\xff\xe7\x1f%\xff\xe6\x1c#\xff\xe6\x18\x1f\xff\xea;A\xff\x02\x01\x01\xff\x00\x00\x00\xff\n\x05\x05\xff\xe817\xff\x9d35\xff\x00\x00\x00\xff\x00\x00\x00\xff\x05\x02\x02\xff\xcf00\xff\xcb\x03\x05\xff\xc4\x00\x03\xff\xc2\x00\x02\xff\xe2\x16\x1d\xff\xe0\x13\x1a\xff\xde\x0f\x16\xff\xe2,2\xff\x02\x01\x01\xff\x00\x00\x00\xff\n\x04\x04\xff\xd8 #\xff\xd6 #\xff\x1d\r\x0e\xff\x00\x00\x00\xff\x00\x00\x00\xff@\x16\x16\xff\xc2\r\x0e\xff\xbc\x00\x00\xff\xb9\x00\x00\xff\xd9\r\x14\xff\xd8\r\x14\xff\xd5\x08\x0f\xff\xd2\x0c\x13\xff\xd3&,\xff\xd4,1\xff\xcf $\xff\xc7\x07\x08\xff\xc3\x04\x05\xff\xc7\x1c\x1d\xff\xcc++\xff\xc6))\xff\xbf\x16\x16\xff\xb8\x03\x03\xff\xb0\x00\x00\xff\xae\x00\x00\xff\xe1LQ\xff\xd1\x07\x0e\xff\xc9\x04\x0b\xff\xc5\x03\n\xff\xc3\x02\t\xff\xbf\x00\x04\xff\xbb\x00\x02\xff\xb9\x00\x02\xff\xb8\x00\x01\xff\xb4\x00\x00\xff\xb3\x00\x00\xff\xb0\x00\x00\xff\xae\x00\x00\xff\xad\x00\x00\xff\xaa\x00\x00\xff\xc177\xff\xff\xfa\xfa\xff\xdaDJ\xff\xc3\x01\x08\xff\xbf\x01\x08\xff\xbb\x00\x07\xff\xb9\x00\x02\xff\xb3\x00\x02\xff\xad\x00\x01\xff\xac\x00\x01\xff\xac\x00\x00\xff\xaa\x00\x00\xff\xa5\x00\x00\xff\xa5\x00\x00\xff\xb4\x0e\x0e\xff\xbe55\xff\xff\xfa\xfa\xff"""

        return image_data


