# https://leetcode.com/problems/design-twitter/
from collections import deque
from typing import List


class Twitter:
    def __init__(self):
        self.newsfeed = deque([])
        self.followmap = {}
        self.topkfeed = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.newsfeed.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.followmap:
            return [
                feed[1]
                for feed in self.newsfeed
                if feed[0] in [userId] + self.followmap[userId]
            ][: self.topkfeed]
        else:  # if user id still not followmap this means he still has no followers , so its key not present in followmap
            return [feed[1] for feed in self.newsfeed if feed[0] == userId][
                : self.topkfeed
            ]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            self.followmap[followerId] = [followeeId]
        else:
            self.followmap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followmap:
            return
        elif (
            followerId in self.followmap
            and followeeId not in self.followmap[followerId]
        ):
            return
        self.followmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
twitter = Twitter()
twitter.postTweet(1, 5)
print(twitter.getNewsFeed(1))
twitter.follow(1, 2)
print(twitter.postTweet(2, 6))
print(twitter.getNewsFeed(1))
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))

twitter = Twitter()
twitter.postTweet(1, 1)
print(twitter.getNewsFeed(1))
twitter.follow(2, 1)
print(twitter.getNewsFeed(2))
twitter.unfollow(2, 1)
print(twitter.getNewsFeed(2))
