# A First Class Example
class Song(object):

    def __init__(self, lyrics):
        # ? self.variable = value
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # * access lyrics by self.lyrics
        for line in self.lyrics:

            print(line)  # prints


#! song_name = class([lyrics]) -> in array to pass multiple lines as list
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()
# ? accessing the sing_me_a_song in class Song

bulls_on_parade.sing_me_a_song()
