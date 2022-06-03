from bs4 import BeautifulSoup as bs
from requests import get # sending get requests

def getChanges():
    result = []

    response = get ("https://blog.ir/changes")  # send a get request to https://blog.ir/changes
    parser = bs(response.content , "html.parser") 

    posts = parser.find_all("div" , "post")  # get all <div class="post" .... > tags
    
    for post in posts:
        a_tag = post.find_all("a") [0] # find all <a href = ... > tags 
        title = a_tag.text # title of post
        link = a_tag["href"] # link of post
        result.append({"TITLE" : title , "LINK" : link})

    return result

