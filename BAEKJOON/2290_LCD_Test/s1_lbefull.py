s, n = input().split()
s = int(s)
p1 = {'1': ' ' * s + '  ', '2': ' ' + '-' * s + ' '}
p1['3'] = p1['5'] = p1['6'] = p1['7'] = p1['8'] = p1['9'] = p1['0'] = p1['2']
p1['4'] = p1['1']
p2 = {'1': ' ' * s + ' |', '4': '|' + ' ' * s + '|', '5': '| ' + ' ' * s}
p2['2'] = p2['3'] = p2['7'] = p2['1']
p2['6'] = p2['5']
p2['8'] = p2['9'] = p2['0'] = p2['4']
p3 = p1.copy()
p3['4'] = p3['2']
p3['7'] = p3['0'] = p3['1']
p4 = p2.copy()
p4['2'] = p2['5']
p4['4'] = p4['5'] = p4['9'] = p4['1']
p4['6'] = p4['8']
p5 = p1.copy()
p5['7'] = p5['1']
answer = []
p = [p1, p2, p3, p4, p5]
for i in range(5):                                      # s=1 기준으로 5줄 숫자를 딕셔너리로 미리 지정해놓고
    l = 1                                               # 2,4번째 줄은 s번 출력
    if i in [1, 3]:
        l = s
    for j in range(l):
        for k in n:
            answer.append(p[i][k] + ' ')
        answer.append('\n')
print(''.join(answer))
