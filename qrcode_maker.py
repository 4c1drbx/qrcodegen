import segno

linkQuest = input("Please paste the link here: ")
nameQuest = input("Please type the name of the file including the .png: ")
random_string = linkQuest

my_first_QR_code = segno.make(random_string)
my_first_QR_code.save(nameQuest, border=0, scale=20)