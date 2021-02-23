# users = ["Test User", "Real User 1", "Real User 2"]
# for index, user in enumerate(users):
#     if index == 0:
#         print("Extra verbose output for:", user)
#     else:
#         print(user)
#
#
#
# list_of_values = [qwe for qwe in range(10, 0, -1)]
# print(list_of_values)
#
# def even_items(iterable):
#     """Return items from ``iterable`` when their index is even."""
#     return [v for i, v in enumerate(iterable, start=1) if not i % 2]
#
# print(even_items(list_of_values))

alphabet = "abcdefghijklmnopqrstuvwxyz"

print(list(alphabet[1::2]))

def alphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    yield alpha

alphabet()