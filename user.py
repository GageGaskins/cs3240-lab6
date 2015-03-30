__author__ = 'Rohan'

class User:
    def __init__(self, name):
        self.name = name
        self.reports = []
        self.starred = []
        self.groups = []

    def starreport(self, report):
        self.starred.append(report)

    def addreport(self, name):
        newreport = Report(name)
        self.reports.append(newreport)