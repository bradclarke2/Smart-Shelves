from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('example.ini')

key = parser.get('credentials', 'APIkey')
print(key)