import random
import time as tim
word=["Afghanistan", "Albania", "Algeria", "Andorra" ,"Angola", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Baden", "Bahamas", "Bangladesh", "Belgium", "Bolivia", "Bosnia", "Botswana", "Brazil" ,"Bulgaria", "Burma", "Burundi", "Cambodia" ,"cameroon", "Canada", "Chad" ,"Chile" ,
      "China" ,"Colombia", "Comoros" ,"Costa Rica", "Croatia", "Cuba" ,"Cyprus" ,"Czechia", "Denmark", "Dominica" ,"Ecuador", "Egypt", "Estonia" ,"Ethiopia", "Fiji" ,"Finland", "France", "Gabon", "Gambia" ,"Georgia", "Germany", "Ghana", "Greece", "Grenada" ,"Guatemala", "Guinea" ,"Haiti", "Honduras", "Hungary",
      "Iceland", "India", "Indonesia", "Iran" ,"Iraq", "Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya" ,"Kiribati", "Korea North", "Korea South", "Kosovo" ,"Kuwait", "Kyrgyzstan", "Laos" ,"Latvia" ,"Lebanon",  "Liberia", "Libya", "Lithuania", "Luxembourg", "Macedonia" ,
      "Madagascar" ,"Malawi" ,"Malaysia", "Maldives", "Mali" ,"Malta", "Mauritania", "Mauritius", "Mexico", "Micronesia" ,"Moldova" ,"Monaco" ,"Mongolia", "Morocco",  "Myanmar", "Nepal" ,"Netherlands", "New Zealand", "Niger" ,"Nigeria", "Norway" ,"Oman" ,"Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay",
      "Peru" ,"Philippines", "Poland", "Portugal", "Qatar", "Romania", "Samoa", "Saudi Arabia" ,"Senegal", "Serbia" ,"Singapore" ,"Slovakia", "Somalia", "South Africa", "Spain" ,"Sri Lanka", "Sudan" ,"Sweden" ,
      "Switzerland", "Syria" ,"Taiwan" ,"Tajikistan", "Tanzania", "Thailand", "Tonga", "Tunisia", "Turkey", "Tuvalu" ,"Uganda" ,"Ukraine", "United Arab Emirates" ,"United Kingdom" ,"United States" ,"Uruguay" ,"Uzbekistan", "Vanuatu" ,"Vatican City", "Venezuela", "Vietnam" ,"Yemen" ,"Zambia", "Zimbabwe"]
ran=random.choice(word)
name=str(input("enter your name: "))
print("please wait")
tim.sleep(3)
print("hi",name,''' this is guess the country game where you enters alphbets
if that letter is present in the word then you will get "correct placement" if not "try again"
you will be given 12 chances''')
n=0
while n<13:
    user=str(input("enter an alphabet"))
    if user in ran:
        print("correct placement")
    else:
        print("try again")
    n=n+1
final=str(input("guess the country"))
if final==ran:
    print("congratulation")
else:
    print("oops! try again")
print(ran)
