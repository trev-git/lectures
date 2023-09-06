from string import ascii_uppercase

text = """
MJZYB LGESE CNCMQ YGXYS PYZDZ PMYGI IRLLC
PAYCK YKGWZ MCWZK YFRCM ZYVCX XCLZP MYXLG
WYTJS MYGPZ YWCAJ MYCWS ACPZY XGLYZ HSWBN
ZYXZT YTGRN VYMJC POYMJ SMYCX YMJZL ZYSLZ
YMTZP MQYMJ LZZYB ZGBNZ YCPYS YLGGW YMJZP
YMJZL ZYCKY ZPYZD ZPKYI JSPIZ YMJSM YMJZL
ZYSLZ YMTGY GXYMJ ZWYTC MJYMJ ZYKSW ZYECL
MJVSQ YERMY MJCKY CKYKG
"""

text = text.upper()

print(ascii_uppercase)
cnt = {ch:text.count(ch) for ch in ascii_uppercase}

for key in cnt:
    if cnt[key] > 0:
        print(f'{key}: {cnt[key]}')