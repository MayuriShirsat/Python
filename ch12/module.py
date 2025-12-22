def myfun():
    print("hello")

myfun()
print(__name__) # output-> __main__

if __name__=="__main__":
    # If the code is executing from the file it actully belongs( not imported ) then run this code
    print("We are directly runing the code")
    # this code will run only in orignal file not in the imported one
    