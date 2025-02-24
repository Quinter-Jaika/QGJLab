# Required modules
import random #For generate
import string #For asses
from flask import Flask, request, render_template #For all

app = Flask(__name__)

#Functions
#Generate password
def password_generator(length):
    # Constants are concatenated
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate and return password
    password = ''.join(random.choices(all_characters, k=length))
    return f'Your new password is: {password}'

#Assess passwords
# Function to check password length
def count_checker(password):
    if len(password) < 12:
        return 'Please ensure that your password is at least 12 characters long.'
    else:
        return 'Password length meets the requirement.'

# Function to check presence of required character types
def character_checker(password):
    count_upper = count_lower = count_number = count_special = 0
    special_characters = string.punctuation  # All special characters

    for char in password:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char.isdigit():
            count_number += 1
        elif char in special_characters:
            count_special += 1

    # Check if all required character types are present
    if count_upper == 0 or count_lower == 0 or count_number == 0 or count_special == 0:
        return ('Please ensure that your password contains at least one uppercase letter, '
                'one lowercase letter, one number, and one special character.')
    else:
        return 'Password contains all required character types.'

# Function to give final feedback
def feedback(password):
    length_feedback = count_checker(password)
    character_feedback = character_checker(password)

    # Check if password is weak or strong
    feedback_messages = []
    if "at least" in length_feedback or "ensure" in character_feedback:
        feedback_messages.append("Weak Password:")
        if "at least" in length_feedback:
            feedback_messages.append(f"- {length_feedback}")
        if "ensure" in character_feedback:
            feedback_messages.append(f"- {character_feedback}")
    else:
        feedback_messages.append("Strong Password!")

    return "<br>".join(feedback_messages) 

# (URL: http://127.0.0.1:5000/)
@app.route("/")
def home():
    return render_template("home.html")  

@app.route("/generate", methods=["GET", "POST"])
def generate():
    result = None
    if request.method == "POST":
        try:
            user_input = int(request.form["length"])  # Convert input to integer
            result = password_generator(user_input)
        except ValueError:
            result = "Invalid input. Please enter a valid number."

    return render_template("generate.html", result=result)  


@app.route("/assess", methods=["GET", "POST"])
def assess():
    result = None
    if request.method == "POST":
        user_input = request.form["password"]  
        result = feedback(user_input)  
    
    return render_template("assess.html", result=result) 

if __name__ == "__main__":
    app.run(debug=True)