class News:

    def __init__(self,title,body):
        self._title = title
        self._body = body

    def __add__(self,other):
        new_title = self._title + other._title
        new_body = self._body + other._body
        return News(new_title,new_body)

    def get_title(self):
        return self._title

    def set_title(self,value):
        self._title = value

    def get_body(self):
        return self._body

    def set_body(self, value):
        self._body = value

    def __str__(self):
        return f'Title is {self._title}\nBody is{self._body} '



news1 = News('Football','..........')
news2 = News('Hockey','..........')

print(news1._title)
print(news1.get_title)
#r = news1.__add__(news2)

#news3 = News('Corona','.........')

#r= news1+news2 + news3
#print(r)