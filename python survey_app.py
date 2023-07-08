# Define customer class to represent the customer participating in the survey
class Customer:
    def __init__(self, name):
        self.name = name
        self.responses = {} # Dictionary to be used to store survey responses for each question
        
    