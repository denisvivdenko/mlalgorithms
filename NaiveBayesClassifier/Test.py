from MessagesParser import SpamMessagesParser
import json
import os


working_directory = os.getcwd()
settings_path = os.path.join(working_directory, 'paths.json')

with open(settings_path) as settings:
    settings = json.load(settings)
    SpamMessagesParser(settings['DATASETS_PATH']).parse_to_csv(settings['CSV_FILE_PATH'])
