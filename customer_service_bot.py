

name = input("What is your name? ")


print(name)

# Cool! We have the initial skeleton done, now we have to define `new_customer()` and `existing_customer()`.By breaking up our bot into a bunch of smaller functions we can build each piece incrementally and check our progress as we slowly build a fully functioning product.
# 
# ## Step 3
# Let's start with `existing_customer()`. The options **DNS Cable Company** wants users to be able to select are 
# 
#             [1] Television Support
#             [2] Internet Support
#             [3] Speak to a support representative. 
# 
# Have `existing_customer()` print "What kind of support do you need?" and then these three options. Remember, use the escape character `\n` in strings for line breaks. Use `input()` in the same way as the previous function to record the users choice.
# 
# 1. If they select `1`, call the function `television_support()` which will we define later.
# 2. If they select `2`, call the function `internet_support()` which we will also define later.
# 3. If they select `3`, call the function `live_rep()` with the argument `"support"`. We'll use this argument to indicate what type of live representative the user will talk to. We will define the function later.
# 4. Finally, just like the `cs_service_bot()` function, if the user enters something other than the three options above, have the function print
#             Sorry, we didn't understand your selection.
# and call itself to let them try again.

# In[ ]:


def existing_customer():

    print("""What kind of support do you need?/n
          [1] Television Support/n
          [2] Internet Support/n
          [3] Speak to a support representative. """)
          
    response = int(input())
          
    if (response == 1):
          television_support()
    elif (response == 2):
          internet_support()
    elif (response == 3):
          live_rep("support")
    else:
          print("Sorry, we didn't understand your selection.")
          existing_customer()   
    
          


# ## Step 4
# You can see that we've introduced a whole new slew of functions as options of `existing_customers()`, and we'll define those soon but first let's define `new_customers()`.
# 
# The options the **DNS Cable Company** wants for `new_customers()` are 
#               
#               [1] Sign up for service.
#               [2] Schedule a home visit.
#               [3] Speak to a sales representative.
#               
# They also want this function to greet their potential new customers with the phrase "We're excited to have you join the DNS family, how can we help you?" A little cheesy if you ask me but hey, the client is always right.
# 
# 1. If the user selects `1`, call the function `sign_up()`.
# 2. If the user selects `2`, call the function `home_visit()`.
# 3. If the user selects `3`, call the function `live_rep()` with the argument `"sales"` so the program directs them to the correct live representative.
# 4. Finally, like the other functions, if the user sumbits something other than the options above, display an error message and call the function again.



def new_customer():
    print("""We're excited to have you join the DNS family, how can we help you?/n
        [1] Sign up for service./n
        [2] Schedule a home visit./n
        [3] Speak to a sales representative. """)
    
    response = int(input())
    
    if (response == 1):
        sign_up()
    elif (response == 2):
        home_visit()
    elif (response ==3 ):
        live_rep("sales")
    else:
        print("Sorry, we didn't understand your selection.")
          
        new_customer()


# ## Step 5
# 
# Now it's time to dive down another level and start defining the next level of functions. Let's start with `television_support()`. **DNS Cable Company** has compiled the three most frequently reported issues and wants those to be surfaced as options in the bot as follows after the prompt "What is the nature of your problem?":
# 
#             [1] I can't access certain channels.
#             [2] My picture is blurry.
#             [3] I keep losing service.
#             
# They also want a fourth catch-all option
# 
#             [4] Other issues.
#             

def television_support():
    print("""What is the nature of your problem?:/n
        [1] I can't access certain channels./n
        [2] My picture is blurry./n
        [3] I keep losing service./n
        [4] Other issues.""")
    
    response = int(input())
    
    if (response == 1):
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif (response == 2):
        print("Try adjusting the antenna above your television set.")
        did_that_help()
    elif(response == 3):
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif(response == 4):
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
          
        television_support()
        


# ## Step 6
# 
# Next, we will define `internet_support()`, which is will be extremely similar to the function you just defined, `television_support()` except with different possible support issues. Here are the issues that **DNS Cable Company** wants included:
# 
#                 [1] I can't connect to the internet.
#                 [2] My connection is very slow.
#                 [3] I can't access certain sites.
#                 
# Just like for television support, they also want a fourth option for `Other Issues`.
# 

