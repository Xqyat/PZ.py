class NoteTwo:
    def __init__(self, text, iscompleted):
        self.text = text
        self.iscompleted = iscompleted
        self.count = 0

    def upcount(self, count):
        self.count += count

    def reset_count(self):
        self.count = 0

note1 = NoteTwo("Task1", False)
print(note1.__dict__)
print(note1.count)
note1.upcount(8)
print(note1.count)
note1.reset_count()
print(note1.count)
