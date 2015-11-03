import json
import urllib2
f = open('test.wiki', 'w')  
pages = [
  'Algorthimic_recipe_1',
  'The_right_to_die_digitally,_digital_euthanasia,_image_rights_and_more',
  'Toy_Hacking',
  'Algorithmic_Kitchen'
  #'Code,_text_and_text-to-speech',
  #'Language_Design',
  #'Applied_Bio-Robotics',
  #'Error_Messages',
  #'DIY_theremin_making',
  #'Domestic_Drone_Defence',
  #'Waag_Society',
  #'Lava_Lab'
]



for page in pages:
  wikiJson = json.load(urllib2.urlopen('http://wiki.hackersanddesigners.nl/mediawiki/api.php?action=parse&page=' + page + '&format=json&disableeditsection=true&prop=wikitext'))

  #title = wikiJson['parse']['title'].encode('utf-8').strip()
  #title = title.replace('&', '\&')

  str = wikiJson['parse']['wikitext']['*'].encode('utf-8').strip()
  f.write(str)

