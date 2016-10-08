# character_count.py

def main():
    # Main function logic
    message = raw_input("Please input a string")
    print(lenmsg(message))

def lenmsg(msg=""):
    length = len(msg)
    if length == 0:
        return("There are no characters in this string.")
    else:
        plural = ''
        if length > 1:
            plural += 's'
        return("'{}' has {} character{}.".format(msg, length, plural))

if __name__ == "__main__":
    main()
