#--------------------------------------------StarDataAbstractor.py--------------------------------------------#

'''
Importing modules:
-csv
-sys
-time (tm)
'''
import csv
import sys
import time as tm


print("Welcome to StarDataAbstractor.py")
print("We provide abstraction algorithms for a particular dataset of stars.")

tm.sleep(1.3)
print("Loading Data...")

tm.sleep(3.4)


#Defining a function to choose the appropriate star characteristic to be abstracted upon
def ChooseComparitiveParameter():
  
  characteristic_list=["Unusable_Element","Mass","Gravity","Distance","Radius"]

  #Running a for loop over the enumerated list of star characteristics to display the options to the user 
  for characteristic_index,characteristic in enumerate(characteristic_list):

    #Verifying whether the index is equal to zero or not to prevent the display of "Unusable_Element"
    #Case-1
    if characteristic_index!=0:
      print("{}:{}".format(characteristic_index,characteristic))

  characteristic_input=int(input("Please enter the index of the star characteristic desired to compare with:"))  

  #Running a try-except block to verify the validity of the user's input
  #Try block
  try:
    user_test_a=characteristic_list[characteristic_input]

    #Verifying whether the user's input is equal to zero or not
    #Case-1
    if characteristic_input==0:
      sys.exit("Invalid Input.")
  #Except block    
  except:
    sys.exit("Invalid Input. Don't add commas, or any other special cahracters except '.'")    

  user_choice=characteristic_list[characteristic_input]

  #Returning the user's choice and index of the desired charcteristic to compare
  return user_choice,characteristic_input


#Defining a function to finalise the mode of comparison and the value of abstraction
def DefineComparisonParameters():
  mode_list=["Unusable_Element","Remove Values Greater Than","Remove Values Lesser Than"]

  #Running a for loop over the enumerated list of comparison modes to display the options to the user 
  for mode_index,mode in enumerate(mode_list):

    #Verifying whether the index is equal to zero or not to prevent the display of "Unusable_Element"
    #Case-1
    if mode_index!=0:
      print("{}:{}".format(mode_index,mode))

  mode_input=int(input("Please enter the index of the mode of comaprison and selection:"))  

  #Running a try-except block to verify the validity of the user's input
  #Try block
  try:
    user_test_b=mode_list[mode_input]

    #Verifying whether the user's input is equal to zero or not
    #Case-1
    if mode_input==0:
      sys.exit("Invalid Input.")
  #Except block     
  except:
    sys.exit("Invalid Input.")

  user_choice=mode_list[mode_input] 

  value_input_global=None

  #Running a try-except block to verify the validity of the user's input
  #Try block
  try:
    value_input=float(input("Please the magnitude of the comparison number:"))  
    value_input_global=value_input
  #Except block  
  except:
    sys.exit("Invalid Input")  

  #Returning the index of the mode,and the value of abstraction provided by the user
  return mode_input,value_input_global  


reader_list_global=None

#Opening (Reading) data from the file 'data.csv' to obtain the primary data
with open("data.csv",'r') as fl:
  reader=csv.reader(fl)
  reader_list_global=list(reader)


headings=reader_list_global.pop(0)

comparison_field,comparison_index=ChooseComparitiveParameter()

comparison_method,comparison_value=DefineComparisonParameters()

#Running a for loop over the enumerated main data list to abstract values on the basis of user-provided data
for star_set_index,star_set in enumerate(reader_list_global):

  #Assessing the mode prescribed by the user to abstract and conducting respective actions
  #cCase-1
  if comparison_method==1:

    #Verifying whether the value is greater than the value of abstraction or not
    #Case-1
    if  float(star_set[comparison_index])>comparison_value:
      reader_list_global.pop(star_set_index)
  #Case-1    
  if comparison_method==2:

    #Verifying whether the value is greater than the value of abstraction or not
    #Case-1
    if  float(star_set[comparison_index])<comparison_value:
      reader_list_global.pop(star_set_index)    


file_name=input("Please provide the file name of the file to be created: ")

#Verifying whether the file name stipulated by the user has a dot or not
#Case-1
if "." in file_name:
  file_name=file_name.split(".")[0]


#Opening (Creating) a new file of the name provided by the user containing the stipulated data
with open(file_name+".csv",'w') as wt:
  writer=csv.writer(wt)

  writer.writerow(headings)
  writer.writerows(reader_list_global)

#--------------------------------------------StarDataAbstractor.py--------------------------------------------#

