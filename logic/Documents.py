# T00062598 - Josue Fadul Mejia


class Document(object):

    def __init__(self, id_document: int, title: str, no_pages: int, category: str, authors: str):
        self.id_document = id_document
        self.title = title
        self.no_pages = no_pages
        self.category = category
        self.authors = authors

    # methods
    @property
    def id_document(self) -> int:
        return self.id_document

    @id_document.setter
    def id_document(self, id_document: int):
        self._id_document = id_document

    @property
    def title(self) -> str:
        return self.title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def no_pages(self) -> int:
        return self.no_pages

    @no_pages.setter
    def no_pages(self, no_pages: int):
        self._no_pages = no_pages

    @property
    def category(self) -> str:
        return self.category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def authors(self) -> str:
        return self.authors

    @authors.setter
    def authors(self, authors: str):
        self._authors = authors

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.id_document, self.title, self.category, self.no_pages, self.authors)

    def see_document(self):
        print("\nID: " + str(self.id_document) + "\nTitle: " + self.title + "\nCategory:" + self.category + "\nAuthor: " + self.authors + "\nNumber of pages: " + str(self.no_pages))


if __name__ == '__main__':
    _id_document = int(input("Insert the Document ID: "))
    _title = str(input("Write the title: "))
    _category = str(input("Write the book category: "))
    _author = str(input("Write the Book author: "))
    _no_pages = int(input("Insert the Number of pages:"))

    J = Document(id_document=_id_document, title=_title, no_pages=_no_pages, category=_category, authors=_author)
    print(J)
