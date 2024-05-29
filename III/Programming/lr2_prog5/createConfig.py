from configparser import ConfigParser

config = ConfigParser()

config.read('dev.ini')

print(config.sections())
print(config.get('settings', 'precision'))
print(config.options('settings'))