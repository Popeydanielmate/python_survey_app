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
    
# Define the Restaurant class to handle survey-related operations
class Restaurant:
    def display_survey_questions(self):
        # Displays survey questions to the customer
        print("Welcome to our restaurant survey!")
        print("Please answer the following questions:")
        print("1. How satisfied were you with your meal?")
        print("2. How likely are you to recommend our restaurant to a friend?")    
    
        