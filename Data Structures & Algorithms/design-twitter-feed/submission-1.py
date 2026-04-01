class Twitter:

    def __init__(self):
        # To store tweets as (timestamp, tweetId)
        self.tweets = defaultdict(deque)  # Dictionary mapping userId -> deque of (timestamp, tweetId)
        # To store follow relationships as a set
        self.following = defaultdict(set)  # Dictionary mapping userId -> set of followeeIds
        # A global timestamp to order tweets
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet to the user's tweet deque with current timestamp
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Create a min-heap to keep track of the top 10 most recent tweets
        min_heap = []
        
        # Add the user's own tweets
        if userId in self.tweets:
            for tweet in list(self.tweets[userId])[:10]:
                heapq.heappush(min_heap, tweet)
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        
        # Add tweets from people the user is following
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                for tweet in list(self.tweets[followeeId])[:10]:
                    heapq.heappush(min_heap, tweet)
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)

        # Extract the tweets in reverse order (most recent first)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])

        return result[::-1]  # Return the most recent tweets first

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)