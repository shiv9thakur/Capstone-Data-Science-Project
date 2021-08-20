import re

text_to_search = '''

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (needed to be escaped):
. ^ $ * + - { } [ ] \ | ( )

shiv9thakur
coreyms.com

Mr. Pandey
Amit
Ajay
Pappu
Mrs. Briganza

Jai Hind

'''
sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r'and$')

matches = pattern.finditer(text_to_search)

for match in matches:
      print(match)

print(text_to_search[56:66])

print("Coded Completed")
