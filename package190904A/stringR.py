class string(str):
    s=''
    def __init__(self,st):
        print("ok",st)
        self.s=st
    def capitalize(self):
        return self.s