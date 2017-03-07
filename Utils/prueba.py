# -*- coding: utf-8 -*-

cadena = '''
Trying 192.168.4.50...
Connected to 192.168.4.50.
Escape character is '^]'.

User:admin
Password:*********
console>show interfaces status

Port   Type                            Duplex  Speed    Neg  Link  Flow Control
                                                             State Status
-----  ------------------------------  ------  -------  ---- ----- -----------
1/g1   Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g2   Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g3   Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g4   Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g5   Gigabit - Level                 Full    100      Auto  Up    Inactive
1/g6   Gigabit - Level                 Full    100      Auto  Up    Inactive
1/g7   Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g8   Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g9   Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g10  Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g11  Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g12  Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/g13  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g14  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g15  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g16  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g17  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g18  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g19  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
--More-- or (q)uit
1/g20  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g21  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g22  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g23  Gigabit - Level                 N/A     Unknown  Auto  Down  Inactive
1/g24  Gigabit - Level                 Full    1000     Auto  Up    Inactive
1/xg1  10G - Level                     N/A     Unknown  Auto  Down  Inactive
1/xg2  10G - Level                     N/A     Unknown  Auto  Down  Inactive
1/xg3  10G - Level                     N/A     Unknown  Auto  Down  Inactive
1/xg4  10G - Level                     N/A     Unknown  Auto  Down  Inactive


Ch   Type                            Link
                                     State
---  ------------------------------  -----
ch1  Link Aggregate                  Down
ch2  Link Aggregate                  Down
ch3  Link Aggregate                  Down
ch4  Link Aggregate                  Down
ch5  Link Aggregate                  Down
ch6  Link Aggregate                  Down
ch7  Link Aggregate                  Down
ch8  Link Aggregate                  Down
ch9  Link Aggregate                  Down
--More-- or (q)uit
ch10 Link Aggregate                  Down
ch11 Link Aggregate                  Down
ch12 Link Aggregate                  Down
ch13 Link Aggregate                  Down
ch14 Link Aggregate                  Down
ch15 Link Aggregate                  Down
ch16 Link Aggregate                  Down
ch17 Link Aggregate                  Down
ch18 Link Aggregate                  Down
ch19 Link Aggregate                  Down
ch20 Link Aggregate                  Down
ch21 Link Aggregate                  Down
ch22 Link Aggregate                  Down
ch23 Link Aggregate                  Down
ch24 Link Aggregate                  Down

Flow Control:Disabled '''

for line in cadena.splitlines():
    if 'Level' in line:
        unit = line[0]
        boca = line.split(unit + '/')[1][1:3]
        if 'Up' in line:
            status = 'Up'
        else:
            status = 'Down'

        print([unit, boca, status])
