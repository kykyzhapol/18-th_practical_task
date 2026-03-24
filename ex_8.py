from solution import MorseMsg

msgs = []
msgs.append(MorseMsg('.. .-.. .. -.- . .--. -.-- - .... --- -.'))
msgs.append(MorseMsg('-- --- .-.- .--. .-. --- --. .-. .- -- -- .-'))
for msg in msgs:
    print(msg)
print(msgs[0].eng_decode())
print(msgs[0].get_vowels('eng'))
print(msgs[0].get_consonants('eng'))
print(msgs[1].ru_decode())
print(msgs[1].get_vowels('ru'))
print(msgs[1].get_consonants('ru'))
