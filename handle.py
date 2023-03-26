import random
import re

def handle_response(message, client) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"
    if p_message.startswith('!avatar'):
        #match = re.match(r'^!avatar\s*<@!?(\d+)>', p_message)
        # Split the message into a list of words
        words = p_message.split()
        if len(words) > 1:
        #if match:
            # Get the user ID from the match
            #user_id = int(match.group(1))
            # Get the user mention from the message
            user_mention = words[1]
            if user_mention.startswith("<@!") and user_mention.endswith(">"):
                # Get the user ID from the mention
                user_id = user_mention.strip('<@!>')
                # Get the user object from the ID
                user = client.get_user(int(user_id))
                if user is not None:
                    # Return the URL of the user's avatar
                    return user.avatar_url
                else:
                    return "Invalid user mention. Please provide a valid user mention."
            # Return the URL of the user's avatar
            else:
                # If no user mention is provided, return an error message
                #return "Please provide a user mention to get their avatar."
                print(f"user_mention: {user_mention}")
                #print(f"user_id: {user_id}")


    #  return 'Yeah, I don\'t know. Try typing "!help".'