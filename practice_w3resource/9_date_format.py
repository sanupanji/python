'''
Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
'''

def date_format(dat):

    return dat.replace(',','/')

print(date_format(input("Enter date in dd,mm,yyyy format : ")))
