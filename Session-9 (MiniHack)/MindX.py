from datetime import date
class Old_Techkids:
    def dayTogether (self, FirstDate, EndDate):
        self.FirstDate = FirstDate
        self.EndDate = EndDate
        DayTogether = EndDate - FirstDate
class New_MindX( Old_Techkids ):
    def MindX(self):
        FirstDate = Old_Techkids.FirstDate
        EndDate = date(2019, 1, 4)
        DayTogether = EndDate - FirstDate
class LoveBucket:
    def love(self, Together):
        love = 0
        Together = Old_Techkids.DayTogether - New_MindX.DayTogether
        for i in range (Together + 1):
            love += 1
    def loveDisplay(self):
        print("Love MindX %i", love, "times")

