'''
Begin with "Welcome to the Cybersecurity Mission".
Ask the user to "trace the hacker" or "secure the system".
If "trace the hacker", ask to "track their IP" or "decode their message".
    If "track their IP", print "You caught the hacker. You Win!".
    If "decode their message", print "The message was a trap. Game Over."
If "secure the system", ask to "shut down the server" or "upgrade the firewall".
    If "shut down the server", print "The attack was stopped. You Win!"
    If "upgrade the firewall", print "The hacker bypassed it. Game Over."
'''

print("Welcome to the Cybersecurity Mission!")
action = input("Do you want to 'trace the hacker' or 'secure the system'? ").lower()

if action == "Trace the hacker":
    sub_action = input("Do you want to 'track their IP' or 'decode their message'? ").lower()
    if sub_action == "track their ip":
        print("You caught the hacker. You Win!")
    elif sub_action == "decode their message":
        print("The message was a trap. Game Over.")
    else:
        print("Invalid choice.")
elif action == "secure the system":
    sub_action = input("Do you want to 'shut down the server' or 'upgrade the firewall'? ").lower()
    if sub_action == "shut down the server":
        print("The attack was stopped. You Win!")
    elif sub_action == "upgrade the firewall":
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")