import defnition as de


f = open('turtle.txt', 'r')
string_modify = de.STRING_MODIFY()
f_data = string_modify.remove_punctuation(f.read())
list = string_modify.remove_newline(f_data)
print(de.word_count(list))
