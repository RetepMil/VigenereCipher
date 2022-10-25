from collections import deque, defaultdict
from itertools import product
import pprint
pp = pprint.PrettyPrinter(compact=True)

# 키 값에 따른 빠른 encryption을 위한 dictionary 초기화
key_strings = '''00 DTYLUKCNOIVSEPFQJWRGMBZAXH
01 LOGKWPRMDUVSYFJNTQIHEAZCBX
02 YGSKCJETRMUWNHQXIZFAOVBLDP
03 BERHJYKWCSLNPDZIGFUAOXVQTM
04 JLSGAOPZEMBVQCUIYDTHXRWFKN
05 IPWSURJTOQGEVDBMYKLNHAXZFC
06 CGLXSIBTJHOKNDMQPVRZAYEFUW
07 YGHKDVLQEXUOASZWPJFBCNRITM
08 ACZLSOGEDPYWFXHBVIMUKNTJQR
09 XTHNIBAFEUQSGLJDWOZKMPVCYR
10 MFKGNURPJZTBQWLCASIHVYOXDE
11 NHTEPCFDXRYZBAIMSGVJKUOQWL
12 AHFPGVUKLMNCTSRDEIWZXYQBOJ
13 SAHIKWDQJNPVUTZCBYLOGFMREX
14 GPNWMTOSQHJVYKFEALXCIRDBZU
15 GPCWQOSVZKINJHERUABDTMXLFY
16 NKAELXYVRDOGZIMTFUBSPJQHWC
17 EFTXLBCAWHUJGVOMYRSNKDQIZP
18 ZLNRQBAVYMJUDOTSHXCWGPKIEF
19 YAGDUTFIXMBWLOJQVNERHKSZPC
20 THRAWJEMNFKYZCIGOBXVSULDQP
21 INESDOMTPBQGHYFUZCRVWLKJXA
22 YIRAELHQOSXGCWTPJVZUNFMDKB
23 ITLFAXYCMOPVGZHURDBWNSJQKE
24 QRJGEFWVLKSUHPCXYBMOITNZAD
25 VYGNODPUJEMFCZIXASKBWHRTLQ
26 ANZIFPCLOKMHSJDEWVBYQXTURG
27 NEBZCRMKDPATGLSOWHFIJQVUYX
28 EQJTZFYSINAUBWCVDXRKHPLGMO
29 KDOTRBZWIAUYPLNHEGFQSJMCXV
30 XVSRDIUZFCQTMPLHYEGJAKNWOB
31 MVELIBQAFGJNPCKWXUSTZRDYHO
32 BMOITNEWDAUVPHZJXYSLRQCFGK
33 UYWVFPNHDCRSMZQGXOBTEKLAIJ
34 LBTNMCYODQIKHSFUJEVARPXWGZ
35 NFGUQPSTMCKOXJVWELIABRHYZD
36 CWMFKHPLOVIQXDARBUTEGZJSNY
37 ITOPAJWHEDZKMCVUXBYQSNLRGF
38 EODXLUVTSYHMFGAJNWPZQBCIKR
39 HZACTFNPIXMQRDUBYKVJOGWLES
40 KYFAZHCLPNQGXWDTVBORUJIMSE
41 NSWZTGXHKVBPCORLYQEAIJDFUM
42 XSYLMPKQIZWEANTOVHRDBFUCGJ
43 XYISKJVQMTRCAUNGZEOHFWLBDP
44 KDMEPYHGQZTSUVJFXOILRANBWC
45 GEVKJRNFBXWQPHDOAMTLIZYUCS
46 MZEKBDFIGQTLJPOWUXSHCRNYVA
47 AZLETRUFIPJHBXKOSYQMNGDCVW
48 KNEOJVXFQWCHTDGUMZLYSRAIPB
49 UIROVSWAGEQXTHZCFYLBDJPKMN
50 XBDQIFRUVENLHOAZPWGMKJTCSY
51 BPJZGEVCNTMAOIKHDWSRFUXQLY
52 CXEDARNFZGLSPWKQHTVIUBMOJY
53 IZMLCRNWAKTBUHJSPFOEGYQXDV
54 JOBCRSIAHGZKNYQLDFEPVXWMUT
55 WPCKJMQTZIELARUBSOXFVYHDNG
56 KHVUDGMOJWPYRFSQBLZACITNXE
57 VFIZLTQPMKRACDSOGJXEUNBWYH
58 GFYVTDQLHWJPKMBAZNIUOSCXER
59 QKMSFAZBVPHGWIODEXUCNYJLTR
60 IAPDHNYVFCMOERLUJTQBWSZXKG
61 ARZOWSMPBKJLVDGUIYNXFHCETQ
62 DHOXKZWVTCPBRMGIQALYJFUNES
63 TJFPRHKUWQOMXNIBLYVDZEAGSC
64 ACBZGTPNSJYDVLXRHOWKUEFMQI
65 FPHEOKUXNQMZWIVRTCSGBDLJAY
66 DJABIUXEYQOKRZNSLMPGCTVHFW
67 AIHDGCNLPQOVTKMJFSRZEBUYXW
68 JKULTOCZYWNDBIXHQMPSFGEARV
69 BZJTGQCFKWRPODNLYMSEVHIUAX
70 CQDBVGIZRNJKFLUXAWYTESPMOH
71 TADSIQMURKNHYVXCELWOPZGFJB
72 VSYUFWHJKOBNTIEDRXMLACZPGQ
73 ILCBVHDKSURWXJNFAEYOPQMGZT
74 WHVQOLDZPURMGEXTSFYBAICJKN
75 EZKTAMWIYJQXPLOVBCHNGUDFRS
76 VCLSBQWEDKGTYIFXHARMZUNPJO
77 FYAJDGSOVPRCHQWUNITEBKZLMX
78 BXQWVTCEURIZKAGPNLODFJHMYS
79 MJPKITCUYZSXBOGLADEWVFQNHR
80 IZEXRFDHAGSQNPTVBMLWKOUJCY
81 CTPONKGRMUJWQEYXZVALHIDBFS
82 HVFBTXSJLNAYPZUQOMRGWICKED
83 UCSBJDZOTEIQHARVYNWLPMGKFX
84 LUJHAXCWIRPMVDQNTGBZEFYOKS
85 AHUKMVEPFNBXYCTORQDSIWZGJL
86 XWLNYZGIAKJSURDHMQCETFVPBO
87 VSIJNAXHZLPOQYGRDKMUWFBETC
88 EMWOFAKYTNQZGXJPLVBRCIUDSH
89 RSLIHTMPNJXGOCKDUQFAZYWVBE
90 XCJIGNOKFEHMTADBYWPLSZRUQV
91 AJCKXTMLDWHEZBNYORUIVGPSQF
92 RZEWMCBXITNQLYADSOVGFUPHKJ
93 JMSOVGIPCLYUNDRTFEWQBHXKZA
94 FYCRPOJNHLSKVUBIDMXAEQZTGW
95 UXZRBFIQNYLWDKCHSJTPAVEGMO
96 SRJTMXUZBWGFYDKEVOPAHILQCN
97 QOHEWVDSTAKJIBNXPGCLRYMZFU
98 OKSGRZYCDEWVJPAHXFLIMUNBTQ
99 ULDOMNSRCYGVBPXQWAZJFKEITH'''
key_dict = {}
for key in key_strings.split('\n'):
    key, key_string = key.split(' ')
    
    temp_dict = defaultdict(list)
    for i in range(26):
        key_string_deque = deque(list(key_string))
        key_string_deque.rotate(-i)
        for j in range(26):
            temp_dict[key_string[i]].append(key_string_deque[j])
    
    key_dict[key] = temp_dict