def internet_support():
    print("""[1] I can't connect to the internet./n
            [2] My connection is very slow./n
            [3] I can't access certain sites./n
            [4] Other Issues.""")
    
    response = int(input())
    
    if (response == 1):
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif(response == 2):
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif(response == 3):
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif(response == 4):
        live_rep("support")
    else:
        print("Sorry, we didn't understand your selection.")
        internet_support()   
        
        
# The structure of the function should be as followed:
# 1. Ask the user if the solution solved their problem and have them answer Yes or No using `input()`.
# 2. If yes, thank them.
# 3. If no, prompt them with another question and ask them if they would rather talk to a live representative or schedule a home visit.
# 4. If they want to talk to a representative, call `live_rep("support")`
# 5. If they want to schedule a home visit, call `home_visit("support")`
# 6. Make sure to include error messages for both user responses if they enter a choice not listed above


def did_that_help():
    print("Did that fix your problem? (Y/N)")
    response = input()
    
    if (response == "Y"): 
        print("Thank you.  Have a great day")
    elif(response == "N"):
        print("""Would you like to talke to/n
              [1] Talk to a live representative/n
              [2] Schedule a home visit""")
        response_2 = int(input())
        
        if (response_2 == 1):
            live_rep("support")
        elif (response_2 == 2): 
            home_visit("support")
        else:
            print("Sorry, we didn't understand your selection.")
            did_that_help()       
 


# **DNS Cable Company** is very specific about the greeting they want new customers to see:
# 
#                 Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.
#                 [1] Bundle Deal (Internet + Cable)
#                 [2] Internet
#                 [3] Cable
#                 


def sign_up():
    print("""Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.
            [1] Bundle Deal (Internet + Cable)
            [2] Internet
            [3] Cable""")
    
    selection = int(input())
    
    if (selection == 1):
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
        
    elif (selection == 2):
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new_install")
        
    elif (selection == 3):
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new_install")
        
    else:
        print("Sorry, we didn't understand your selection.")
        sign_up()
        
        


# Now, `home_visit()` should first check `purpose` and then do one of the following:
# 1. If `purpose == "none"`, we need to determine the purpose of the home visit, so ask the user what the purpose of the home visit is and give them the options
#                 [1] New service installation.
#                 [2] Exisitng service repair.
#                 [3] Location scouting for unserviced region.
#     1. If they select `1` here, call `home_visit("new_install")`
#     2. If they select `2` here, call `home_visit("support")`
#     3. If they select `3` here, call `home_visit("scout")`
# 
# For all other options, first ask the user
#                 
#                 Please enter a date below when you are available for a technician to come to your home and [PURPOSE SPECIFC TEXT HERE].
# 

def home_visit(purpose = "none"):
    
    if (purpose == "none"):
        print("""What is the purpose of your home visit?
            [1] New service installation.
            [2] Exisitng service repair.
            [3] Location scouting for unserviced region.""")
        
        selection = int(input())
        
        if (selection == 1):
            home_visit("new_install")
        elif (selection == 2):
            home_visit("support")
        elif (selection == 3):
            home_visit("scout")
        else:
            print("Please enter a date below when you are available for a technician to come to your home and [PURPOSE SPECIFC TEXT HERE].")
            visit_date = input()
            
            print("Wonderful! A technical will come visit you on [visit_date]. Please be available between the hours of 1:00 am and 11:00 pm.")
            return visit_date
        
    
# Great work! We have one last function to define! `live_rep()` is called by several different functions, but it always called with one of two arguments, `"sales"` or `"support"`. All this function needs to do is print a message to the user based on the argument.
# 
# 1. If the function is called with an argument of `"sales"`, print 
#             Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.
# 2. If the function is called with an argument of `"support"`, print 
#             Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.


def live_rep(purpose):
    if (purpose == "sales"):
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    
    elif (purpose == "support"):
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")



# 1. This function should start by printing:
#             Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?
#             [1] New Customer
#             [2] Existing Customer
#    You can store this all in a single string and use the escape character `\n` to indicate line breaks.
# 


def cs_service_bot():
    # Replace `pass` with your code
    print("""Hello! Welcome to the DNS Cable Company's Service Portal. Are you a new or existing customer?/n
          [1] New Customer/n
          [2] Existing Customer""")
    
    response = int(input("Please enter the number corresponding to your choice: "))
    
    if (response == 1):
        return new_customer()
    elif (response == 2):
        return existing_customer()
    else:
        return cs_service_bot()   	


cs_service_bot()

