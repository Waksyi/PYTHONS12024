#LUST TUPLE SESSION
#my_list = ['p','r','o','g','r','a','m','i','z']
#print(my_list[2:5])
#print(my_list[5:])
#print(my_list[:])

#create new list called ceit wiyh values ccit, ccdbm, ccns, ccait
CEIT = ["CCIT", "CCDMB", "CCNS", "CCAIT"]

#FUNCTIONS HAS BRACKETS AND METHODS HAS DOTS. PREDEFINED FUNCTIONS

CEIT.append("CCLSA")
#print("after append", CEIT)

#LIST CAN BE CHANGED OR UPDATED. STRINGS ARE IMMUTABLE, LISTS ARE MUTABLE
CEIT[2] = 'CCDCN'
#print(CEIT)

#DELETE SPECIFY INDEX NUMBER TO BE REMOVED ONE OR MORE ITEMS FROM THE LIST
#REMOVE IS TO DELETE A LIST OF ITEM
#EXERCISE REMOVING OR DELETING ITEMS FROM A LIST
#CEIT.remove('CCAIT')

#USING LENGTH FUNCTION
#print("TOTAL ELEMENTS: ", len(CEIT))


#TUPLES
#IF U HAVE DATA THAT DOESNT CHANGE IMPLEMENTING IT AS A TUPLE WILL GUARANTEE THAT IT REMAINS WRITE-PROTECTED
#TASK; CREATE NEW TUPLE; MYINFO, STORE NAME, AGE, PHONE NUMBER_CEITLIST
MYINFO = ("Waksie", 15, 3235600, (CEIT))
#print(MYINFO)
#print(type(MYINFO))

#exercises tuple
#a = (1, 2, 3, 4, 5)
#del(a)
#print(a)

#exercise q2
a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
print(a.count(1))
print(a.index(5))

#exercise3
my_touple = ()
print(my_touple)

touple = 4,6,8,10,12,14
print(touple)

mytouple2 = 4, "python", 9.3
print(mytouple2)

nestedtouple = "python", {4:5, 6:2, 8:2}, (5, 3, 5, 6)
print(nestedtouple)

#objects in python Strings"'"""", lists[], touples() and dictionary{}
