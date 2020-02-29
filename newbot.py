import tweepy
import time

ck = 'yf5BA2XdX6IRysoMf4JT1welF'
csk = 'Y4zSqu6Pv3mOQi1dPBL4Ag2PZZBo34BcFEcRwNFP8BXG1KtedB'
at = '1136894887511461888-nIUzHKF193lg0O75m89aNoyRh0FhNG'
atc = '2XA2HkyhqTBbhBw07t5Lplj6778lzIf0hzw78fDb2jwlg'

auth = tweepy.OAuthHandler(ck,csk)
auth.set_access_token(at,atc)
api = tweepy.API(auth)

user = api.me()
print(user.name)

#get tweet using id
#status = api.get_status('770189549976690688')
#print(status.text)

#--------------------------------------------------------------------------------




#--------------------------------------------------------------------------------
def find_user(str): #finds if user exists or not
    try: 
        x=api.get_user(str)
        if x:
            print("yes, the user exists")
    except Exception:
        print("no,the user doesn't exist")

        
        
#find_user('cndnsjkncjskncj') #call here  #input garera pani username lida hunxa
#--------------------------------------------------------------------------------









#--------------------------------------------------------------------------------
def is_following(first_name, second_name): #checks if follows or not
    check = api.show_friendship(source_screen_name=first_name, target_screen_name =second_name)
    flw=check[0].following, check[1].following
    if flw == (True,False):
        print(first_name +" is following "+ second_name, second_name +" is not following "+ first_name)
        
    if flw == (False,True):
        print(first_name +" is not following "+ second_name, second_name +" is  following "+ first_name)
    
    if flw == (True,True):
        print(first_name +" is following "+ second_name, second_name +" is following "+ first_name)
        
    if flw == (False,False):
        print(first_name +" is not following "+ second_name, second_name +" is not following "+ first_name)
        
    
    
#is_following('Cristiano','cacklerraj') #call here       
#--------------------------------------------------------------------------------     






#--------------------------------------------------------------------------------
def follow (his_name):  #jaslai follow garne ho
    try:
        friend=api.create_friendship(his_name,follow)
        if friend:
            print("followed" + his_name)
            
    except tweepy.error.TweepError:
        print("enter valid username")
    
    


#follow('dndjjncjksdnjkshfus') #call here
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
def un_follow(his_name): #jaslai unfollow garne ho
    try:
        friend=api.destroy_friendship(his_name)
        if friend:
            print("unfollowed " + his_name)
            
    except tweepy.error.TweepError:
        print("enter valid username")
    
    

#un_follow('dndjjjcbsdhcjsbhcsb n') #call here
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
def count(f): #counts the no of followers
    number=api.get_user(f).followers_count
    #print(number)
    return number

#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
def mass_unfollow(): #as the name suggests
    followers = api.followers_ids('kaushal_023') #mero followers
    friends = api.friends_ids('kaushal_023') # maile follow gareko
    for f in friends:
        if(count(f)<200): # custom function
            if f not in followers:
                #print(f)
                
                un_follow(f'{f}') #custom function
                time.sleep(2)


#mass_unfollow() #call here
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
def change_dp(photo):
    dp_changed=api.update_profile_image(photo)
    if dp_changed:
        print("display pic updated")

#change_dp('torres.jpg') #call here
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
def change_cp(photo):
    cp_changed=api.update_profile_background_image(photo)
    if cp_changed:
        print("display pic updated")

#change_cp('torres.jpg') #call here
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
#input use garera garda ni hunxa
your_name ='Kaushal'
p_url = ""
p_location ="Jhapa,Nepal"
p_bio="Hello, welcome to my profile"

def update_profile(your_name,p_url,p_location,p_bio):
    p_updated = api.update_profile(your_name,p_url,p_location,p_bio)
    if p_updated:
        print("profile updated")
    

#update_profile(your_name,p_url,p_location,p_bio) call here

#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------

def re_tweet():
    try:
        rt = api.retweet(770189549976690688)
        if rt:
            print("retweeted")
            
    except tweepy.error.TweepError:
        print("maybe already done or tweet not found")

#re_tweet() #call here


def unre_tweet():
    try:
        un_rt = api.unretweet(770189549976690688)
        if un_rt:
            print("un retweeted")
            
    except tweepy.error.TweepError:
        print("maybe already done or tweet not found")

        
#unre_tweet() #call here



def write_tweet(tweet):
    try:
        twt = api.update_status(tweet)
        if twt:
            print("tweeted")
    except Exception:
        print("dont post same tweet")

#write_tweet("hey I am Kaushal's bot.")

def tweet_with_photo(photo,tweet):
    try:
        ph_twt = api.update_with_media(photo,tweet)
        if ph_twt:
            print("tweeted with picture")
    except Exception:
        print('file not found')
tweet_with_photo('tores.jpg', 'can you believe it?? Torres scored the goal.')        
#--------------------------------------------------------------------------------



#--------------------------------------------------------------------------------
#this doesn't work as sending message isn't allowed
message = "Hello myself"

def send_dm(his_name,message):
    quick_reply_type= ""
    attachment_type=""
    attachment_media_id=""
    m_sent = api.send_direct_message(his_name,message,quick_reply_type,attachment_type,attachment_media_id)
    if m_sent:
        print("message sent to"+ his_name)

#send_dm('752324414750928896',message) #can use username too
#------------------------------------------------------------------------------------

                        #ROUGH AREA

#--------------------------------------------------------------------------------
"""
followers = api.followers_ids('kaushal_023') #mero followers
friends = api.friends_ids('kaushal_023') # maile follow gareko
#print(followers)
#print(friends)
#api.show_friendship(source_screen_name="kaushal_023", target_screen_name ="googledevs")


def count(f): #counts the no of followers
    number=api.get_user(f).followers_count
    #print(number)
    return number

for f in friends:
    if(count(f)>10000):
        if f not in followers:
            print(f)
            #api.destroy_friendship(f)
            #time.sleep(2)

        
 """       

       