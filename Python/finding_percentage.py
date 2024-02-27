if __name__ == '__main__':
    n = int(input()) # Sets the Number of Students Inputs
    student_marks = {} # Creates the Dict of the Students

    for _ in range(n):
        name, *line = input().split() # Gets the Name of the student
        scores = list(map(float, line)) # Gets the Score of student
        student_marks[name] = scores # Adds the score to the dict and relationates with the name

    query_name = input() # Ask for a name to make the average
    defined_scores = student_marks[query_name] # Get the Scores for the student
    
    average = float(sum(defined_scores))/len(defined_scores) # Makes the Average
    print(f"{average:.2f}") # Prints the Average