pp.pprint(key_dict['00'])

# encryption test
a = 'CRYPTO'
keys = ['66', '11', '52', '55', '04', '90']
offset = 11
ciphertext = ''
for plain_char, key in zip(a, keys):
    ciphertext += key_dict[key][plain_char][offset]
print(ciphertext)

plaintext  = 'THISCIPHERWASWIDELYUSEDBECAUSEOFSIMPLESTR'
ciphertext = 'OYKWUXRNJOOPPTXCTYNYQHFCQNIIWNKPAZQSTIFHOOWEYEHDQQYZMFQDHGZWUQIEZOUJNCEHDQQERBNJKRMRGLWIXVLVPFOBLLAVOPZENPADJPKVMMMPDYXJCBWEX'

'''
First determine length of k using sliding window
n이 1 부터 25까지 모든 offset 값을 하나씩 고려하면서, 각 n 자리마다 모두 치환가능한 key 후보군들이 전부 존재한다면 key의 길이를 구할 수 있다.
예를 들어 n이 4이면 4마다 등장하는 char에 대한 key_string은 동일해야 함:
plaintext에서 T...C...E..........E의 T, C, E는 모두 동일한 key_string을 사용해서 encryption됨

T C E ...
H I R ...
I P W ...
S H A ...

에서
T -> O, C -> U, E -> J,...에 해당하는 key_string과 offset의 pair가 존재함
'''


