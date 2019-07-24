
#Problem 4 - Decrypt a Story
#5.0/5.0得分 (计入成绩)
#For this problem, the graders will use our implementation of the Message, PlaintextMessage, and CiphertextMessage classes, so don't worry if you did not get the previous parts correct.

#Now that you have all the pieces to the puzzle, please use them to decode the file story.txt. The file ps6.py contains a helper function get_story_string() that returns the encrypted version of the story as a string. Create a CiphertextMessage object using the story string and use decrypt_message to return the appropriate shift value and unencrypted story string.

#Paste your function decrypt_story() in the box below.

def decrypt_story():
    decrypt_story = get_story_string()
    story = CiphertextMessage(decrypt_story)
    return story.decrypt_message()
