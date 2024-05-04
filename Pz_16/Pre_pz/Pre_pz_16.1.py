class Note:
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1

note1 = Note("Task1")
print(note1.__dict__)
print(dir(note1))
print(note1.text)
#
# note1.upcount()
# print(note1.count)
# note1.upcount()
# print(note1.count)

# print(note1.upcount)
# print(Note.upcount)

note2 = Note("Task2")
print(note2.__dict__)
print(dir(note2))
print(note2.text)