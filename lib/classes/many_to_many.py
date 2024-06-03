class Article:
    all_articles = []

    def __init__(self, author, magazine, title: str):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise AttributeError("title is an immutable string")


    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        self._magazine = value


class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        return list(set(article.magazine.category for article in articles))


class Magazine:
    all_article_titles = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all_article_titles.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        authors = [article.author for article in self._articles]
        return list(set(authors))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        unique_authors = set(authors)
        return [author for author in unique_authors if authors.count(author) > 2]

    def add_article(self, author, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    @classmethod
    def top_publisher(cls):
        if not cls.all_article_titles:
            return None
        return (author for author in cls.all_article_titles if len(author.articles) > 2)



# author creation
author_1 = Author("Carry Bradshaw")
author_2 = Author("Nathaniel Hawthorne")

# magazine creation
magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture")

# articles
Article(author_1, magazine_1, "How to wear a tutu with style")
Article(author_1, magazine_1, "How to be single and happy")
Article(author_1, magazine_1, "Dating life in NYC")
Article(author_1, magazine_2, "Carrara Marble is so 2020")
Article(author_2, magazine_2, "2023 Eccentric Design Trends")