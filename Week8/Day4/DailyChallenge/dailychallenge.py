class Pagination:
    def __init__(self, items=None, pageSize=10):
        if items is None:
            items = []
        self.items = items
        if not self.items:
            self.items = []
        self.pageSize = int(pageSize)
        self.currentPage = 0

    def getVisibleItems(self):
        return self.items[self.currentPage: self.currentPage + self.pageSize]


    def firstPage(self):
        self.currentPage = 0

    def nextPage(self):
        if self.currentPage + self.pageSize >= len(self.items):
            print("text's ended")
        else:
            self.currentPage += self.pageSize
            return self

    def prevPage(self):
        if self.currentPage == 0:
            print("it's already a start")
        self.currentPage -= self.pageSize

    def lastPage(self):
        count = 0
        last_page = []
        for index in range(len(self.items)):
            if count % self.pageSize == 0:
                count = 0
                last_page = []
            last_page.append(index)
            count += 1
        self.currentPage = last_page[0]

    def goToPage(self, numPage):
        count = 1
        division_in_pages = {}

        for num, element in enumerate(self.items):
            if (num - 1) % self.pageSize == 0:
                count += 1
            else:
                division_in_pages[count] = [element]
        if numPage not in division_in_pages:
            if numPage > list(division_in_pages.keys())[-1]:
                return self.lastPage()
            else:
                return self.firstPage()

        page_root = self.items.index(*division_in_pages[numPage])
        self.currentPage = page_root



alphabetList = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(',')
page = Pagination(alphabetList, 4)

print(page.getVisibleItems())
# ["a", "b", "c", "d"]

page.nextPage()

print(page.getVisibleItems())
# ["e", "f", "g", "h"]

page.lastPage()

print(page.getVisibleItems())






















