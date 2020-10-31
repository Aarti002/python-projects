
my_collection=[]
class Store:
    def __init__(self,name,title,status):
        self.name=name
        self.title=title
        self.status=status
    def add(self):
        flag=0
        for i in my_collection:
            if i['name']==self.name:
                print("Can't add this book already there!")
                flag=1
                break
        if flag==0:
            my_collection.append({
                'name':self.name,
                'title':self.title,
                'status':self.status
            })
    def delete(self):
        global my_collection
        pre=len(my_collection)
        my_collection=[i for i in my_collection if i['name']!=self.name]
        ne=len(my_collection)
        if ne==pre:
            print('Oops.. book is not present!')
        else:
            print('Deleted!')

    def print_st(self):
        print(my_collection)


if __name__=='__main__':
    ans=input('Wanna create your store?(y/n)')
    if ans=='y':
        x=0
        while(x!=4):
            print('Menu:',end="")
            print('1.Add a book')
            print('2.Delete a book')
            print('3.Print Library')
            print('4.Close store')
            x = int(input())

            if x==1:
                n = input('Provide name: ')
                t = input('Provide title: ')
                s = input('Provide status: ')
                obj = Store(n, t, s)
                obj.add()
            elif x==2:
                n=input('Which book you want to delete? ')
                n = input('Provide name: ')
                t = input('Provide title: ')
                s = input('Provide status: ')
                obj = Store(n, t, s)
                obj.delete()


            elif x==3:
                obj=Store('not given','not given','not given')
                obj.print_st()


    print("Okay! have a nice day.")