'''
Looking at the plaintext, from heuristic 'STR' should be 'STRUCTURE', so adding UCTURE at the end and go through the process again:
'''
plaintext  = 'THISCIPHERWASWIDELYUSEDBECAUSEOFSIMPLESTRUCTURE'

combinations = {}
for n in range(1, 26):
    # groups에 residue of n 자리의 모든 문자를 하나의 그룹으로 묶어 놓는다
    groups = []
    for i in range(n):
        group = []
        cnt = i
        while cnt < len(plaintext) - 1:
            group.append((plaintext[cnt], ciphertext[cnt]))
            cnt += n
        groups.append(group)
    
    # groups에 대해서 위의 조건 검사 진행
    for i in range(1, 26): # offset 값
        dictionary = {}
        for idx, group in enumerate(groups): # 각 residue 집합에 대해서 다음의 조건이 부합하는지 확인
            possible_key = []
            for j in range(0, 100):
                key = str(j) if j > 9 else f'0{j}'
                if all([ciphertext == key_dict[key][plaintext][i] for plaintext, ciphertext in group]):
                    possible_key.append(j)
            if possible_key:
                dictionary[idx] = possible_key
        
        if len(dictionary) == n:
            # pp.pprint(f'################# n: {n}, offset: {i} #################\n')
            # pp.pprint(dictionary)
            combinations = dictionary

'''
The result shows that only available key length for this cipher is 25, and possible key for each digit is as follows:
Now let us delete all the redundant keys for places that have multiple key possiblilities
'''
offset = 6

confirmed_keys = set([possible_keys[0] for place, possible_keys in combinations.items() if len(possible_keys) == 1])
for key in combinations.keys():
    if len(combinations[key]) != 1:
        combinations[key] = [possible_key for possible_key in combinations[key] if possible_key not in confirmed_keys]
pp.pprint(combinations)

'''
At this stage decipher the ciphertext once to see if more heuristic can be used
'''

decryptedtext = ''
for i, char in enumerate(ciphertext):
    place = i % 25
    key = combinations[place]
    decryptedtext += key_dict[str(key[0]) if key[0] > 9 else '0' + str(key[0])][char][-offset] if len(key) == 1 else '0'
    if place == 24:
        # print(decryptedtext)
        decryptedtext = ''
    
'''
The result is:

THI0CIP0ERWASWIDELY000000
CAU0EOF0IMPLESTRUCT000000
INF0RMA0IONSECURITY000000
MOS0POP0LARKEYWORDS000000
TET0ENI0ELOOKINGPLA000000

For places of residue 3 and 7, there are only two candidates so they can be easily found by trying out all candidates.
From random trial key for place 3 is 00 and key for place 7 is 38 is as follows:

combinations[3] = [0]
combinations[7] = [38]

THISCIPHERWASWIDELY000000
CAUSEOFSIMPLESTRUCT000000
INFORMATIONSECURITY000000
MOSTPOPULARKEYWORDS000000
TETHENICELOOKINGPLA000000

We know for a fact that 000000 for the first line is 'USEDBE' and that for second line is 'URE000'.
From heuristic, we can guess that the last three '0' for second can be 'AND'.
With this in mind, trial and error can be used to find keys which make 'USEDBE' for first line and 'UREAND' for secondd line.


'''

combinations[3] = [28]
combinations[7] = [38]

candidate_19 = [31, 42, 68, 96]
candidate_20 = [5, 86]
candidate_21 = [40, 42, 57, 79, 98]
candidate_22 = [4, 24, 25, 34, 76]
candidate_23 = [69, 78]
candidate_24 = [12, 18, 48, 60, 65]
candidate_prod = product(candidate_19, candidate_20, candidate_21, candidate_22, candidate_23, candidate_24)

for a, b, c, d, e, f in candidate_prod:
    
    combinations[19] = [a]
    combinations[20] = [b]
    combinations[21] = [c]
    combinations[22] = [d]
    combinations[23] = [e]
    combinations[24] = [f]
    
    decryptedtext = ''
    for i, char in enumerate(ciphertext):
        place = i % 25
        key = combinations[place][0]
        decryptedtext += key_dict[str(key) if key > 9 else '0' + str(key)][char][-offset]
        # if place == 24:
        #     print(decryptedtext)
        #     decryptedtext = ''
    if decryptedtext[19:25] == 'USEDBE' and decryptedtext[119:125] == 'INTEXT':
        print('\n######## PLAINTEXT FOUND ########')
        print(decryptedtext)
        print('#################################\n')
        break

'''
At last print the whole key in required format
'''

answer = '('
for key, value in combinations.items():
    if key == 24:
        answer += f'{value[0]} / 25)'
        break
    answer += f'{value[0]}, '
print('The final answer is: \n' + answer)