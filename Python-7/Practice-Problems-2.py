# Q1) Createan new file "practice.txt" using python. add the following data in it:
# Hi everyone
# we are learning File I/O
# Using Python
# I like programming in python

"""
f = open("Python-7/practice.txt", "w")
f.write("Hi everyone\nwe are learning File I/O\nUsing Python\nI like programming in python")
f.close()
"""
#or
"""
with open("Python-7/practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nUsing Python\nI like programming in python")
"""
"""
# Q2) WAF that replaces all occurrences of "python" with "Java" in the above file.

with open("Python-7/practice.txt", "r+") as f:
    data = f.read()
    new_data = data.replace("python", "Java")
    print(new_data)

with open("Python-7/practice.txt", "w") as f:
    f.write(new_data)
"""
"""
# Q3) Search if the word "learning" exists in the file or not.
word = "learning"
with open("Python-7/practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")
"""

"""
#Q4) WAF to find which line of the file does the word "learning" occurs first. (print -1 if word not found)

def find_line():
    word = "bye"
    data = True
    line_no = 1
    with open("Python-7/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(find_line())
"""

# Q5) From a file containing numbers seperated by commas, print the count of even numbers.
"""
with open("Python-7/practice.txt", "r") as f:
    data = f.read()
    print(data)
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            if(int(num)%2==0):
                print(int(num))
            num = ""
        else:
            num += data[i]
#NOTE can also solve using list

count = 0
with open("Python-7/practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1
print(count)
"""