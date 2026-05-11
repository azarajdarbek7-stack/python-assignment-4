class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        print("-" * 30)
        for key, value in self.result.items():
            print(f"{key}: {value}")
        print("-" * 30)

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        if not self.students:
            return
        counts = {}
        for s in self.students:
            country = s.get('country', 'Unknown')
            counts[country] = counts.get(country, 0) + 1
        
        sorted_countries = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        self.result = {
            "total_students": len(self.students),
            "total_countries": len(counts),
            "top_3": dict(sorted_countries[:3])
        }

    def __str__(self):
        return f"CountryAnalyser: {len(self.students)} students"