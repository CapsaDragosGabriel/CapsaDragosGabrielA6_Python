import utils as u

if __name__ == '__main__':
    read = ""
    while read != "q":
        x = input("Enter a number or quit:\n")
        if x == "q":
            break
        else:
            print(u.process_item(int(x)))
