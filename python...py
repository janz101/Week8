def count_space(text):

    spaces=0
    for char in text:
        if char ==" " :
           spaces=space+1
    return spaces
def main():

    text=input("please enter text")
    number_of_spaces = count_spaces(text)
    print("num of spaces=",number_of_spaces)
main()
