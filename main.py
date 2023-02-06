import random

Q =['Hi i am Q',
   'hey',
   'How are you',
   "i love most of marvel movies ",
   'Thank you '
   ]

while True:
    me = input('>')
    print(f"Q:{random.choice(Q)}")

