# Prompting and Passing

# exercise that uses argv and input 
# prompt
from sys import argv


script, user_name = argv 
prompt = '-> ' # this will show on before answer
# ex:
# what is your name? 
# ->_


print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)


print(f"""
      Alright, so you said {likes} about liking me.
      You live in {lives}. Not sure where that is.
      And you have a {computer} computer. Nice!
      """)


# study drill  
# find the zork and adventure copy the zork and adventure ( text based adventure game )