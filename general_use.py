import twitter

# copy your keys here, 
api = twitter.Api(consumer_key="yourKeyHere",  # called 'api key' on twitter site
                  consumer_secret="yourKeyHere", 
                  access_token_key="yourKeyHere",
                  access_token_secret="yourKeyHere",
                  sleep_on_rate_limit=True # respect rate limits)
                  )

# list of follows you want to keep 
l = ['your', 'friends', 'here']


##########
# SCRIPT #
##########

# list of friends as twitter objs
v = api.GetFriends()

# list of @ handles 
scrnms = [u.screen_name for u in v]

def dele():
	exceptions = []

	for i,c in enumerate(scrnms):
		try:
			if c not in l:
				api.DestroyFriendship(screen_name=c)
		except twitter.error.TwitterError as twt:
			if twt.message[0]['code'] != 34:
				exceptions.append({c:twt})
		finally:
			print(i,"/",len(scrnms))

	if exceptions:
		print('Exceptions: ',exceptions)
		with open('exceptions.txt', 'w') as f_obj:
			f_obj.write(exceptions)


if __name__=="__main__":
	dele()