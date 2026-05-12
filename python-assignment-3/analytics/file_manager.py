import os
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        return os.path.exists(self.filename)

    def create_output_folder(self, folder='output'):
        if not os.path.exists(folder):
            os.makedirs(folder)

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(self.result, f, indent=4)
        print(f"Result saved to {self.output_path}")