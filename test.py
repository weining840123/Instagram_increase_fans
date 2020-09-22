from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


chromedriver_path = '/Users/aaron/instagramBuffer/chromedriver' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('thecat_calledsanta')
password = webdriver.find_element_by_name('password')
password.send_keys('aaron840123zxopzxopzx')

# login
button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button > div')
button_login.click()
sleep(3)

# ignore the save info button
button_save_info = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
if button_save_info:
	button_save_info.click()
sleep(3)

# ignore the open notification button
button_open_notification = webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
if button_open_notification:
	button_open_notification.click()
sleep(3)
print("login success!!!")

# notnow = webdriver.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications


# the hashtag you focus on
hashtag_list = ['catsofinstagram', 'cat', 'catstagram', 'cats', 'instacat', 'catlover']

prev_user_list = [] # if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
# prev_user_list = list(prev_user_list['0'])

new_followed = []
# tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    # tag += 1
    # webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag + '/')
    sleep(5)
    
    post = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    post.click()
    sleep(2)
    # break
    
    try:
    	for _ in range(10):
	    	username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/div/a').text
	    	print(username)
	    	if username not in prev_user_list:
	    		if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == '追蹤':
	    			webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
	    			print("Follow people!!!")
	    			followed += 1 
	    			new_followed.append(username)

	    		
	    		try:
	    			# Like the post
	    			post_like_buttom = webdriver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg[aria-label='讚']")
	    			post_like_buttom.click()
	    			likes += 1


	    			# Comment the post
		    		r = randint(0, 4)
		    		webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]").click()
		    		comment_area = webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")
		    		if r == 0:
		    			comment_area.send_keys("Adorable cat!!")
		    			sleep(2)
		    		elif r == 1:
		    			comment_area.send_keys("So cute! You can see may cat in my page. Floolw for follow!!")
		    			sleep(2)
		    		elif r == 2:
		    			comment_area.send_keys("Cats are the best pet. No doubt.")
		    			sleep(2)
		    		elif r == 3:
		    			comment_area.send_keys("Wow, my cat looks similar to yours. Follow for follow!!")
		    			sleep(2)
		    		else:
		    			comment_area.send_keys("Nice pic. Like for like!!")
		    			sleep(2)
		    		comment_area.send_keys(Keys.ENTER)
		    		comments += 1
	    		except:
	    			print("Already like the post!!!!!")

	    		# go to next post
	    		next_button = webdriver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[position()=last()]")
	    		next_button.click()
	    		sleep(randint(10, 20))

    except:
    	continue


    # for _ in range(20):
    # 	username = webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/a').text
    # 	# print(username)
    # 	if username not in prev_user_list:
    # 		if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == '追蹤':
    # 			webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
    # 			print("Follow people!!!")
    # 			followed += 1 
    # 			new_followed.append(username)

    		
    # 		try:
    # 			# Like the post
    # 			post_like_buttom = webdriver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > svg[aria-label='讚']")
    # 			post_like_buttom.click()
    # 			likes += 1


    # 			# Comment the post
	   #  		r = randint(0, 4)
	   #  		webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[2]").click()
	   #  		comment_area = webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea")
	   #  		if r == 0:
	   #  			comment_area.send_keys("Adorable cat!!")
	   #  			sleep(2)
	   #  		elif r == 1:
	   #  			comment_area.send_keys("So cute! You can see may cat in my page. Floolw for follow!!")
	   #  			sleep(2)
	   #  		elif r == 2:
	   #  			comment_area.send_keys("Cats are the best pet. No doubt.")
	   #  			sleep(2)
	   #  		elif r == 3:
	   #  			comment_area.send_keys("Wow, my cat looks similar to yours. Follow for follow!!")
	   #  			sleep(2)
	   #  		else:
	   #  			comment_area.send_keys("Nice pic. Like for like!!")
	   #  			sleep(2)
	   #  		comment_area.send_keys(Keys.ENTER)
	   #  		comments += 1
    # 		except:
    # 			print("Already like the post!!!!!")

    	

    # 	# go to next post 
    # 	next_button = webdriver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[position()=last()]")
    # 	next_button.click()
    # 	sleep(randint(10, 20))
	

"""
    															
    try:        
        for x in range(1,200):
            username = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
            print(username)

            
            if username not in prev_user_list:
                # If we already follow, do not unfollow
                if webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    
                    webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                    
                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                    
                    button_like.click()
                    likes += 1
                    sleep(randint(18,25))

                    # Comments and tracker
                    comm_prob = randint(1,10)
                    print('{}_{}: {}'.format(hashtag, x,comm_prob))
                    if comm_prob > 7:
                        comments += 1
                        webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()
                        comment_box = webdriver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[3]/div/form/textarea')
																		
                        if (comm_prob < 7):
                            comment_box.send_keys('Really cool!')
                            sleep(1)
                        elif (comm_prob > 6) and (comm_prob < 9):
                            comment_box.send_keys('Nice work :)')
                            sleep(1)
                        elif comm_prob == 9:
                            comment_box.send_keys('Nice gallery!!')
                            sleep(1)
                        elif comm_prob == 10:
                            comment_box.send_keys('So cool! :)')
                            sleep(1)
                        # Enter to post comment
                        comment_box.send_keys(Keys.ENTER)
                        sleep(randint(22,28))

                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(25,29))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(20,26))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
"""

