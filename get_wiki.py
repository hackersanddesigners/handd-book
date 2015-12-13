# -*- coding: utf-8 -*-
import json
import urllib2
import os
import re

wikiUrl = 'http://wiki.hackersanddesigners.nl/mediawiki/'
f = open('handd-book.wiki', 'w')  

def get_pages(from_page):
  pages = []
  pageUrl = wikiUrl + 'api.php?action=parse&page=' + from_page + '&format=json&disableeditsection=true&prop=wikitext'
  wikiJson = json.load(urllib2.urlopen(pageUrl))
  try:
    wikistr = wikiJson['parse']['wikitext']['*'].encode('utf-8').strip()
    reobj = re.compile(r'\[\[[A-Za-z0-9\ \(\)\-\'\$\€,]*\]\]', re.IGNORECASE)
    res = reobj.findall(wikistr)
    for mat in res:
      page = mat.replace('[[','')
      page = page.replace(']]','')
      page = page.replace(' ','_')
      pages.append(page)
  except Exception, e:
    print e
  return pages

def get_image(filename):
  # http://wiki.hackersanddesigners.nl/mediawiki/api.php?action=query&titles=File:Chicken-and-Potato-Soup.png&prop=imageinfo&&iiprop=url&format=json
  if os.path.exists(filename):
    return
  wikiJson = json.load(urllib2.urlopen(wikiUrl + 'api.php?action=query&titles=File:' + filename + '&prop=imageinfo&&iiprop=url&format=json'))
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

pages = get_pages('Book_sprint_2015')

for page in pages:
  pageUrl = wikiUrl + 'api.php?action=parse&page=' + page + '&format=json&disableeditsection=true&prop=wikitext|images|links' 
  print pageUrl 
  wikiJson = json.load(urllib2.urlopen(pageUrl))
  wikistr = ''
  try:
    title = wikiJson['parse']['title'].encode('utf-8').strip()
    print title
    wikistr += '\n\n=' + title + '=\n\n'
  except Exception, e:
    print e

  try:
    # Get images - JBG
    imgs = wikiJson['parse']['images']
    for img in imgs:
      img = img.encode('utf-8').strip()
      print ' - ' + img
      get_image(img)
  except Exception, e:
    print e

  try:
    wikistr += wikiJson['parse']['wikitext']['*'].encode('utf-8').strip()
    wikistr = re.sub(r'\|\d*(x\d*)?px', '', wikistr) # Remove px info from images - JBG
    wikistr = re.sub(r'{{[A-Za-z0-9#:|/.?= \n&\-\\\”\{\}]*}}', '', wikistr) # Remove youtube links - JBG

    # Replace internal wiki links with external links for footnotes - JBG
    for link in wikiJson['parse']['links']:
      link_str = link['*'].encode('utf-8').strip()
      prep_str = link_str.replace(' ', '_')
      wikistr = re.sub(r'\[\[' + link_str + '[A-Za-z0-9\(\)| ]*\]\]', '[' + wikiUrl + 'index.php/' + prep_str + ' ' + link_str + ']', wikistr) 

    f.write(wikistr)
  except Exception, e:
    print e

