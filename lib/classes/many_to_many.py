class Article:
    all = []  # Class-level list to keep track of all articles

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")

        self.__author = author
        self.__magazine = magazine
        self.__title = title

        author._Author__articles.append(self)
        magazine.add_article(self)
        Article.all.append(self)  # Add this article to the class-level list

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine")
        self.__magazine = value

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author")
        self.__author = value
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(set(article.magazine for article in self.__articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        if article not in self.__articles:
            self.__articles.append(article)
        return article

    def topic_areas(self):
        if not self.__articles:
            return None
        return list(set(article.magazine.category for article in self.__articles))

class Magazine:
    instances = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string")
        self.__name = name
        self.__category = category
        self.__articles = []  # Initialize the __articles attribute
        Magazine.instances.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters")
        self.__name = value

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string")
        self.__category = value

    def add_article(self, article):
        if not isinstance(article, Article):
            raise Exception("Must be an instance of Article")
        self.__articles.append(article)

    def articles(self):
        return self.__articles

    def contributors(self):
        return list(set(article.author for article in self.__articles))

    def article_titles(self):
        if not self.__articles:
            return None
        return [article.title for article in self.__articles]

    def contributing_authors(self):
        author_count = {}
        for article in self.__articles: 
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1

        contributing_authors = [author for author, count in author_count.items() if count > 2]

        # Return None if no authors have written more than 2 articles
        return contributing_authors if contributing_authors else None


# class Magazine:
#     def __init__(self, name, category != ""):
#         self._name  = name
#         self._category = category

#     @property
#     def name_attribute(self):
#         return self._name
    
#     @name_attribute.setter
#     def name_attribute(self, value):
#         if not isinstance(value, str) and 2<=len(value)<=16:
#             pass

#     def category_attribute(self):
#         return self.category
    
#     @category_attribute.setter
#     def category_attribute(self, value):
#         if isinstance(value, str) and len(value) > 0:
#             self.category = value
 
#     def articles(self, item):
#         if isinstance(item, Article):
                
#                 many articles

#             pass #iterate over article list


  
#     def test_has_many_articles(self):
#         """magazine has many articles"""
#         author_1 = Author("Carry Bradshaw")
#         magazine_1 = Magazine("Vogue", "Fashion")
#         magazine_2 = Magazine("AD", "Architecture")
#         article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
#         article_2 = Article(author_1, magazine_1, "Dating life in NYC")
#         article_3 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")

#         assert len(magazine_1.articles()) == 2
#         assert len(magazine_2.articles()) == 1
#         assert article_1 in magazine_1.articles()
#         assert article_2 in magazine_1.articles()
#         assert article_3 not in magazine_1.articles()
#         assert article_3 in magazine_2.articles()

#     def test_articles_of_type_articles(self):
#         """magazine articles are of type Article"""
#         author_1 = Author("Carry Bradshaw")
#         magazine_1 = Magazine("Vogue", "Fashion")
#         magazine_2 = Magazine("AD", "Architecture")
#         Article(author_1, magazine_1, "How to wear a tutu with style")
#         Article(author_1, magazine_1, "Dating life in NYC")
#         Article(author_1, magazine_2, "2023 Eccentric Design Trends")

#         assert isinstance(magazine_1.articles()[0], Article)
#         assert isinstance(magazine_1.articles()[1], Article)
#         assert isinstance(magazine_2.articles()[0], Article)

#     def test_has_many_contributors(self):
#         """magazine has many contributors"""
#         author_1 = Author("Carry Bradshaw")
#         author_2 = Author("Nathaniel Hawthorne")
#         magazine_1 = Magazine("Vogue", "Fashion")
#         Article(author_1, magazine_1, "How to wear a tutu with style")
#         Article(author_2, magazine_1, "Dating life in NYC")

#         assert len(magazine_1.contributors()) == 2
#         assert author_1 in magazine_1.contributors()
#         assert author_2 in magazine_1.contributors()

#     def test_contributors_of_type_author(self):
#         """magazine contributors are of type Author"""
#         author_1 = Author("Carry Bradshaw")
#         author_2 = Author("Nathaniel Hawthorne")
#         magazine_1 = Magazine("Vogue", "Fashion")
#         Article(author_1, magazine_1, "How to wear a tutu with style")
#         Article(author_2, magazine_1, "Dating life in NYC")

#         assert isinstance(magazine_1.contributors()[0], Author)
#         assert isinstance(magazine_1.contributors()[1], Author)

#     def test_contributors_are_unique(self):
#         """magazine contributors are unique"""
#         author_1 = Author("Carry Bradshaw")
#         author_2 = Author("Nathaniel Hawthorne")
#         magazine_1 = Magazine("Vogue", "Fashion")
#         Article(author_1, magazine_1, "How to wear a tutu with style")
#         Article(author_1, magazine_1, "How to be single and happy")
#         Article(author_2, magazine_1, "Dating life in NYC")

#         assert len(set(magazine_1.contributors())) == len(magazine_1.contributors())
#         assert len(magazine_1.contributors()) == 2



# # class Article:
# #     all_articles = []

# #     def __init__(self, author, magazine, title: str):
# #         self._author = author
# #         self._magazine = magazine
# #         self._title = title
# #         Article.all_articles.append(self)

# #     @property
# #     def title(self):
# #         return self._title

# #     @property
# #     def author(self):
# #         return self._author

# #     @author.setter
# #     def author(self, value):
# #         if not isinstance(value, Author):
# #             raise TypeError("Author must be an instance of the Author class")
# #         self._author = value

# #     @property
# #     def magazine(self):
# #         return self._magazine

# #     @magazine.setter
# #     def magazine(self, value):
# #         if not isinstance(value, Magazine):
# #             raise TypeError("Magazine must be an instance of the Magazine class")
# #         self._magazine = value


# # class Author:
# #     def __init__(self, name):
# #         self._name = name

# #     @property
# #     def name(self):
# #         return self._name

# #     def articles(self):
# #         return [article for article in Article.all_articles if article.author == self]

# #     def magazines(self):
# #         return list(set(article.magazine for article in self.articles()))

# #     def add_article(self, magazine, title):
# #         return Article(self, magazine, title)

# #     def topic_areas(self):
# #         articles = self.articles()
# #         if not articles:
# #             return None
# #         return list(set(article.magazine.category for article in articles))


# # # magazine_1 = Magazine("Vogue", "Fashion")
# # # magazine_2 = Magazine("AD", "Architecture")

# # # article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")

# # # magazine_1.article_titles = "How to wear a tutu with style"

# # class Magazine:
# #     all_magazines = []


# #     def __init__(self, name: str, category: str):
# #         self._name = name
# #         self._category = category
# #         self._article_titles = []
# #         Magazine.all_magazines.append(self)

# #     @property
# #     def name(self):
# #         return self._name

# #     @name.setter
# #     def name(self, value):
# #         if not isinstance(value, str) and not (2 <= len(value) <= 16):
# #             raise ValueError("Name must be a string between 2 and 16 characters")
# #         self._name = value

# #     @property
# #     def category(self):
# #         return self._category

# #     @category.setter
# #     def category(self, value):
# #         if not isinstance(value, str) or len(value) <= 0:
# #             raise ValueError("Category must be a non-empty string")
# #         self._category = value

# #     def articles(self):
# #         return self._article_titles

# #     def add_article(self, article):
# #         if not isinstance(article, Article):
# #             raise TypeError("Article must be an instance of the Article class")
# #         self._article_titles.append(article)

# #     def contributors(self):
# #         authors = [article.author for article in self.articles]
# #         return list(set(authors))

# #     @classmethod
# #     def top_publisher(cls):
# #         if not cls.all_magazines:
# #             return None
# #         return max(cls.all_magazines, key=lambda x: len(x.articles()))


# #     def article_titles(self):
# #         return [article.title for article in self._articles]

# #     # def contributing_authors(self):
# #     #     authors = [article.author for article in self._articles]
# #     #     unique_authors = set(authors)
# #     #     return [author for author in unique_authors if authors.count(author) > 2]

# #     # def add_article(self, author, title):
# #     #     if not isinstance(author, Author):
# #     #         raise TypeError("Author must be an instance of Author")
# #     #     article = Article(author, self, title)
# #     #     self._articles.append(article)
# #     #     return article

# #     # @classmethod
# #     # def top_publisher(cls):
# #     #     if not cls.all_article_titles:
# #     #         return None
# #     #     return (author for author in cls.all_article_titles if len(author.articles) > 2)



# # # author creation
# # author_1 = Author("Carry Bradshaw")


# # author_2 = Author("Nathaniel Hawthorne")

# # # magazine creation
# # magazine_1 = Magazine("Vogue", "Fashion")
# # magazine_2 = Magazine("AD", "Architecture")

# # # articles
# # Article(author_1, magazine_1, "How to wear a tutu with style")
# # Article(author_1, magazine_1, "How to be single and happy")
# # Article(author_1, magazine_1, "Dating life in NYC")
# # Article(author_1, magazine_2, "Carrara Marble is so 2020")
# # Article(author_2, magazine_2, "2023 Eccentric Design Trends")
