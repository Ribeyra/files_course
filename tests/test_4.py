from files_course.step_4_a import transform


rules1 = {
    'word_min_len': 3,
    'censored_words': ['language', 'show'],
    'capital_letters': ['l', 'a'],
}
res = 'The Python was not named After Long snake but After the British comedy\
 Monty Python Flying Circus\n'

transform('files/step_4_1_in.txt', 'files/step_4_1_out.txt', rules=rules1)
if str(open('files/step_4_1_out.txt').read()) != res:
    raise Exception('fail1')

rules2 = {
    'word_min_len': 5,
    'censored_words': ['explain', 'implementation'],
    'capital_letters': ['s', 'p'],
}
res2 = '''Beautiful better
Explicit better implicit
Simple better complex
Complex better complicated
Readability counts
Special cases aren't Special enough break rules
Although Practicality beats Purity
Errors Should never Silently
Unless explicitly Silenced
ambiguity refuse temptation guess
There Should Preferably obvious
Although obvious first unless you're Dutch
better never
Although never often better right
Namespaces honking great let's those
'''
transform('files/step_4_2_in.txt', 'files/step_4_2_out.txt', rules=rules2)
if str(open('files/step_4_2_out.txt').read()) != res2:
    raise Exception('fail2')

print('pass')
