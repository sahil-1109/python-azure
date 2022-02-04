intro = input('Greetings, Enter the message you want to modify: ')
if( intro.startswith('G')):
    intro.replace('hello', 'Your message is replaced')
elif(intro.endswith('?')):
    intro.replace('?','greet,dont ask!')
print(intro)
