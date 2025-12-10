import random
import os

def load_question_bank(file_path):
    """
    Reads the file where questions and answers are on alternating lines.
    Returns a list of dictionaries: [{'q': question, 'a': answer}, ...]
    """
    if not os.path.exists(file_path):
        return None  # File does not exist

    try:
        # Use utf-8 encoding to prevent common decoding errors
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except Exception:
        # If utf-8 fails, try again with error ignoring
        with open(file_path, 'r', errors='ignore') as file:
            lines = file.readlines()
    
    questions_data = []
    # Process lines in pairs (Question, Answer)
    for i in range(0, len(lines) - 1, 2):
        q = lines[i].strip()
        a = lines[i+1].strip()
        questions_data.append({'q': q, 'a': a})
        
    return questions_data

def main():
    # Display welcome message
    print("Welcome to professor assistant version 1.0.")
    
    # Get professor's name
    prof_name = input("Please Enter Your Name: ")
    
    # Greet the professor
    print(f"Hello Professor {prof_name}, I am here to help you create exams from a question bank.")

    while True:
        # Ask whether to create an exam
        user_choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()
        
        # Quit option (accepts 'no' or 'n')
        if user_choice in ['no', 'n']:
            print(f"Thank you professor {prof_name}. Have a good day!")
            break
        
        # Proceed option (accepts 'yes' or 'y')
        elif user_choice in ['yes', 'y']:
            
            # Get path to question bank file
            path = input("Please Enter the Path to the Question Bank: ")
            
            # Load the questions and handle errors
            questions_bank = load_question_bank(path)
            
            if questions_bank is None or len(questions_bank) == 0:
                print("Error: The file path provided does not exist or is empty. Please try again.")
                continue

            print("Yes, indeed the path you provided includes questions and answers.")

            # Get number of questions with input validation
            while True:
                try:
                    num_questions = int(input("How many question-answer pairs do you want to include in your exam? "))
                    if num_questions > len(questions_bank):
                        print(f"Note: The bank only has {len(questions_bank)} questions. We will use all of them.")
                        num_questions = len(questions_bank)
                    break
                except ValueError:
                    print("Please enter a valid number.")

            # Get output filename
            output_filename = input("Where do you want to save your exam? ")

            # Randomly select unique questions using randint
            selected_indices = []
            max_index = len(questions_bank) - 1
            while len(selected_indices) < num_questions:
                # Select a random index
                random_index = random.randint(0, max_index)
                
                # Only add if the question hasn't been selected yet
                if random_index not in selected_indices:
                    selected_indices.append(random_index)
            
            # Write the selected questions to the output file
            try:
                with open(output_filename, 'w', encoding='utf-8') as out_file:
                    for idx in selected_indices:
                        pair = questions_bank[idx]
                        out_file.write(f"Question: {pair['q']}\n")
                        out_file.write(f"Answer: {pair['a']}\n\n")
                
                # Confirm success
                print(f"Congratulations Professor {prof_name}. Your exam is created and saved in {output_filename}.")
            
            except IOError:
                print("Error: Could not write to the specified output file.")
        
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")

# Execute the program
if __name__ == "__main__":
    main()