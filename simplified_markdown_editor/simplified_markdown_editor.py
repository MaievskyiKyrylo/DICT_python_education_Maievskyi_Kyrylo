text = ""

while True:
    formatter = input("Choose a formatter: ")
    if formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list "
              "unordered-list new-line\nSpecial commands: !help !done")
    elif formatter == "!done":
        with open("output.md", "w") as file:
            file.write(text)
        break
    elif formatter not in ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                           "unordered-list", "new-line"]:
        print("Unknown formatting type or command")
    else:
        if formatter == "plain":
            text += input("Text: ")
        elif formatter == "bold":
            text += "**" + input("Text: ") + "**"
        elif formatter == "italic":
            text += "*" + input("Text: ") + "*"
        elif formatter == "inline-code":
            text += "`" + input("Text: ") + "`"
        elif formatter == "link":
            label = input("Label: ")
            url = input("URL: ")
            text += "[" + label + "](" + url + ")"
        elif formatter == "header":
            level = int(input("Level: "))
            if level < 1 or level > 6:
                print("The level should be within the range of 1 to 6")
                continue
            text += "#" * level + " " + input("Text: ") + "\n"
        elif formatter == "unordered-list":
            while True:
                rows = int(input("Number of rows: "))
                if rows > 0:
                    break
                print("The number of rows should be greater than zero")
            for i in range(rows):
                text += "* " + input(f"Row #{i+1}: ") + "\n"
        elif formatter == "ordered-list":
            while True:
                rows = int(input("Number of rows: "))
                if rows > 0:
                    break
                print("The number of rows should be greater than zero")
            for i in range(rows):
                text += f"{i+1}. " + input(f"Row #{i+1}: ") + "\n"
        elif formatter == "new-line":
            text += "\n"

        print(text)
