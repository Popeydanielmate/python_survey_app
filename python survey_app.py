# Define customer class to represent the customer participating in the survey
class Customer:
    def __init__(self, name):
        self.name = name
        self.responses = {} # Dictionary to be used to store survey responses for each question
        
    def collect_survey_response(self, question, answer):
        self.responses[question] = answer
        
    def validate_responses(self):
        # Validate the survey responses (e.g., check if all questions were answered)
        # Return True if responses are valid, False otherwise
        if len(self.responses) == 2:  
            return True
        else:
            return False
        
    def generate_voucher(self):
        # Generates $20 voucher for the customer
        pass  
    
        