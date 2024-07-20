import random
from playsound import playsound
import time



class Merge_Sort_A():
    def __init__(self):
        self.Arrayempty = []

    def array_maximun_randomize(self,maximun_element):
        for _ in range (maximun_element):
            self.Arrayempty.append(random.randint(1,maximun_element))  