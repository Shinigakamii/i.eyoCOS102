admitted = []
not_admitted = []

def check_admission(jamb_score, credits, passed_interview):
    if jamb_score >= 250 and credits >= 5 and passed_interview:
        admitted.append("Admitted")
        print("Congratulations! You are admitted into the Computer Science Department.")
    else:
        not_admitted.append("Not Admitted")
        print("Sorry, you did not meet the admission requirements for the Computer Science Department.")

# Example usage:
jamb_score = int(input("Enter your JAMB score: "))
credits = int(input("Enter the number of credits in key subjects: "))
passed_interview = input("Did you pass the interview? (yes/no): ").lower() == "yes"

check_admission(jamb_score, credits, passed_interview)