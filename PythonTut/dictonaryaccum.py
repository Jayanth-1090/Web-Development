# f=open("scarlet.txt","r")
# txt = f.read()
# t_count = 0
# s_count = 0
# for c in txt:
#     if c == 't':
#         t_count+=1
#     elif c == 's':
#         s_count+=1
# print("t: "+str(t_count)+ " occurances")
# print("s: "+str(s_count)+ " occurances")

# f=open("scarlet.txt","r")
# txt = f.read()
# x={}
# x['t']=0
# x['s']=0
# for c in txt:
#     if c == 't':
#         x[c]+=1 #x['t']+=1 or x[c]+=1 #another way is not to hardcode value
#     elif c == 's':
#         x[c]+=1 #x['s']+=1 #here x and t are hardcoded 
# print("t: "+str(x['t'])+ " occurances")
# print("s: "+str(x['s'])+ " occurances")


f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

# Write a loop that prints the letters and their counts
for c in letter_counts.keys():
    print(c + ": " + str(letter_counts[c]) + " occurrences")



#to count each word occurance and make a list

sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
    
word_counts = {}

for word in sentence.split():
   word_counts[word] = word_counts.get(word, 0) + 1