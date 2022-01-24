# 入力部分

print('出力したいURLを入力してください')
rssurl = input()
print('出力したいファイル名を拡張子なしで入力してください')
filename = input()
print('出力形式を入力します。"html"または"txt"または"csv"で入力してください')
out_type = input()


# イベントループ
def output( str1 ,filetype):
    path1 = os.path.dirname(__file__) + "/" 
    file1 = path1 + filename + filetype
    write1( file1, str1 )
    print(path1 + ' に '+ filename + filetype + ' を出力')

def write1( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0

def time_split(date):
    timex = date.split("T")
    timex2 = timex[1].split("+")
    datex = timex[0].split("-")
    publish = datex[0] + "/" + datex[1] + "/" + datex[2] + " " + timex2[0]
    return publish         


if out_type != 'html' and out_type != 'txt' and out_type != 'csv' and out_type != 'cmd':
    print('選択したファイル形式が間違っています。最初からやり直してください。')

else :
    import os      
    import feedparser
    
    d = feedparser.parse(rssurl)
    outx = ""

    if 'title' not in d.feed:
        print('このURLはRSSフィードのものではありません。最初からやり直してください') 
        import sys
        sys.exit()

    print('処理しています...')
 
    if out_type == "html": ## HTML
        filetype = ".html"
        tt = d.feed.title
        for entry in d['entries']:
            outx += '<a href="'+ entry.link + '">' + entry.title + "</a><br>"
            outx += time_split(entry.published) + "<br><br>"
        
        str1 = '''
        <html>
            <head>
                <meta charset="utf-8">
                <title>{title1}</title>
            </head>
            <body>
                <h1>{title2}
                {body1} 
            </body>
        </html>'''.format( title1 = "output", title2 = tt,body1 = outx ) 
    
        output(str1 ,filetype) # 出力
    

    elif out_type == 'txt': # TXT
        filetype = ".txt"
        for entry in d['entries']:
            outx += entry.title + '\n' + 'link : '+ entry.link + '\n' 
            outx += time_split(entry.published) + '\n' + '\n'

        str1 = '''{body1}'''.format(body1 = outx ) 
        output(str1 ,filetype)
    

    elif out_type == 'csv': # CSV
        filetype= ".csv"
        outx += 'タイトル,日付,時間,リンク' + '\n'
        for entry in d['entries']:
            date = time_split(entry.published).split(" ")
            outx += entry.title + ',' + date[0] + ',' + date[1] + ',' + entry.link + '\n'

    elif out_type == 'cmd':
        outx = "\npage-title:" + d.feed.title + '\n'
        for entry in d['entries']:
            date = time_split(entry.published).split(" ")
            outx += "title     :" + entry.title + '\n' 
            outx += "published :" + date[0] + ',' + date[1] + "\n"
            outx += "link      :" + entry.link + '\n\n'
            

        str1 = '''{body1}'''.format(body1 = outx)
        print(str1)
        