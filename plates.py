import socket
import re
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",1234))
s.sendall('"plates"\n')
recv = ""
while "\n" not in recv:
	recv = recv + s.recv(4096)
recv = recv.lower()
recv = recv.strip()

word_file = open("wordlist.dat","r")
global WORDS_WITH_SCORE
WORDS_WITH_SCORE = []



def submit_answer():
	global WORDS_WITH_SCORE
	for words, score in WORDS_WITH_SCORE:
		if score == 4:
			return words
	for words, score in WORDS_WITH_SCORE:
		if score == 3:
			return words
	for words, score in WORDS_WITH_SCORE:
		if score == 2:
			return words
	for words, score in WORDS_WITH_SCORE:
		if score == 1:
			return words
			


def capitalize_letter(word,n): #capitalizes nth letter
	if len(word)-1 == n:
		return word[:n] + word[n].upper()
	elif n == 0:
		return word[0].upper()+word[1:]
	else:
		return word[:n] + word[n].upper() + word[(n+1):]


def score_word(word,pattern):
	letter1 = [a.start() for a in re.finditer(pattern[1],word)]
	letter2 = [a.start() for a in re.finditer(pattern[2],word)]
	letter3 = [a.start() for a in re.finditer(pattern[3],word)]
	all_combo_of_letters = []
	for a in letter1:
		for b in letter2:
			for c in letter3:
				all_combo_of_letters.append([a,b,c])


	
	for combo in all_combo_of_letters:
		
		global WORDS_WITH_SCORE
		if a>b or a>c or b>c or a == b or b == c or a == c:
			continue

		score = 0
		if a > 0:
			score += 1
		if b - a > 1:
			score += 1
		if c - b > 1:
			score += 1
		if c + 1 < len(word):
			score += 1
		capitalized_word = capitalize_letter(word,a)
		capitalized_word = capitalize_letter(capitalized_word,b)
		capitalized_word = capitalize_letter(capitalized_word,c)
		WORDS_WITH_SCORE.append([capitalized_word, score])
		if score == 4:
			print capitalized_word

for word in word_file:
	word = word.strip()
	if re.search(recv[1]+"*"+recv[2]+"*"+recv[3],word):
		score_word(word,recv)
	
	
answer = submit_answer()
print answer
s.sendall('"%s"\n'%(answer))

print "SUBMITTED ANSWER: %s"%(answer)
recv = s.recv(4096)
print "MESSAGE RECEIVED: %s"%(recv)