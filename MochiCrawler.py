
import httplib
import re
import argparse

class MochiCrawler():

    def __init__(self,url,depth):
        self.url=url
        self.depth=depth

    def crawlWEB(self):
        processed = []
        # only works for http links
        if self.url.startswith("http://")  and (not self.url in processed):
            processed.append(self.url)
            self.url = self.url.replace("http://", "", 1)

            print "------------------>"+processed[0]

            # split out the url into host and web components
            host, path = self.url, "/"
            print "...................host>>>>>>>"+host
            print "...................path_______"+path

            urlparts = self.url.split("/")
            if len(urlparts) > 1:
                host = urlparts[0]
                path = self.url.replace(host, "", 1)

            # make the first request
            print "crawling host--->: " + host + " path--->: " + path
            conn = httplib.HTTPConnection(host)
            req = conn.request("GET", path)
            res = conn.getresponse()

            # find the links
            contents = res.read()
            n = re.findall('href="(.*?)"', contents)

            for href in n:
                if href.startswith("/"):
                    href = "http://" + host + href

                # follow links to the next dept
                if self.depth:
                    m=MochiCrawler(href, self.depth - 1)
                    m.crawlWEB()
        else:
            #Skip already processed links
            print "skip link " + self.url

if __name__ == '__main__':
    m=MochiCrawler('http://www.strathmore.edu', 2)
    m.crawlWEB()
