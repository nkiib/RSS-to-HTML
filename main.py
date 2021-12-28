import os
import feedparser
import datetime
 
rssurl='https://nishikiout.hatenablog.com/feed'
d = feedparser.parse(rssurl)
outx = ""

for entry in d['entries']:
    outx += '<a href="'+ entry.link + '">' + entry.title + "</a><br>"
    outx += entry.published + "<br><br>"

def write1( file1, str1 ): 
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0 

dt = datetime.datetime.today()
day = dt.date()



str1 = '''
<html>
<head>
<meta charset="utf-8">
<title>{title1}</title>
</head>
<body>
{body1} 
</body>
</html>
'''.format( title1 = "hello hstml", body1 = outx ) 

print( str1 ) 

path1 = os.path.dirname(__file__) + "/" 
file1 = path1 + "output.html"
write1( file1, str1 ) 