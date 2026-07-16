class Report:

    def generate_report(self):
        return "Generating Report"

    def save_to_file(self):
        return "Saving Report to File"

    def print_report(self):
        return "Printing Report"


report = Report()
print(report.generate_report())
print(report.save_to_file())
print(report.print_report())