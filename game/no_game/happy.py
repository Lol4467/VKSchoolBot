import random
 
greetings = ["'How can I help you?'", "'...'", "'Next!'"]
MOODS = ('bad', 'average', 'good')
RANKS = ('low', 'medium', 'high')
 
 
class Bureaucrat:
    '''A government employee who works in the Institution.'''
 
    def __init__(self):
        self.rank = random.choice(RANKS)
        self.mood = random.choice(MOODS)
 
    def greet(self):
        '''A random greeting from the government employee.'''
 
        print(random.choice(greetings))
        print('The bureaucrat is of a {} rank.'.format(bureaucrat.rank))
        print('The bureaucrats mood seems to be {}.'.format(bureaucrat.mood))
 
bureaucrat = Bureaucrat()
bureaucrat.greet()