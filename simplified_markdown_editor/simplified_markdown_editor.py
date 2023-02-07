formats = ["plain", "bolt", "inline-code", "link", "header",
           "unordered-list", "ordered-list", "newline", "!help", "!done"]

class Markdown:
    def plain(self):
        self.level = [1, 2, 3, 4]

    def link(self):
        self.url = input("URL: >")

    def header(self):
        self.level = [1, 2, 3, 4]

    def information(self):
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line"
              "\nSpecial commands: !help !done")

marks = Markdown()

while True:
    choice = input("Choose a formatter: >")
    try:
        choice != formats
    except:
        print("Unknown formatting type or command")

    if choice == "!help":
        marks.information()
    elif choice == "!done":
        exit()
    elif choice == "plain":
        choice += marks.header()
    elif choice == "link":
        choice += marks.header()
    elif choice == "unordered-list":
        choice += marks.header()
    elif choice == "ordered-list":
        choice += marks.header()
    elif choice == "header":
        choice += marks.header()
    elif choice == "new-line":
        choice += marks.header()
    elif choice == "inline-code":
        choice += marks.header()
    elif choice == "bold":
        choice += marks.header()

    elif choice not in formats:
        print("Unknown formatting type or command")


