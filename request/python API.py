import requests
from html import unescape
from html import escape
import io

# Making a GET request
r = requests.get(
    'https://truyen.tangthuvien.vn/story/chapters?story_id=294&chapter_id=3626129')

data = r.text.split('title="')
Chapter = []
Link = []
for x in data:
    if x.find('chapter-text') != -1:
        chapter = unescape(x.split('">')[0])
        Chapter.append(chapter)
    if x.find('href=" ') != -1:
        link = x.split('href=" ')[1].split(' "')[0]
        Link.append(link)
for x in range(len(Chapter)):
    if x > 1898 and x < 1916:
        chapterx = requests.get(Link[x])
        text = chapterx.text.split(
            '</h5>')[1].split('">')[1].split('</div>')[0]
        text = text.replace('\t', ' ')
        text = text.replace('\n', ' ')
        text = text.replace(
            'Chương trình ủng hộ thương hiệu Việt của Tàng Thư Viện:', ' ')
        title = 'That Gioi Vu Than/'+Chapter[x].split(':')[0]+'.txt'
        print(title)
        with io.open(title, "w+", encoding="utf-8") as f:
            f.write(Chapter[x])
            f.write(unescape(text))
            f.close()

    # file = open(str(Chapter[x])+'.txt', 'w+')
    # print(Chapter[x])
    # # file.write(Chapter[x])
    # file.write(text)
    # file.close()
