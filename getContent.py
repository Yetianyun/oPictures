

#使用另一种方法，获得某网站的内容
def getContent(url):
    print(url)

if __name__ == '__main__':
    source_file = "text/source.txt"
    file = open(source_file)
    for url in file:
        getContent(url)

