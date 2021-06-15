import glob
import re
from Message import Message
import csv
import os


class SpamMessagesParser:

    def __init__(self, directoryPath):
        self.directoryPath = directoryPath

    def parse_to_csv(self, path):
        self.create_csv_file(path)
        directory = self.directoryPath
        parsed_messages = self.parse_directory(directory)

        for parsed_message in parsed_messages:
            message_subject = self.parse_file(parsed_message.file_path)
            print(message_subject, parsed_message.is_spam)
            self.write_to_csv(path, message_subject, parsed_message.is_spam)

    def parse_directory(self, directoryPath):
        parsed_messages = []

        for file_path in glob.glob(directoryPath, recursive=True):
            is_spam = 'ham' not in file_path
            parsed_messages.append(Message(file_path, is_spam))

        return parsed_messages

    def parse_file(self, path):
        subject = ''

        with open(path, 'r', errors='ignore') as file_content:
            for line in file_content:
                if line.startswith('Subject:'):
                    subject = re.sub(r'Subject: ', '', line).strip()

        return subject

    def create_csv_file(self, path):
        header = ['subject', 'is_spam']

        if os.path.exists('path'):
            with open(path, 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(header)

    def write_to_csv(self, path, message_subject, is_spam):
        data = [message_subject, is_spam]

        with open(path, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
