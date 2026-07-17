def analyze_result(name,roll,marks):
    #calculate total and average
    total=sum(marks)
    average=total/len(marks)
    #assign the grades
    if average>=90:
        grade="A"
    elif average>=75:
        grade="B"
    elif average>=60:
        grade="C"
    elif average>=40:
        grade="D" 
    else:
        grade="Fail"
    #printing student details
    #here we use f string
    print(f"Student:{name}(Roll:{roll})")
    print(f"Total:{total}(Average:{average})")
    print(f"Grade:{grade}")
    #print student details
    print("subject below 40:")
    found=False
    for i,mark in enumerate(marks):
        if mark<40:
           print(f"Subject{i+1}")
           found=True 
    if not found:
        print("None")
#sample input
name="Aarav"
roll=101
marks=[88.5,35.0,76.0,92.5,48.0]
#function call
analyze_result(name,roll,marks)
             