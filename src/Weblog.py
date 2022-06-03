from bs4 import BeautifulSoup as bs
from requests import get


class Weblog:
    def __init__(self , address):
        self.address = address
        self.address = self.address.replace("http://" , "https://")

        if not self.address.startswith("https://"):
            self.address = "https://" + self.address
        
        
        if self.address[-1] == "/":
            self.address = self.address[0:-1]

        self.name = self.address.replace("https://" , "")
        

        self.rss_address = self.address + "/rss"
        

        self.follow_link = "http://blog.ir/panel/-/followed_blogs?follow={}".format(self.address)
        
        response = get(self.address)
        if response.status_code == 200:
            self.html_parser = bs(response.content , "html.parser")
        else:
            pass

        response = get(self.rss_address)
        if response.status_code == 200:
            self.rss_parser = bs(response.content , "xml") # lxml should be installed using pip
        else:
            pass

    def extractDigits(self, data):
        number = ""
        for char in data:
            if char.isdigit():
                number += char
        try:
            return int(number)
        except:
            return None

    def getInfo(self):
        result = {}
        title = self.rss_parser.title.text

        result["TITLE"] = title

        script_tag = self.html_parser.find_all("script")[1]
        if "stats" in script_tag.text :
            text = script_tag.text
            text = text.replace("\n" , "")
            text = text.replace("\t" , "")
            text = text.split("'")

            for i in range(len(text)):
                if text[i] == "VIEW_STAT_POSTS_COUNT":
                    posts_count = self.extractDigits(text[i+4])
                    result["POSTS_COUNT"] = posts_count
                if text[i] == "VIEW_STAT_BLOG_LIFE_TIME":
                    blog_life_time = self.extractDigits(text[i+4])
                    result["BLOG_LIFE_TIME"] = blog_life_time
                if text[i] == "VIEW_STAT_FOLLWER_COUNT":
                    followers_count = self.extractDigits(text[i+4])
                    result["FOLLOWERS_COUNT"] = followers_count
                if text[i] == "VIEW_STAT_COMMENTS_COUNT":
                    comments_count = self.extractDigits(text[i+4])
                    result["COMMENTS_COUNT"] = comments_count
                
        if not("FOLLOWERS_COUNT" in result):
            followersTitle = self.html_parser.find("div" , "followersTitle")
            if followersTitle:
                followers_count = self.extractDigits(followersTitle.text)
                if followers_count:
                    result["FOLLOWERS_COUNT"] = followers_count
        
        return result

    def getPages(self):
        result = []
        a_tags = self.html_parser.find_all("a")
        for a in a_tags:
            if a.has_attr("href"):
                if "/page/" in a["href"] and not (a.has_attr("alt")):
                    title = a.text
                    link = a["href"]
                    result.append({"TITLE" : title , "LINK" : self.address + link})
        return result

    def getLastPosts(self):
        result = []
        items = self.rss_parser.find_all("item")
        for item in items:
            title = item.title.text
            link = item.link.text
            if title and link:
                result.append({"TITLE" : title , "LINK" : link})
        return result

    def getLastFollowers(self):
        result = []
        followersLs = self.html_parser.find(id = "followersLs")
        if followersLs:
            for follower in followersLs.find_all("a" , "follower"):
                result.append(follower["href"])
            
            return result
        else:
            return None
   
    def getLinks(self):
        result = []
        a_tags = self.html_parser.find_all("a")
        for a in a_tags:
            if a.has_attr("href") and a.has_attr("alt"):
                if "/process/link_clicked" in a["alt"]:
                    title = a.text
                    link = a["href"]
                    result.append({"TITLE" : title , "LINK" : link})
        return result
