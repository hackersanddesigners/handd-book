import json
import urllib2
import pypandoc
import os
from bs4 import BeautifulSoup

pages = [
  'Royal_Tombs._Review._Hackers_%26_Designers_Summer_Academy',
  'Toy_Hacking',
  'Algorthimic_recipe_1',
  'The_right_to_die_digitally,_digital_euthanasia,_image_rights_and_more'
  #'Algorithmic_Kitchen'
  #'Code,_text_and_text-to-speech',
  #'Language_Design',
  #'Applied_Bio-Robotics',
  #'Error_Messages',
  #'DIY_theremin_making',
  #'Domestic_Drone_Defence',
  #'Waag_Society',
  #'Lava_Lab'
]

def get_image(filename):
  print filename
  # http://wiki.hackersanddesigners.nl/mediawiki/api.php?action=query&titles=File:Chicken-and-Potato-Soup.png&prop=imageinfo&&iiprop=url&format=json
  if os.path.exists(filename):
    return
  wikiJson = json.load(urllib2.urlopen('http://wiki.hackersanddesigners.nl/mediawiki/api.php?action=query&titles=File:' + filename + '&prop=imageinfo&&iiprop=url&format=json'))
  print wikiJson
  try:
    pages = wikiJson['query']['pages']
    print pages
    for key, value in pages.iteritems(): 
      url = value['imageinfo'][0]['url']
      print url
      img_res = urllib2.urlopen(url)
      img_file = open(filename, 'wb')
      img_file.write(img_res.read())
      img_file.close()
  except Exception, e:
    print e

#def process_images(html_str):
#  soup = BeautifulSoup(html_str, 'html.parser')
#  imgs = soup.findAll('img')
#  for img in imgs:
#    src = img['src'].encode('utf-8').strip()
#    path_elms = src.split('/')
#    filename = path_elms[len(path_elms) - 1]
#    if not os.path.exists(filename):
#      img_res = urllib2.urlopen('http://wiki.hackersanddesigners.nl' + src)
#      img_file = open(filename, 'wb')
#      img_file.write(img_res.read())
#      img_file.close()
#
#    img['src'] = filename
   
#  html_str = str(soup) 
#  return html_str
 
def write_begin():
  begin_file = open('begin.tex', 'r')
  book_file = open('handd_book.tex', 'w')
  book_file.write(begin_file.read())
  book_file.close()
  begin_file.close()

def write_end():
  end_file = open('end.tex', 'r')
  book_file = open('handd_book.tex', 'a')
  book_file.write(end_file.read())
  book_file.close()
  end_file.close()

def write_chapters():
  book_file = open('handd_book.tex', 'a')
  for page in pages:
    wikiJson = json.load(urllib2.urlopen('http://wiki.hackersanddesigners.nl/mediawiki/api.php?action=parse&page=' + page + '&format=json&disableeditsection=true&prop=wikitext|images'))
    try:
      # Get images - JBG
      imgs = wikiJson['parse']['images']
      for img in imgs:
        img = img.encode('utf-8').strip()
        get_image(img)

      # Title stuff - JBG
      title = wikiJson['parse']['title'].encode('utf-8').strip()
      title = title.replace('&', '\&')
      book_file.write('\\chapter{' + title + '}')

      html_str = wikiJson['parse']['wikitext']['*'].encode('utf-8').strip()
      #html_str = process_images(html_str)
      #tex_str = pypandoc.convert(html_str, 'tex', format='html').encode('utf-8').strip()
      tex_str = pypandoc.convert(html_str, 'tex', format='mediawiki').encode('utf-8').strip()
      book_file.write(tex_str)
    except Exception, e:
      print e
  book_file.close()

write_begin()
write_chapters()
write_end()

