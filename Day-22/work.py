#POSITIONAL
def fullname(first,last):
    return first+last

print(fullname("Kalyan ","Maharajulu"))

#POSITIONAL AND DEFAULT
def full_name(first,last,middle=0):
    return first+middle+last

print(full_name("Kalyan "," Maharajulu","Roy"))

#POSITIONAL, DEFAULT AND ARBITUARY
def student_details(name, age, batch="37R", *course):
    return (name, age, batch, course)

print(student_details("kalyan", 23,"37r", "Python", "MERN", "React", "Node.js"))

#POSITIONAL, DEFAULT, ARBITUARY AND KWARGS

def student_details(name, age, batch="37R", *course, **addr):
    return (name, age, batch, course, addr)

print(student_details("kalyan", 23,"37r", "Python", "MERN", "React", "Node.js",street = "3",landmark="gandhi nagar", city="Hyderabad",state="Telangana"))