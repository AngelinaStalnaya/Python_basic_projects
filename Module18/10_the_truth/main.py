text = 'vujgvmCfb tj ufscfu ouib z/vhm' \
       ' jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm' \
       ' yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ ' \
       'bstfTq jt uufscf uibo otf/ef ' \
       'uzSfbebcjmj vout/dp ' \
       'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf' \
       ' ipvhiBmu zqsbdujdbmju fbutc uz/qvsj' \
       ' Fsspst tipvme wfsof qbtt foumz/tjm ' \
       'omfttV mjdjumzfyq odfe/tjmf ' \
       'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
       'xOp tj scfuuf ibou /ofwfs' \
       ' uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op' \
       ' gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb' \
       ' Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
alphabeth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
encrypt_text = ''
final_text = ''
index_d = 0
new_word = ''


for sym in text:
    if sym == ' ':
        encrypt_text += sym
    if sym == '/':
        encrypt_text += '.'
    if sym in alphabeth:
        encrypt_text += alphabeth[alphabeth.index(sym) - 1]
    if sym == '.':
        encrypt_text += '-'
    if sym == '(':
        encrypt_text += "'"
    if sym == '"':
        encrypt_text += '!'
    if sym == '-':
        encrypt_text += '-'
new_text = encrypt_text.split()

word = new_text[0]
while not word.istitle():
    word = word[-1:] + word[:-1]
    index_d += 1

for word in new_text:
    new_word = ''
    for i in range(len(word)):
        new_word += word[i - index_d % len(word)]
        if new_word.endswith('.'):
            index_d += 1
        else:
            continue
    if new_word.istitle():
        final_text += '\n' + new_word + ' '
    else:
        final_text += new_word + ' '

print(final_text)
