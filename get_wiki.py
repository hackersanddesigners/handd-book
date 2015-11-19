# -*- coding: utf-8 -*-
import json
import urllib2
import os

f = open('handd-book.wiki', 'w')  
pages = [
  'How_to_organize_a_summer_academy',
  'How_to_document_a_summer_academy',
  'How_to_engage_in_collaborative_processes',
  'How_to_research_stuff_by_making',
  'Royal_Tombs._Review._Hackers_%26_Designers_Summer_Academy',
  '(Un)willingly_Memorialized_—_Images_and_the_dead_in_the_Digital_Age',
  'Summer_Talks:_Training_and_the_problem_of_data',
  'Summer_Talks:_Gestural_Interfacing',
  'Summer_Talks:_Discrete_Cosine_Transform',
  'Review_Jona_Andersen',
  'Algorthimic_recipe_1',
  'Algorthimic_recipe_2',
  'Algorthimic_recipe_3',
  'Fembot',
  'Spybot',
  'Haikubot',
  'Swapbot',
  'Facebot',
  'Beuysbot',
  'Net_launcher',
  'Bottle_rocket',
  'Umbrella_artillery',
  'Genuino_UNO',
  'Theremin_Sensor',
  'Conversations',
  'Hackers_%26_Designers_bag',
  'Glossary',
  'Pizza_ordering_language',
  'Cocktail_Generator',
  '\'Sad_Face\'_Error',
  '\'Awkward\'_Error',
  'Movie_bio-robotics',
  'Computer_language_history',
  'Computer_language_design_schema',
  'DIY_steps_Theremin',
  'DIY_steps_Talking_plant',
  'DIY_steps_bio-robotics',
  'Group_pictures',
  #'Images_test_page',
  #'Jeremy_Bailey_ad1',
  #'Jeremy_Bailey_ad2',
  #'Jeremy_Bailey_ad3',
  #'Jeremy_Bailey_ad4',
  #'Jeremy_Bailey_ad5',
  'Feedback_deelnemers',
  'Toy_Hacking',
  'Algorithmic_Kitchen',
  'Code,_text_and_text-to-speech',
  'Language_Design',
  'Applied_Bio-Robotics',
  'Error_Messages',
  'DIY_theremin_making',
  'Domestic_Drone_Defence',
  'Waag_Society',
  'Lava_Lab',
  'Underground_Cinema',
  'Summer_Talks_and_Summer_Party',
  'Short_bios',
  'Credits'
]

def get_image(filename):
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

for page in pages:
  wikiJson = json.load(urllib2.urlopen('http://wiki.hackersanddesigners.nl/mediawiki/api.php?action=parse&page=' + page + '&format=json&disableeditsection=true&prop=wikitext|images'))
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

  #title = wikiJson['parse']['title'].encode('utf-8').strip()
  #title = title.replace('&', '\&')

  try:
    wikistr += wikiJson['parse']['wikitext']['*'].encode('utf-8').strip()
    f.write(wikistr)
  except Exception, e:
    print e

