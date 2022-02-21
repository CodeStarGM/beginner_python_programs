print("""
+---------------------+
| Enter short form of |
|any programming word |
+---------------------+
""")


while True:
    user_input = input('Enter The Short form : ')
    pro_abs = {'HTML': 'Hyper Text Markup Language', 'CSS': 'Cascading Style Sheet', 'JS': 'Javascript','WWW':'World Wide Web'}

    user_input = user_input.upper()
    
    if user_input == 'Q':
        break
    print("The Answer is =>",pro_abs[user_input])
    print('press "Q" to quit')

    

    