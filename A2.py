import random
from playsound import playsound
import time

class Merge_Sort_A():
    def __init__(self):
        self.Arrayempty = []

    def array_maximun_randomize(self,maximun_element):
        for _ in range (maximun_element):
            self.Arrayempty.append(random.randint(1,maximun_element)) 

    def split_Arrays(self, Arrayempty= None):

        if Arrayempty is None:
            Arrayempty = self.Arrayempty

        if len(Arrayempty) <= 1:

            return Arrayempty
        
        halfpoint = len(Arrayempty)//2
        self.sounds_for_sort()
        print("Half point position: ", halfpoint)

        left_half = Arrayempty[:halfpoint]
        self.sounds_for_sort()
        print("Left Half", left_half)
       
        right_half = Arrayempty[halfpoint:]
        self.sounds_for_sort()
        print("Right Half", right_half)
        
        split_left = self.split_Arrays(left_half)
        self.sounds_for_sort()
        print("Splilt Left ", split_left)
        
        split_right = self.split_Arrays(right_half)
        self.sounds_for_sort()
        print("Split Right ", split_right)
        
        return self.merge_sort(split_left, split_right)