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
    
# Define Restaurant class to handle survey-related operations
class Restaurant:
    def display_survey_questions(self):
        # Displays survey questions to the customer
        print("Welcome to our restaurant survey!")
        print("Please answer the following questions:")
        print("1. How satisfied were you with your meal?")
        print("2. How likely are you to recommend our restaurant to a friend?")    
    
    def collect_survey_responses(self, customer):
        # Collects survey responses from the customer
        self.display_survey_questions()
        
        # Collect responses for each question
        for question in range(1, 3):  
            answer = input(f"Answer for question {question}: ")
            customer.collect_survey_response(question, answer)
            
# Creates instances of Restaurant and Customer classes
restaurant = Restaurant()
customer = Customer("John Doe")

restaurant.collect_survey_responses(customer)

# Validates the customer's responses and provide the voucher if valid
if customer.validate_responses():
    customer.generate_voucher()
    print("Thank you for completing the survey! Here's your $20 voucher.")
else:
    print("Please complete the survey to receive the voucher.")