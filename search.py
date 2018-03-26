# -*- coding: utf-8 -*-
import requests
import bs4
import sys

def main():
    index = 1

    try:
        fread = open('in.txt', 'r')
    except BaseException, e:
        # print e.message
        print '"in.txt"文件打开失败'
        return

    for word in fread.readlines():

        word = word.replace("\r", "")
        word = word.replace("\n", "")
        word = word.replace("\t", "")
        word = word.replace(" ", "")

        if word == '':
            continue

        print '※单词序号:', index
        print '※原始单词:', word

        try:
            url = "http://dict.youdao.com/search?q=" + word
            response = requests.get(url)
            soup = bs4.BeautifulSoup(response.content.decode("utf-8"), "html.parser")
            h2_node = soup.find('h2', class_='wordbook-js')
            name_node = h2_node.find('span', class_='keyword')
            nameStr = name_node.get_text()
            nameStr = nameStr.replace("\r", "")
            nameStr = nameStr.replace("\n", "")
            nameStr = nameStr.replace("\t", "")
            nameStr = nameStr.replace(" ", "")
            if nameStr.lower() != word.lower():
                print '(此单词查询出错)'
                print ''
                index += 1
                continue
        except BaseException, e:
            # print e.message
            print '(此单词查询出错)'
            print ''
            index += 1
            continue

        try:
            baav_node = h2_node.find('div', class_='baav')
            pronounce_nodes = baav_node.findAll('span', class_='pronounce')
            for pronounce_node in pronounce_nodes:
                try:
                    phonetic_node = pronounce_node.find('span', class_='phonetic')
                    nameStr = pronounce_node.get_text().replace(phonetic_node.get_text(), "")
                    nameStr = nameStr.replace("\r", "")
                    nameStr = nameStr.replace("\n", "")
                    nameStr = nameStr.replace("\t", "")
                    nameStr = nameStr.replace(" ", "")
                    if nameStr == '英'.decode('utf8'):
                        print '※英式音标:', phonetic_node.get_text()
                    elif nameStr == '美'.decode('utf8'):
                        print '※美式音标:', phonetic_node.get_text()
                    elif nameStr == ''.decode('utf8'):
                        print '※音标:', phonetic_node.get_text()
                except BaseException, e:
                    # print e.message
                    pass
        except BaseException, e:
            # print e.message
            pass

        try:
            li_node = soup.find('div', class_='trans-container').find('ul').find('li')
            if li_node != None:
                print '※单词释义:', li_node.get_text()
        except BaseException, e:
            # print e.message
            pass

        try:
            webPhrase_node = soup.find('div', id='webPhrase', class_='pr-container')
            wordGroup_nodes = webPhrase_node.findAll('p', class_='wordGroup')
            print '※短语(网络释义):'
            for wordGroup_node in wordGroup_nodes:
                try:
                    contentTitle_node = wordGroup_node.find('span', class_='contentTitle')
                    search_js_node = contentTitle_node.find('a', class_='search-js')
                    nameStr = wordGroup_node.get_text().replace(search_js_node.get_text(), "")
                    nameStr = nameStr.replace("\r", "")
                    nameStr = nameStr.replace("\n", "")
                    nameStr = nameStr.replace("\t", "")
                    nameStr = nameStr.replace(" ", "")
                    nameStr = search_js_node.get_text() + ": " + nameStr
                    print nameStr
                except BaseException, e:
                    # print e.message
                    pass
        except BaseException, e:
            # print e.message
            pass

        try:
            transformToggle_node = soup.find('div', id='transformToggle').find('div', id='wordGroup', class_='trans-container tab-content hide more-collapse')
            wordGroup_nodes = transformToggle_node.findAll('p', class_='wordGroup')
            print '※词组短语:'
            for wordGroup_node in wordGroup_nodes:
                try:
                    contentTitle_node = wordGroup_node.find('span', class_='contentTitle')
                    search_js_node = contentTitle_node.find('a', class_='search-js')
                    nameStr = wordGroup_node.get_text().replace(search_js_node.get_text(), "")
                    nameStr = nameStr.replace("\r", "")
                    nameStr = nameStr.replace("\n", "")
                    nameStr = nameStr.replace("\t", "")
                    nameStr = nameStr.replace(" ", "")
                    nameStr = search_js_node.get_text() + ": " + nameStr
                    print nameStr
                except BaseException, e:
                    # print e.message
                    pass
        except BaseException, e:
            # print e.message
            pass

        try:
            synonyms_node = soup.find('div', id='synonyms', class_='trans-container tab-content hide')
            ul_node = synonyms_node.find('ul')
            li_nodes = ul_node.findAll('li')
            wordGroup_nodes = ul_node.findAll('p', class_='wordGroup')
            li_node_index = 0
            print '※同近义词:'
            for li_node in li_nodes:
                try:
                    print '词义:', li_node.get_text()
                    contentTitle_node = wordGroup_nodes[li_node_index].find('span', class_='contentTitle')
                    search_js_node = contentTitle_node.find('a', class_='search-js')
                    nameStr = wordGroup_nodes[li_node_index].get_text().replace(search_js_node.get_text(), "")
                    nameStr = nameStr.replace("\r", "")
                    nameStr = nameStr.replace("\n", "")
                    nameStr = nameStr.replace("\t", "")
                    nameStr = nameStr.replace(" ", "")
                    nameStr = search_js_node.get_text() + nameStr
                    print '单词:', nameStr
                except BaseException, e:
                    # print e.message
                    pass
                li_node_index += 1
        except BaseException,e:
            # print e.message
            pass

        try:
            relWordTab_node = soup.find('div', id='relWordTab', class_='trans-container tab-content hide')
            wordGroup_nodes = relWordTab_node.findAll('p', class_='wordGroup')
            print '※同根词:'
            for wordGroup_node in wordGroup_nodes:
                try:
                    contentTitle_node = wordGroup_node.find('span', class_='contentTitle')
                    search_js_node = contentTitle_node.find('a', class_='search-js')
                    nameStr = wordGroup_node.get_text().replace(search_js_node.get_text(), "")
                    nameStr = nameStr.replace("\r", "")
                    nameStr = nameStr.replace("\n", "")
                    nameStr = nameStr.replace("\t", "")
                    nameStr = nameStr.replace(" ", "")
                    if nameStr == '词根：'.decode('utf8'):
                        print '词根:', search_js_node.get_text()
                    else:
                        nameStr = search_js_node.get_text() + ": " + nameStr
                        print nameStr
                    if wordGroup_node.next_sibling != None:
                        tempStr = wordGroup_node.next_sibling
                        tempStr = tempStr.replace("\r", "")
                        tempStr = tempStr.replace("\n", "")
                        tempStr = tempStr.replace("\t", "")
                        tempStr = tempStr.replace(" ", "")
                        if tempStr != '':
                            print tempStr
                except BaseException, e:
                    # print e.message
                    pass
        except BaseException,e:
            # print e.message
            pass

        print ''
        index += 1

    fread.close()

if __name__  ==  '__main__':
    try:
        reload(sys)
        sys.setdefaultencoding('utf-8')
        print 'To DCY'
        main()
        print 'Made By JXL'
    except BaseException,e:
        # print e.message
        pass
