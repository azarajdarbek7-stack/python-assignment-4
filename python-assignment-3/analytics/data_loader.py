import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        try:
            with open(self.filename, mode='r', encoding='utf-8-sig') as f:
                lines = [line for line in f if line.strip()]
                if not lines: return []
                
                delimiter = ';' if ';' in lines[0] else ','
                reader = csv.DictReader(lines, delimiter=delimiter)
                self.students = [row for row in reader]
            return self.students
        except Exception as e:
            print(f"Error loading: {e}")
            return []