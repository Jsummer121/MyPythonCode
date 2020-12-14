# -*- coding: utf-8 -*-
class pig:
    def __init__(self,name,weigt,height, like, dislike):
        self.weigt = weigt
        self.height = height
        self.like = like
        self.dislike = dislike
        self.name = name

    def pi(self):
        print("%s的身高为%scm,体重为%skg"%(self.name,self.height,self.weigt))

    def alike(self):
        print('%s喜欢%s，不喜欢%s'%(self.name,self.like,self.dislike))

wanting = pig('周婉婷',300,140,'肉肉','葱花')
wanting.pi()
wanting.alike()



