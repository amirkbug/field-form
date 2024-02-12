class info():
    def __init__(self,fname,lname,score) :
        self.fname = fname
        self.lname = lname
        self.score = score
    def state(self,score):
        self.score = score
        if self.score <= 20 and self.score >=18:
            return 'very good'
        elif self.score < 18 and self.score >=15:
            return 'good'
        elif self.score < 15 and self.score >=12:
            return 'not bad'
        elif self.score < 12 and self.score >=10:
            return 'bad'
        elif self.score < 10 and self.score >=0:
            return 'very bad'
        else:
            return 'out of range'