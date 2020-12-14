m_1 = input()
m_2 = input()
if len(m_1)!=len(m_2):
    print(1)
elif m_1 == m_2:
    print(2)
elif m_1.upper() == m_2.upper():
    print(3)
else:
    print(4)
