from enum import Enum
import datetime

class SubCatagory():
    def __init__(self, name:str, base_score):
        assert type(name) == str
        self.name = name
        self.base_score = base_score

        self.tasks = []


    def get_score(self, include_unfinished):
        score = 0
        for task in self.tasks:
            if task.finished == True or include_unfinished:
                score += self.base_score + task.rating * self.base_score
        return score
            

class Catagory():
    catagories = []
    def __init__(self, name:str, subcatagories):
        self.name = name
        self.subcategories = subcatagories
        self.general = SubCatagory('', base_score=1)

        Catagory.catagories.append(self)
    
    
    def get_total(self):
        total = 0
        for subcategory in self.subcategories:
            total += subcategory.get_score()

        return total
    

    


class Health(Catagory):
    def __init__(self):
        Catagory.__init__(self, name='Health', subcatagories= {
                            'physical': SubCatagory('physical', 1),
                            'mental': SubCatagory('mental', 1),
                            'sleep': SubCatagory('sleep', 1),
                            })



class Relationships(Catagory):
     def __init__(self):
         Catagory.__init__(self, name='Relationships')
         self.subcatagories = {'family': 1,
                          'friends': 1,
                          'romantic': 1,
                          }


class Environment(Catagory):
     def __init__(self):
         Catagory.__init__(self, name='Health')
         self.subcatagories = {}



class Knowledge_Wisdom(Catagory):
     def __init__(self):
         Catagory.__init__(self, name='Knowledge/Wisdom')
         self.subcatagories = {
                               "Soft Skills": 1,
                               "Hard Skills": 1}


class Spirituality(Catagory):
     def __init__(self):
         Catagory.__init__(self, name='Spirituality')


class Career(Catagory):
     def __init__(self):
         Catagory.__init__(self, name='Career')
         self.subcatagories = {
                               "Professional development": 1,
                               "Work": 1,}
class task():
    def __init__(self, label:str, catagory:Catagory, subCatagory, date:datetime.datetime, finished:bool, rating=0):
        self.label = label
        self.catagory = catagory
        self.subCatagory = subCatagory
        self.date = date
        self.finished = finished
        self.rating = rating


class User():
    '''
    The user class stores login info, tasks and current stats
    '''
    def __init__(self, f_name:str, l_name:str, password:str):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password
    
    def __repr__(self) -> str:
        return f"{self.fname} A current user"
