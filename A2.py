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
    
    
    def merge_sort(self,left_half, right_half):
        sorted_array = []
        self.sounds_for_sort()
        print(f"Initial left_half: {left_half}")
        self.sounds_for_sort()
        print(f"Initial right_half: {right_half}")

        while (left_half and right_half):

            if left_half[0] < right_half[0]:
                    self.sounds_for_sort()
                    sorted_array.append(left_half[0])
                    print(f"Appending {left_half[0]} from left_half")
                    left_half.pop(0)
            else:
                    self.sounds_for_sort()
                    sorted_array.append(right_half[0])
                    print(f"Appending {right_half[0]} from right_half")
                    right_half.pop(0)

            self.sounds_for_sort()
            print(f"Current sorted_array: {sorted_array}")
            

            if left_half:
                self.sounds_for_sort()
                sorted_array += left_half
                print(f"Appending remaining left_half: {left_half}")
                

            if right_half:
                self.sounds_for_sort()
                sorted_array+= right_half
                print(f"Appending remaining right_half: {right_half}")
                
            return sorted_array
    
    def sounds_for_sort(self):
        playsound('Sound 3/Sound 3.mp3')
        time.sleep(0.1) 