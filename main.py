########### ARRAYS #############

fruits = ["apples", "banana", "elderberries", "cucumbers", "dates"]

# Data structures have 4 types of operation:
# Reading, searching, adding, deleting.

# Reading an array:

print(fruits[0])

# Searching in an array

print(fruits.index("apples"))

# Adding in an array

fruits.append("watermelon")
print(fruits)

# Deleting an element from an array

fruits.remove("watermelon")
print(fruits)

# TIME COMPLEXITY FOR ARRAY DATA STRUCTURE

# READING -> (MOST EFFICIENT OPERATION) 1 STEP BECAUSE computer
# has the ability to jump to any particular index in the array and peer inside.

# SEARCHING -> (LESS EFFICIENT) for N cells in an array, linear search will take a maximum of N steps.
# COMPUTER HAS TO CHECK EACH VALUE WITHIN THE ARRAY TO FIND THE VALUE WE ARE LOOKING FOR.
# IF THE VALUE WE ARE LOOKING FOR IS NOT WITHIN THE ARRAY, THE COMPUTER WILL LIKEWISE CHECK EACH VALUE STEP BY STEP
# UNTIL IT MAKES SURE THAT IT'S INDEED NOT WITHIN THE ARRAY.

# INSERTION -> (IN WORST-CASE SCENARIO, TAKES N+1 STEPS) The efficiency of inserting a new piece of data inside an array
# depends on where inside the array you’d like to insert it.

# insertion in a worst-case scenario can take up to N + 1 steps for an array containing N elements.
# This is because the worst-case scenario is inserting a value into the beginning of the array in
# which there are N shifts (every data element of the array) and one insertion.

############## SETS ################

# In any case, a set is an array with one simple constraint of not allowing duplicates.

example_set = ["a", "b", "c"] # no duplicates

# READING -> EXACTLY THE SAME AS READING AN ARRAY. TAKES ONE STEP FOR THE COMPUTER WITHIN A PARTICULAR INDEX.

# SEARCHING -> NO DIFFERENT FROM SEARCHING AN ELEMENT WITHIN AN ARRAY. it takes up to N STEPS.

# DELETION -> IDENTICAL TO DELETION WITHIN ARRAYS. it takes up to N steps to delete a value and move
# data to the left to close the gap.

# INSERTION -> DIFFERENT THAN INSERTION WITHIN ARRAYS. Insertion into a set in a best-case scenario will take N + 1

# Inserting a value at the end of a set, which was a best-case scenario for an array.
# With an array, the computer can insert a value at its end in a single step.
#
# With a set, however, the computer first needs to determine that this value doesn’t already exist in
# this set—because that’s what sets do: they prevent duplicate data. So every insert first requires a search.

# WORST-CASE SCENARIO - INSERTING AN ELEMENTS AT THE BEGINNING OF A SET
# TAKES N STEPS TO CHECK WHETHER THE SET DOES NOT HAVE A SIMILAR VALUE
# TAKES ANOTHER N STEPS TO SHIFT ALL THE DATA TO THE RIGHT
# ANOTHER FINAL STEP IS TO INSERT THE ACTUAL VALUE
# TOTAL: 2N +1 STEPS IN THE WORST CASE



