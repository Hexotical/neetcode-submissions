class Twitter:

    def __init__(self):
        #Post tweets, follow unfollow, view ten most recent tweets
        self.followerList = defaultdict(set)
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        to_ret = []
        for i in range(len(self.tweets)-1, -1, -1):
            if len(to_ret )> 9:
                break
            #print(self.tweets[i])
            if self.tweets[i][0] == userId or self.tweets[i][0] in self.followerList[userId]:
                to_ret.append(self.tweets[i][1])

        return to_ret
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerList[followerId]:
            self.followerList[followerId].remove(followeeId)
