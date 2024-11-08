import networkx as nx

def weights(adj_list,G):
    G[0][132]['weight'] = 27
    G[0][111]['weight'] = 36
    G[0][25]['weight'] = 23
    G[0][111]['weight'] = 36
    G[132][0]['weight'] = 27
    G[132][35]['weight'] = 21
    G[132][111]['weight'] = 29
    G[111][0]['weight'] = 36
    G[111][20]['weight'] = 36
    G[111][108]['weight'] = 45
    G[111][5]['weight'] = 17
    G[111][0]['weight'] = 36
    G[111][132]['weight'] = 29
    G[1][43]['weight'] = 67
    G[1][19]['weight'] = 72
    G[1][42]['weight'] = 57
    G[1][53]['weight'] = 75
    G[43][1]['weight'] = 67
    G[43][73]['weight'] = 50
    G[43][14]['weight'] = 1 #edited #87
    G[2][119]['weight'] = 26
    G[2][30]['weight'] = 17
    G[119][2]['weight'] = 26
    G[119][30]['weight'] = 12
    G[119][40]['weight'] = 27
    G[119][118]['weight'] = 31
    G[30][2]['weight'] = 17
    G[30][119]['weight'] = 12
    G[3][76]['weight'] = 34
    G[3][77]['weight'] = 46
    G[76][3]['weight'] = 34
    G[76][24]['weight'] = 42
    G[77][3]['weight'] = 46
    G[77][78]['weight'] = 57
    G[77][130]['weight'] = 60
    G[77][130]['weight'] = 60
    G[77][76]['weight'] = 2
    G[76][77]['weight'] = 2
    G[4][70]['weight'] = 33
    G[4][142]['weight'] = 39
    G[4][70]['weight'] = 33
    G[4][142]['weight'] = 39
    G[70][4]['weight'] = 33
    G[70][54]['weight'] = 59
    G[70][4]['weight'] = 33
    G[142][4]['weight'] = 39
    G[142][4]['weight'] = 39
    G[142][55]['weight'] = 38
    G[7][84]['weight'] = 32
    G[7][78]['weight'] = 81
    G[7][83]['weight'] = 78
    G[7][115]['weight'] = 70
    G[84][7]['weight'] = 32
    G[84][18]['weight'] = 31
    G[84][85]['weight'] = 73
    G[84][131]['weight'] = 41
    G[84][82]['weight'] = 71
    G[78][7]['weight'] = 81
    G[78][77]['weight'] = 57
    G[78][79]['weight'] = 65
    G[78][85]['weight'] = 58
    G[78][128]['weight'] = 42
    G[83][7]['weight'] = 78
    G[83][115]['weight'] = 35
    G[83][130]['weight'] = 56
    G[115][7]['weight'] = 70
    G[115][117]['weight'] = 83
    G[115][83]['weight'] = 35
    G[115][82]['weight'] = 35
    G[9][72]['weight'] = 32
    G[9][105]['weight'] = 34
    G[72][9]['weight'] = 32
    G[72][105]['weight'] = 27
    G[72][95]['weight'] = 101
    G[105][9]['weight'] = 34
    G[105][71]['weight'] = 34
    G[105][72]['weight'] = 27
    G[10][107]['weight'] = 20
    G[10][141]['weight'] = 27
    G[107][10]['weight'] = 20
    G[107][27]['weight'] = 37
    G[107][131]['weight'] = 54
    G[141][10]['weight'] = 27
    G[141][26]['weight'] = 21
    G[141][93]['weight'] = 65
    G[12][129]['weight'] = 39
    G[12][81]['weight'] = 56
    G[12][140]['weight'] = 32
    G[129][12]['weight'] = 39
    G[129][31]['weight'] = 42
    G[129][74]['weight'] = 28
    G[129][81]['weight'] = 77
    G[129][140]['weight'] = 44
    G[129][140]['weight'] = 44
    G[13][91]['weight'] = 50
    G[13][92]['weight'] = 59
    G[91][13]['weight'] = 50
    G[91][143]['weight'] = 37

    G[92][13]['weight'] = 59
    G[92][15]['weight'] = 53

    G[14][57]['weight'] = 46
    G[14][23]['weight'] = 65
    G[14][43]['weight'] = 1#edited
    G[14][68]['weight'] = 41

    G[57][14]['weight'] = 46
    G[57][23]['weight'] = 46
    G[57][39]['weight'] = 49
    G[57][58]['weight'] = 66
    G[57][56]['weight'] = 137
    G[57][68]['weight'] = 66

    G[15][92]['weight'] = 53
    G[15][102]['weight'] = 55

    G[102][15]['weight'] = 55
    G[102][109]['weight'] = 26

    G[16][65]['weight'] = 19
    G[16][64]['weight'] = 33

    G[65][16]['weight'] = 19
    G[65][66]['weight'] = 69
    G[65][44]['weight'] = 43

    G[64][16]['weight'] = 33
    G[64][34]['weight'] = 55
    G[64][47]['weight'] = 27

    G[18][84]['weight'] = 31
    G[18][126]['weight'] = 45

    G[126][18]['weight'] = 45
    G[126][82]['weight'] = 25
    G[126][29]['weight'] = 71
    G[126][147]['weight'] = 60

    G[19][62]['weight'] = 46
    G[19][53]['weight'] = 62
    G[19][1]['weight'] = 72

    G[62][19]['weight'] = 46
    G[62][51]['weight'] = 47
    G[62][52]['weight'] = 39

    G[53][19]['weight'] = 62
    G[53][41]['weight'] = 82
    G[53][42]['weight'] = 45
    G[53][51]['weight'] = 84
    G[53][1]['weight'] = 75

    G[20][5]['weight'] = 36
    G[20][111]['weight'] = 36
    G[20][86]['weight'] = 41
    G[20][87]['weight'] = 52

    G[5][20]['weight'] = 36
    G[5][111]['weight'] = 17

    G[86][20]['weight'] = 41
    G[86][21]['weight'] = 41
    G[86][110]['weight'] = 61
    G[86][87]['weight'] = 82

    G[87][20]['weight'] = 52
    G[87][85]['weight'] = 66
    G[87][86]['weight'] = 82
    G[87][94]['weight'] = 40
    G[87][112]['weight'] = 29

    G[23][57]['weight'] = 46
    G[23][14]['weight'] = 65
    G[23][45]['weight'] = 64
    G[23][68]['weight'] = 50

    G[24][39]['weight'] = 30
    G[24][122]['weight'] = 42
    G[24][76]['weight'] = 42
    G[24][75]['weight'] = 54

    G[39][24]['weight'] = 30
    G[39][57]['weight'] = 49

    G[122][24]['weight'] = 42
    G[122][121]['weight'] = 36
    G[122][123]['weight'] = 37

    G[75][24]['weight'] = 54
    G[75][128]['weight'] = 36
    G[75][136]['weight'] = 72 #ed
    G[75][76]['weight'] = 51
    G[136][75]['weight'] = 72
    G[76][75]['weight'] = 51

    G[25][0]['weight'] = 23
    G[25][93]['weight'] = 20
    G[93][25]['weight'] = 20
    G[93][133]['weight'] = 46
    G[93][141]['weight'] = 65
    G[93][26]['weight'] = 59
    G[93][94]['weight'] = 35

    G[26][141]['weight'] = 21
    G[26][93]['weight'] = 59
    G[26][133]['weight'] = 66

    G[27][85]['weight'] = 30
    G[27][107]['weight'] = 37
    G[27][94]['weight'] = 51

    G[85][27]['weight'] = 30
    G[85][84]['weight'] = 73
    G[85][78]['weight'] = 58
    G[85][87]['weight'] = 66

    G[31][129]['weight'] = 42
    G[31][128]['weight'] = 27

    G[32][89]['weight'] = 31
    G[32][90]['weight'] = 34


    G[89][32]['weight'] = 31
    G[89][58]['weight'] = 70
    G[89][90]['weight'] = 35

    G[90][32]['weight'] = 34
    G[90][103]['weight'] = 72
    G[90][137]['weight'] = 38

    G[34][59]['weight'] = 31
    G[34][64]['weight'] = 55
    G[34][66]['weight'] = 72
    G[34][37]['weight'] = 59

    G[59][34]['weight'] = 31
    G[59][56]['weight'] = 82
    G[59][71]['weight'] = 22

    G[66][34]['weight'] = 72
    G[66][44]['weight'] = 47
    G[66][65]['weight'] = 69
    G[66][125]['weight'] = 68

    G[37][34]['weight'] = 59
    G[37][124]['weight'] = 43
    G[37][56]['weight'] = 44

    G[35][132]['weight'] = 21
    G[35][108]['weight'] = 21
    G[35][134]['weight'] = 43

    G[108][35]['weight'] = 21
    G[108][110]['weight'] = 58
    G[108][111]['weight'] = 45

    G[124][37]['weight'] = 43
    G[124][123]['weight'] = 25
    G[124][125]['weight'] = 68

    G[40][120]['weight'] = 17
    G[40][119]['weight'] = 27

    G[120][40]['weight'] = 17
    G[120][114]['weight'] = 47
    G[120][118]['weight'] = 49

    G[41][50]['weight'] = 59
    G[41][61]['weight'] = 72
    G[41][51]['weight'] = 82
    G[41][53]['weight'] = 82
    G[41][54]['weight'] = 76
    G[41][67]['weight'] = 60

    G[50][41]['weight'] = 59
    G[50][49]['weight'] = 60

    G[50][51]['weight'] = 77
    G[50][61]['weight'] = 51

    G[61][41]['weight'] = 72
    G[61][54]['weight'] = 67
    G[61][50]['weight'] = 51

    G[51][41]['weight'] = 82
    G[51][50]['weight'] = 77

    G[51][62]['weight'] = 47
    G[51][53]['weight'] = 84

    G[51][62]['weight'] = 47

    G[54][41]['weight'] = 76
    G[54][55]['weight'] = 65
    G[54][61]['weight'] = 67
    G[54][70]['weight'] = 59

    G[67][41]['weight'] = 60

    G[42][1]['weight'] = 57
    G[42][55]['weight'] = 146
    G[42][53]['weight'] = 45
    G[42][73]['weight'] = 20 #edit
    G[55][42]['weight'] = 146
    G[55][54]['weight'] = 65
    G[55][95]['weight'] = 52
    G[55][142]['weight'] = 38

    G[73][42]['weight'] = 52
    G[73][43]['weight'] = 50
    G[73][46]['weight'] = 65
    G[73][68]['weight'] = 47

    G[44][113]['weight'] = 41
    G[44][66]['weight'] = 47
    G[44][65]['weight'] = 43

    G[113][44]['weight'] = 41
    G[113][118]['weight'] = 60

    G[45][23]['weight'] = 64
    G[45][46]['weight'] = 94
    G[45][56]['weight'] = 47

    G[46][45]['weight'] = 94
    G[46][73]['weight'] = 65

    G[56][45]['weight'] = 47
    G[56][37]['weight'] = 44
    G[56][57]['weight'] = 137
    G[56][59]['weight'] = 82
    G[56][95]['weight'] = 64
    G[56][124]['weight'] = 68

    G[47][63]['weight'] = 47
    G[47][64]['weight'] = 27

    G[63][47]['weight'] = 47
    G[63][71]['weight'] = 19

    G[48][114]['weight'] = 24
    G[48][116]['weight'] = 33

    G[114][48]['weight'] = 24
    G[114][120]['weight'] = 47

    G[49][50]['weight'] = 60

    G[52][62]['weight'] = 39
    G[95][55]['weight'] = 52
    G[95][56]['weight'] = 64
    G[95][72]['weight'] = 101

    G[58][57]['weight'] = 66
    G[58][28]['weight'] = 52
    G[58][38]['weight'] = 38
    G[58][89]['weight'] = 70
    G[58][136]['weight'] = 76
    G[58][36]['weight'] = 63

    G[28][58]['weight'] = 52

    G[38][58]['weight'] = 38

    G[136][58]['weight'] = 76
    G[136][74]['weight'] = 30
    G[136][104]['weight'] = 47

    G[36][58]['weight'] = 63
    G[36][104]['weight'] = 21

    G[71][63]['weight'] = 19
    G[71][105]['weight'] = 34
    G[71][59]['weight'] = 22

    G[68][73]['weight'] = 47
    G[68][57]['weight'] = 66
    G[68][23]['weight'] = 50
    G[68][14]['weight'] = 41

    G[74][129]['weight'] = 28
    G[74][125]['weight'] = 170
    G[74][136]['weight'] = 30

    G[130][77]['weight'] = 60
    G[130][125]['weight'] = 44
    G[130][83]['weight'] = 56

    G[79][78]['weight'] = 65
    G[79][112]['weight'] = 29
    G[79][106]['weight'] = 34
    G[79][140]['weight'] = 16

    G[112][79]['weight'] = 29
    G[112][87]['weight'] = 29

    G[106][79]['weight'] = 34
    G[106][21]['weight'] = 32
    G[106][80]['weight'] = 47

    G[81][12]['weight'] = 56
    G[81][80]['weight'] = 58
    G[81][129]['weight'] = 77
    G[81][139]['weight'] = 59

    G[80][81]['weight'] = 58
    G[80][106]['weight'] = 47

    G[82][126]['weight'] = 25
    G[82][84]['weight'] = 71
    G[82][115]['weight'] = 35
    G[82][116]['weight'] = 92

    G[131][84]['weight'] = 41
    G[131][107]['weight'] = 54
    G[131][147]['weight'] = 84

    G[110][86]['weight'] = 61
    G[110][108]['weight'] = 58
    G[110][109]['weight'] = 37

    G[94][87]['weight'] = 40
    G[94][93]['weight'] = 35
    G[94][27]['weight'] = 51

    G[88][17]['weight'] = 31
    G[88][97]['weight'] = 77
    G[88][8]['weight'] = 46
    G[88][137]['weight'] = 36

    G[17][88]['weight'] = 31
    G[17][96]['weight'] = 28

    G[97][88]['weight'] = 77

    G[8][88]['weight'] = 46
    G[8][138]['weight'] = 25
    G[8][143]['weight'] = 35

    G[133][93]['weight'] = 46
    G[133][134]['weight'] = 44
    G[133][26]['weight'] = 66
    #
    G[96][33]['weight'] = 25
    G[96][22]['weight'] = 52
    G[96][17]['weight'] = 28
    #
    G[33][96]['weight'] = 25

    G[22][96]['weight'] = 52

    # G[99][98]['weight'] = 0
    #
    # G[98][99]['weight'] = 0
    #
    G[109][102]['weight'] = 26
    G[109][110]['weight'] = 37
    G[109][144]['weight'] = 84

    G[103][11]['weight'] = 30
    G[103][104]['weight'] = 49
    G[103][81]['weight'] = 86
    G[11][103]['weight'] = 30
    G[11][138]['weight'] = 17

    G[104][103]['weight'] = 49
    G[104][36]['weight'] = 21
    G[104][136]['weight'] = 47

    G[21][106]['weight'] = 32
    G[21][80]['weight'] = 34
    G[118][113]['weight'] = 60
    G[118][120]['weight'] = 49
    G[118][119]['weight'] = 31

    G[117][115]['weight'] = 83

    G[116][82]['weight'] = 92
    G[116][48]['weight'] = 33

    G[121][122]['weight'] = 36
    G[121][125]['weight'] = 32
    G[121][76]['weight'] = 27
    G[76][121]['weight'] = 27

    G[123][122]['weight'] = 37
    G[123][124]['weight'] = 25
    G[123][57]['weight'] = 83

    G[125][124]['weight'] = 68
    G[125][121]['weight'] = 32
    G[125][66]['weight'] = 68
    G[125][74]['weight'] = 170
    G[125][130]['weight'] = 44

    G[29][126]['weight'] = 71
    G[29][147]['weight'] = 67

    G[128][75]['weight'] = 36
    G[128][78]['weight'] = 42
    G[128][31]['weight'] = 27

    G[140][129]['weight'] = 44
    G[140][79]['weight'] = 16
    G[140][12]['weight'] = 32
    G[134][133]['weight'] = 44
    G[134][135]['weight'] = 38
    G[134][35]['weight'] = 43

    G[135][134]['weight'] = 38
    G[135][6]['weight'] = 47

    G[6][135]['weight'] = 47
    G[6][146]['weight'] = 48

    G[137][138]['weight'] = 36
    G[137][90]['weight'] = 38
    G[137][88]['weight'] = 36

    G[138][137]['weight'] = 36
    G[138][139]['weight'] = 38
    G[138][11]['weight'] = 17
    G[138][8]['weight'] = 25

    G[139][138]['weight'] = 38
    G[139][81]['weight'] = 59
    G[139][143]['weight'] = 36

    G[143][139]['weight'] = 36
    G[143][91]['weight'] = 37
    G[143][8]['weight'] = 35

    G[144][109]['weight'] = 84
    G[144][145]['weight'] = 36

    G[145][146]['weight'] = 25
    G[145][144]['weight'] = 36

    G[146][145]['weight'] = 25
    G[146][6]['weight'] = 48

    G[147][29]['weight'] = 67
    G[147][126]['weight'] = 60
    G[147][131]['weight'] = 84

    G[127][91]['weight'] = 60
    G[127][80]['weight'] = 45
    G[80][127]['weight'] = 45
    G[91][127]['weight'] = 60
    G[92][91]['weight'] = 41
    G[92][102]['weight'] = 65
    G[102][92]['weight'] = 65
    G[91][92]['weight'] = 41

    G[148][81]['weight'] = 21
    G[81][148]['weight'] = 21

    G[148][103]['weight'] = 51
    G[103][148]['weight'] = 51

    G[148][139]['weight'] = 39
    G[139][148]['weight'] = 39

    G[148][11]['weight'] = 39
    G[11][148]['weight'] = 39

    #
    #
    #
