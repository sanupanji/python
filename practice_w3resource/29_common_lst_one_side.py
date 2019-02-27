'''
Write a Python program to print out a set containing all the colors
from color_list_1 which are not present in color_list_2. Go to the editor
Test Data : 
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])
Expected Output : 
{'Black', 'White'}
'''

def common_lst_one_side(ls1,ls2):

    return  ls1.difference(ls2)

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

print(common_lst_one_side(color_list_1,color_list_2))
