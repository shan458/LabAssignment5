""""
The program is trying to translate a sentence captured as user input. 
We first read in the text file textese.txt.
Then from the text file, we create a list of strings from each lines in the text file. 
Then, we create a dictionary the lists. 
Once the text file has been read into memory, we close the file. 

We then define a fuction for translating which envolves splitting the user input (sentence) into an 
array or strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

Once we have the array of strings representing the user's input sentence, we
loop through each words, find the key matching the word and returns back the value tied to that word

After each word is translated, we then
print out the translated sentence to the user. 
"""

"""
main():
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):
    words = for each of the word in the sentence
    for each words, translate the word
    print translated sentence to user

create_dictionary():
    read in textese.txt
    create list = each line from file
    close the file 
    create a dict off of the list
    return the dict

main()
"""