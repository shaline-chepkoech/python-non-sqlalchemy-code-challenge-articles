class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not(5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self._name = name
        self.articles = [] # list
        self.magazines = set() # set
        self.topic_areas = [] # list
        
    @property
    def name(self):
        return self._name
    
    def __repr__(self):
        return f"Author({self.name})"
    
    def add_article(self, title, magazine):
        article = Article(title, self, magazine)
        self.articles.append(article)
        self.magazines.add(magazine)
        magazine.add_article(article)
        return article

    def magazines(self):
        return list(self.magazines)

    def add_article(self, magazine, title):
        self.magazines.add(magazine)
        magazine.add_title(title)

    def topic_areas(self):
        return list(self.topic_areas)
   

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass