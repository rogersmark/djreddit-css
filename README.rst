djreddit-css
=====================

This package is a Django application that exists to make moderating sub-reddits at Reddit just a teensy bit easier. A lot of subreddits tend to use custom CSS. The problem is that this is usually managed via threads that have to be constantly maintained and checked, or via one-off applications that can't be shared. The purpose of this is to allow for an application that can be shared by Redditors. 

Usage
=====================

Go to the administration panel and you can create "SubReddits". This is because with this application you can manage multiple subreddits form one instance. After you've created that, you can create "Groupings". In /r/mls, we group users by MLS teams, and put their crests next to their name in posts. Finally, you have users, which is the name of the users to put inside a grouping. This'll all be used to create custom displays of the CSS for a specific subreddit. Users will be able to fill our a simple form, and you can come and copy and paste the CSS into your subreddit whenever you'd like, knowing that you got everyone taken care of.

Future Changes
=====================

I'd like to eventually make the CSS update automatic, and do more to compress the CSS as well.