from enum import Enum
import datetime
from math import sqrt

class Subcategory():
    def __init__(self, name:str, base_score):
        assert type(name) == str
        self.name = name
        self.base_score = base_score

        self.tasks = []


    def get_score(self, include_unfinished):
        score = 0
        for task in self.tasks:
<<<<<<< Updated upstream
            if task.finished == True or include_unfinished:
                score += self.base_score + task.rating * self.base_score
=======
            if task.finished or include_unfinished:
                score += sqrt(task.duration) * (self.base_score + int(task.rating) * 0.5*self.base_score)
>>>>>>> Stashed changes
        return score
            

class Category():
    catagories = []
    def __init__(self, name:str, subcatagories):
        self.name = name
        self.subcategories = subcatagories
        self.general = Subcategory('', base_score=1)

        Category.catagories.append(self)
    
    
    def get_total(self):
        total = 0
        for subcategory in self.subcategories:
            total += subcategory.get_score()

        return total
    


class Health(Category):
    def __init__(self):
        Category.__init__(self, name='Health', subcatagories= {
                            'physical': Subcategory('physical', 1),
                            'mental': Subcategory('mental', 1),
                            'sleep': Subcategory('sleep', 1),
                            })


class Relationships(Category):
    def __init__(self):
        Category.__init__(self, name='Relationships', subcatagories= {
                            'family': Subcategory('family', 1),
                            'friends': Subcategory('friends', 1),
                            'romantic': Subcategory('romantic', 1),
                            })


class Environment(Category):
    def __init__(self):
        Category.__init__(self, name='Environment', subcatagories= {})



class Knowledge_Wisdom(Category):
    def __init__(self):
        Category.__init__(self, name='Knowledge/Wisdom', subcatagories= {
                            'soft skills': Subcategory('soft skills', 1),
                            'hard skills': Subcategory('hard skills', 1),
                            })


class Spirituality(Category):
    def __init__(self):
        Category.__init__(self, name='Spirituality', subcatagories= {})


class Career(Category):
    def __init__(self):
        Category.__init__(self, name='Career', subcatagories= {
                            'professional development': Subcategory('professional development', 1),
                            'work': Subcategory('work', 1),
                            })
class Task():
    def __init__(self, label:str, category:Category, subcategory:Subcategory, duration:float, finished:bool, rating=0):
        self.label = label
        self.category = category
        self.subCategory = subcategory
        self.duration = duration
        self.finished = finished
        self.rating = rating


    def __repr__(self):
        return f'''A Task of Label: {self.label}\n
                Category: {self.category.name}\n
                subCategory: {self.subCategory.name}\n'''

class User():
    '''
    The user class stores login info, tasks and current stats
    '''
    def __init__(self, f_name:str, l_name:str, password:str):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password

        self.health = Health()
        self.relationships = Relationships()
        self.environment = Environment()
        self.knowledge = Knowledge_Wisdom()
        self.spirituality = Spirituality()
        self.career = Career()
    
    def __repr__(self) -> str:
        return f"{self.f_name} A current user"
    

    def add_task(self, label:str, category:str, sub_category:str, rating:str, duration:str):
        for main_category in Category.catagories:
            if main_category.name == category:
                #Add to the general list if the task doesnt have a sub category
                if sub_category is None:
                    task = Task(label=label, category=main_category, subcategory=main_category.general, 
<<<<<<< Updated upstream
                    date=None, finished=True, rating=rating)
                    print(task)
=======
                    duration=float(duration), finished=True, rating=rating)
>>>>>>> Stashed changes
                    main_category.general.tasks.append(task)
                
                #Add to the subtask object if it does exist
                else:
                    for sub in main_category.subcategories.values():
                        if sub.name == sub_category:
                            task = Task(label=label, category=main_category, subcategory=sub, 
<<<<<<< Updated upstream
                            date=None, finished=True, rating=rating)
                            print(task)
=======
                            duration=float(duration), finished=True, rating=rating)
>>>>>>> Stashed changes
                            sub.tasks.append(task)
    
    def get_piechart(self, completed=True):
        return {'Health': self.health.get_total(),
                'Relationships': self.relationships.get_total(),
                'Environment': self.environment.get_total(),
                'Knowledge': self.knowledge.get_total(),
                'Spirituality': self.spirituality.get_total(),
                'Career': self.career.get_total()}
            
