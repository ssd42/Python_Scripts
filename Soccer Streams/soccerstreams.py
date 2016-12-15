import praw
import re
import webbrowser

# Why even try sometimes 
r = praw.Reddit(user_agent="Archiving_links")

# This regex has the right paren flaw try again later
email_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

# urls = re.findall(email_regex, search_string)


# I like the class mostly since script is mostly written as a library
# That can be used in other subreddits
class getStreams:
    def __init__(self, subreddit = "soccerstreams"):
        self.subreddit = subreddit
        self.posts = []
        self.comments = []

    def get_games(self):
        sub = r.get_subreddit(self.subreddit)
        self.posts = [submission.title for submission in sub.get_hot(limit=15)]

    def get_comments(self, team_name):
        # Post will be of a generator type
        sub = r.get_subreddit(self.subreddit)
        team = team_name.lower()
        comments_link = []

        for submission in sub.get_hot(limit=15):
            if team in submission.title.lower():

                comments = submission.comments

                iterator = 1
                for comment in comments[:10]: # Get first 10 comments (mod comment isnt always gurarenteed)
                    print(str(iterator) + ':  ' + comment.body + '\n')
                    comments_link.append(comment.body)

                    iterator+=1

        ans = input('What comment will you like to check(choose by number): ')

        while ans != 'quit':

            urls = re.findall(email_regex, comments_link[int(ans) - 1])
            # Deal with the ')'
            # yeah this works less readable(is this even english?) but cleaner than before
            clean_urls = [url[:-1] if url[-1:] is ')' else url for url in urls]

            # has to be a way with string comprehension to deal with this below... i know i know
            # done
            [print(str(count) + ':  ' + url + '\n') for count, url in enumerate(clean_urls, len(clean_urls))]

            try:
                new_ans = input("Which link (choose number): ")
                # "-1" cause 1 to n-1 looks better to average user than 0 to n
                webbrowser.open_new_tab(clean_urls[int(new_ans)-1])
            except Exception as e:
                print(e)

            ans = input('Next url number ( or \'quit\' to leave): ')


def main():
    streams = getStreams()
    streams.get_games()

    print('AVAILABLE STREAMS ARE: \n\n')
    [print(stream) for stream in streams.posts]

    team = input('\nWhich team will you want to watch?\n::>')
    streams.get_comments(team)

if __name__ == '__main__':
    main()
