def print_book_info(title, author=None, year=None):
    #  Write your code here
    output = f'"{title}"'
    if author is not None or year is not None:
        output += ' was written'
    if author is not None:
        output += f' by {author}'
    if year is not None:
        output += f' in {year}'
    print(output)
