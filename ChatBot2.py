#01 import librabries
import random
from textblob import TextBlob

#02 name and nickname conversation
print('Hello human what is ur name?')
name=input()
print('Do u have a nickname?')
ans=input()
if 'y' in ans.lower():
    nickname=input('What is ur nickanme?\n')
    print('Good to see u '+nickname)
else:
    nickname=name +'shu'
    print("I will call u "+nickname)

#03 greeting selection
greetings=[
    'How r u today '+nickname+'?',
    'How is ur day going '+nickname+'?',
    'Wassup '+nickname+'?',
    'Are u feeling well '+nickname+'?',
    'How are things going '+nickname+'?',
    'How r u feeling '+nickname+'?'
]

print(random.choice(greetings))
ans=input()
blob=TextBlob(ans)
if blob.polarity > 0:
    print('Glad u r doing well')
else:
    print('Sorry to hear that')

#04 several random opinions on topic
topics=[
    'Condition Zero',
    'Cricket',
    'Politics',
    'Avengers',
    'Games',
    'Computers',
    'College',
    'India'
]

questions=[
    'Do u like ',
    'What is ur opinion on ',
    'What do u think about ',
    'What is ur take on ',
    'What is ur rating on '

]
for i in range(0,random.randint(3,4)):
    question=random.choice(questions)
    questions.remove(question)
    topic=random.choice(topics)
    topics.remove(topic)
    print(question+topic+'?')
    ans=input()
    blob=TextBlob(ans)
    if blob.polarity > 0.5:
        print('Omg u really love '+topic)
    elif blob.polarity > 0.1:
        print('Well u clearly like '+topic)
    elif blob.polarity < -0.5:
        print('Woo, you totally hate '+topic)
    elif blob.polarity < -0.1:
        print("So u don't like "+topic)
    else:
        print('That is a very neutral view on '+topic)

#05 random goodbye
goodbye=[
    'It was nice talking to u '+nickname+' I gotta go now',
    'Ok I am bored '+nickname+' I will go and watch Netflix',
    'Bye Bye '+nickname+' I am going',
    'Talk to u later byee '+nickname,
    'Byee '+nickname+' I want to sleep now'

]

print(random.choice(goodbye))