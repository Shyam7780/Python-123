#Multipal inheritace Class


class G_Father:
    def house(self):
        print('House')

class Father(G_Father):
    def car(self):
        print('My Car')
class child(Father):
    pass
C1=child()
C1.house()
C1.car()