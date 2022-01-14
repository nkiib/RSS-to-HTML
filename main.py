# 入力部分

print('出力したいURLを入力してください')
rssurl = input()
print('出力したいファイル名を拡張子なしで入力してください')
filename = input()
print('出力形式を入力します。"html"または"txt"で入力してください')
out_type = input()


# イベントループ
def output(write1, str1 ,filetype):
    path1 = os.path.dirname(__file__) + "/" 
    file1 = path1 + filename + filetype
    write1( file1, str1 )
    print(path1 + ' に '+ filename + filetype + ' を出力')

def write1( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0     


if out_type != 'html' and out_type != 'txt':
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
        for entry in d['entries']:
            outx += '<a href="'+ entry.link + '">' + entry.title + "</a><br>"
            outx += entry.published + "<br><br>"

        str1 = '''
        <html>
            <head>
                <meta charset="utf-8">
                <title>{title1}</title>
            </head>
            <body>
                {body1} 
            </body>
        </html>'''.format( title1 = "output", body1 = outx ) 
    
        output(write1, str1 ,filetype) # 出力
    

    elif out_type == 'txt': # TXT
        filetype = ".txt"
        for entry in d['entries']:
            outx += entry.title + '\n' + 'link : '+ entry.link + '\n' 
            outx += entry.published + '\n' + '\n'

        str1 = '''{body1}'''.format( title1 = "output", body1 = outx ) 
        output(write1, str1 ,filetype)
    

    elif out_type == 'csv': # CSV
        print('CSVに到達')
            # 未実装
    
    
    elif out_type == 'xml': # XML
        print('XMLに到達')
        # 未実装


    