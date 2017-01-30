verses = []
song = []

# Allows the user to enter any number of verses 
print "How many verses does your song have? ",
verseCount = int(raw_input())
for x in xrange(verseCount):
    print "What is your next verse?",
    verses = verses + [raw_input()]

# Modifies the chorus to have the requested repeat
print "Enter the chorus: ",
chorus = raw_input() + " "
print "Enter the chorus repeat", 
chorus = chorus * int(raw_input())
chorus = chorus.strip()

# Builds the song
for verse in verses:
    song = song + [verse, chorus]
song = song + [".... One more time! ...."] + song

print song
for line in song: 
    print line
