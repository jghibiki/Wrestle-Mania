init python:
    class Char:
        def __init__(self):
            self.strength = 0
            self.speed = 0
            self.cunning = 0
            self.karma = 0
            self.weight = 0
            self.maxStat = 30

        def incStat(self, stat, length):
            if str(stat) == "strength":
                if self.strength+length <= self.maxStat: 
                    self.strength += length
                else:
                    self.strength = self.maxStat
            elif str(stat) == "speed":
                if self.speed+length <= self.maxStat:
                    self.speed += length
                else:
                    self.speed = self.maxStat
            elif str(stat) == "cunning":
                if self.cunning+length <= self.maxStat:
                    self.cunning += length
                else:
                    self.speed = maxStat 
                
            elif str(stat) == "karma":
                if self.karma+length <= self.maxStat:
                    self.karma += length
                else:
                    self.karma = self.maxLength
            elif str(stat) == "weight":
                if self.weight+length <= self.maxStat:
                    self.weight += length
                else:
                    self.weight = self.maxLength
            else:
                postError("Stat name typo")

    class Time:
        def __init__(self):
            self.time_in_day = 12
            self.days_to_go = 24
            self.current_time = 0
            self.current_day = 1

        def incHour(self, num):
            temp = num + self.current_time
            if temp <= self.time_in_day:
                self.current_time = temp
                return True
            else:
                return False

        def isEndOfDay(self):
            if self.current_time == self.time_in_day:
                return True
            else:
                return False

        def incDay(self):
            if (self.current_day + 1) <= self.days_to_go:
                self.current_day += 1
                return True
            else:
                return False

        def getCurrentDay(self):
            return self.current_day

        def getTime(self):
            return self.current_time
