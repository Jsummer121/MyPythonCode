N, M = input().split(' ')  # N��ʾ������M��ʾѭ���� �ں��������ʱ������ĸ���ΪM+1��
N, M = int(N), int(M)
a = {}
c = []
T = 0
# ѭ�����պ���ÿ��ѭ��������Ȼ����浽�ֵ�����
for i in range(1, N+1):
    b = input().split(' ')
    a[i] = [int(x) for x in b]
    c.append(abs(sum(a[i][1:])))
    T += a[i][0] - c[i-1]

P = max(c)
k = c.index(P)
print(str(T)+' '+str(k+1)+' '+str(P))
""" T ƻ�����ܺ�
    k ����������һ��
    P ����Ϊ

73 -8 -6 -4
76 -5 -10 -8
80 -6 -15 0
"""