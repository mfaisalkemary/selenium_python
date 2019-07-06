class parent:
    parentAttr=20

    def __init__(self):
        print('this is the parent constructor')

    def parentMethod(self):
        print('this is the parent method')

    def parentsetter(self,attr):
        parent.parentAttr=attr

    def parentGetter(self):
        print(parent.parentAttr)

class child(parent):
    def __init__(self):
        print('this is the child constructor')

    def childMethod(self):
        print('this is the child method')

    def parentMethod(self):
        print('this is the ovverridden method')

c=child()
c.childMethod()
c.parentMethod()
c.parentsetter(346789)
c.parentGetter()
