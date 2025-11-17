# import pandas as pd
# import random
# import datetime

# # Define users
# usernames = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack",
#              "Karen", "Liam", "Mona", "Ned", "Olivia", "Paul", "Quincy", "Rita", "Sam", "Tina"]

# # Complete list of comments
# comments = [
#     "You are such an idiot! I can't believe you did that.",
#     "Stop being so pathetic. You always ruin everything.",
#     "This is the worst idea ever. I can't believe you thought it would work.",
#     "I can't believe how dumb that was. Are you serious?",
#     "You should just quit. You're not good at this.",
#     "You look so ugly in that outfit. What were you thinking?",
#     "You're a complete loser. Nobody likes you.",
#     "What a stupid thing to say. Do you even think before speaking?",
#     "That's just plain dumb. Why would you even suggest that?",
#     "I hate you. You're the worst person I know.",
#     "You make me sick. I can't stand being around you.",
#     "You're worthless. You contribute nothing to this team.",
#     "You're a failure. You always mess things up.",
#     "I can't stand you. You're so annoying.",
#     "You're such a coward. You never stand up for yourself.",
#     "You're a fat pig. You need to lose some weight.",
#     "You have no friends because you're so annoying.",
#     "Nobody likes you. You should just leave.",
#     "You're a waste of space. Nobody wants you here.",
#     "You're so annoying. Why do you even bother?",
#     "You should just disappear. Nobody would miss you.",
#     "You're a disgrace. You've embarrassed everyone.",
#     "You're an embarrassment. I can't believe we're related.",
#     "You're hopeless. You'll never amount to anything.",
#     "You're a freak. Everyone thinks so.",
#     "You're a joke. Nobody takes you seriously.",
#     "You're a weirdo. You creep everyone out.",
#     "You're a creep. Stay away from me.",
#     "You're a psycho. You need help.",
#     "You're a pathetic loser. Get a life.",
#     "You should be ashamed of yourself. How could you do that?",
#     "You're disgusting. Just looking at you makes me sick.",
#     "You're a moron. Do you even have a brain?",
#     "You're a dumbass. I can't believe you did that.",
#     "You're a pain in the ass. Nobody wants to deal with you.",
#     "You're a piece of crap. I can't stand you.",
#     "You're a waste of oxygen. You shouldn't even be alive.",
#     "You're an idiot. Plain and simple.",
#     "You're a dipshit. You never get anything right.",
#     "You're a fool. Everyone laughs at you.",
#     "You're an ass. Nobody likes you.",
#     "You're a loser. You never win at anything.",
#     "You're stupid. It's a wonder you can even talk.",
#     "You're a dummy. You make no sense.",
#     "You're worthless. Just leave.",
#     "You're a nobody. Nobody cares about you.",
#     "You're garbage. Absolute trash.",
#     "You're trash. Pure filth.",
#     "You're scum. Lowest of the low.",
#     "You're filth. Disgusting.",
#     "You're dirt. Beneath everyone.",
#     "You're slime. Slippery and gross.",
#     "You're a bastard. A real piece of work.",
#     "You're a son of a bitch. Nobody likes you.",
#     "You're a prick. Always causing trouble.",
#     "You're a douche. Nobody can stand you.",
#     "You're a dick. Always a problem.",
#     "You're a jerk. Never nice to anyone.",
#     "You're a loser. Always have been, always will be.",
#     "You're a moron. Absolutely clueless.",
#     "You're a dumbass. Never get anything right.",
#     "You're an idiot. Completely hopeless.",
#     "You're a fool. Always messing things up.",
#     "You're a dumbass. Can't believe you did that.",
#     "You're a piece of shit. Worthless.",
#     "You're a loser. Nobody cares about you.",
#     "You're stupid. A complete idiot.",
#     "You're dumb. Can't believe how dumb.",
#     "You're a retard. Absolutely brainless.",
#     "You're an imbecile. Completely useless.",
#     "You're a knucklehead. Always a problem.",
#     "You're a meathead. Always causing trouble.",
#     "You're a blockhead. Never get anything right.",
#     "You're a numbskull. Always in the way.",
#     "You're a nincompoop. Absolutely useless.",
#     "You're a dunderhead. Can't believe how dumb.",
#     "You're a bonehead. Always causing trouble.",
#     "You're a chowderhead. Completely hopeless.",
#     "You're a chucklehead. Always a problem.",
#     "You're a birdbrain. Completely useless.",
#     "You're a pea-brain. Absolutely brainless.",
#     "You're a pinhead. Always causing trouble.",
#     "You're a butt-head. Never get anything right.",
#     "You're a dimwit. Completely useless.",
#     "You're a halfwit. Absolutely hopeless.",
#     "You're a nitwit. Can't believe how dumb.",
#     "You're a twit. Always a problem.",
#     "You're a twerp. Completely useless.",
#     "You're a nerd. Always causing trouble.",
#     "You're a dork. Completely hopeless.",
#     "You're a geek. Always a problem.",
#     "You're a dweeb. Completely useless.",
#     "You're a nerd. Can't believe how dumb.",
#     "You're a dork. Always causing trouble.",
#     "You're a geek. Completely hopeless.",
#     "You're a dweeb. Always a problem.",
#     "You're a nerd. Absolutely useless.",
#     "You're a dork. Completely brainless.",
#     "You're a geek. Always causing trouble.",
#     "You're a dweeb. Completely hopeless.",
#     "You're a nerd. Always a problem.",
#     "You're a dork. Absolutely brainless.",
#     "You're a geek. Always causing trouble.",
#     "You're a dweeb. Completely hopeless.",
#     "You're a nerd. Always a problem.",
#     "You're a dork. Absolutely brainless.",
#     "You're a geek. Always causing trouble.",
#     "You're a dweeb. Completely hopeless.",
#     "You're a nerd. Always a problem.",
#     "You're a dork. Absolutely brainless.",
#     "You're a geek. Always causing trouble.",
#     "You're a dweeb. Completely hopeless."
# ]

# # Ensure we have exactly 200 comments
# if len(comments) < 200:
#     while len(comments) < 200:
#         comments.extend(comments)
# comments = comments[:200]

# # Define label categories
# labels = ["toxic", "severe toxic", "obscene", "threat", "insult", "identity hate"]

# # Random time intervals (seconds)
# time_intervals = [1, 2, 5, 6, 120, 240, 600, 900]  # Intervals ranging from seconds to minutes

# # Assign comments to users with date, time, and label
# chat_data = []
# start_time = datetime.datetime.now()

# for i in range(200):
#     user = random.choice(usernames)
#     message = comments[i]
#     label = random.choice(labels)
    
#     # Randomly increment the time
#     increment = datetime.timedelta(seconds=random.choice(time_intervals))
#     current_time = start_time + increment
#     start_time = current_time  # Update start_time for the next iteration
    
#     # Format date and time
#     date_time = current_time.strftime('%m/%d/%Y, %I:%M%p')
    
#     chat_data.append({
#         "Name": user,
#         "Comments": message,
#         "Date and Time": date_time,
#         "Label": label
#     })

# # Create DataFrame and save to CSV
# chats_df = pd.DataFrame(chat_data)
# chats_df.to_csv('chats.csv', index=False)
import re

def is_valid_regex(s):
    try:
        re.compile(s)
        # If we can compile, let's try using it with a simple match
        re.match(s, '')
        return True
    except re.error:
        return False

# Input handling
T = int(input())
results = []
for _ in range(T):
    S = input()
    results.append(is_valid_regex(S))

# Output results
for result in results:
    print(result)
