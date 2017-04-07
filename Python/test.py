from configparser import SafeConfigParser
import os

parser = SafeConfigParser()
parser.read('keys.ini')

print(os.path.abspath('keys.ini'))

key = parser.get('credentials', 'APIkey')
print(key)