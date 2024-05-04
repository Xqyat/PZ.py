# # class Comment:
# #     count = 0
# #     def __init__(self, text):
# #         self.text = text
# #
# #     @staticmethod
# #     def merge_comments(first, second):
# #         return f"{first}{second}"
# #     def upcount(self):
# #         self.count += 1
# # my_comment = Comment("My comment")
# # my_comment.upcount()
# # print(my_comment.count)
# # my_comment.count = 17
# # print(my_comment.__dict__)
# # print(my_comment.count)
# #
# # print(Comment.count)
# # print(Comment.__dict__)
# #
# # # m_1 = Comment.merge_comments("Привет","студент!")
# # # print(m_1)
# # # m_2 = Comment.merge_comments("Great","OK")
# # # print(m_2)
# #1
# class Image:
# #2
#
#     def __init__(self, resolution, title, extension):
#         self.resolution = resolution
#         self.title = title
#         self.extension = extension
# #3
#     def resize(self, resolution):
#         self.resolution = resolution
# #4
#     def title_upper(self, title):
#         self.title = title.upper()
# f1 = Image(180,"hello", 400)
# f1.title_upper("hello people")
# print(f1.title)
# print(f1.__dict__)
#
# #5
# r1 = Image(80, "First resolution", 90)
# r1.resize(3)
# print(r1.resolution)
# r2 = Image(70, "Second resolution", 60)
# r2.resize(7)
# print(r2.resolution)
# r3 = Image(20, "Third resolution", 49)
# r3.resize(98)
# print(r3.resolution)
# #2
# print(Image.__dict__)
