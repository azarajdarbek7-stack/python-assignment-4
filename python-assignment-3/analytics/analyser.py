class DataAnalyser:
    """Базовый класс (Parent)"""
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        """Этот метод будет переопределен в дочернем классе"""
        pass

    def print_results(self):
        print("\n--- Analysis Complete ---")

class CountryAnalyser(DataAnalyser):
    """Дочерний класс (Child) — использует твою логику из 3-го задания"""
    def analyse(self):
        countries = [s['country'] for s in self.students]
        country_counts = {}
        for c in countries:
            country_counts[c] = country_counts.get(c, 0) + 1

        sorted_c = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": dict(sorted_c[:3]),
            "all_countries": country_counts
        }
        return self.result

    def print_results(self):
        super().print_results()
        print(f"Total students: {self.result['total_students']}")
        print(f"Countries found: {self.result['total_countries']}")
        print(f"Top 3: {self.result['top_3']}")