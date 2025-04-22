string = "java developer" # global var
def outer():
    string = "python"
    def inner():
        nonlocal string # enclosed scope var
        string+=" developer" #local scope var
        return f"I am a {string}"
    
    return inner()

print(outer())
