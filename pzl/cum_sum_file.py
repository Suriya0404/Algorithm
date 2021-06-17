# [u'tourney_id', u'tourney_name', u'surface', u'draw_size', u'tourney_level', u'tourney_date', u'match_num', u'winner_id', u'winner_seed', u'winner_entry', u'winner_name', u'winner_hand', u'winner_ht', u'winner_ioc', u'winner_age', u'winner_rank', u'winner_rank_points', u'loser_id', u'loser_seed', u'loser_entry', u'loser_name', u'loser_hand', u'loser_ht', u'loser_ioc', u'loser_age', u'loser_rank', u'loser_rank_points', u'score', u'best_of', u'round', u'minutes', u'w_ace', u'w_df', u'w_svpt', u'w_1stIn', u'w_1stWon', u'w_2ndWon', u'w_SvGms', u'w_bpSaved', u'w_bpFaced', u'l_ace', u'l_df', u'l_svpt', u'l_1stIn', u'l_1stWon', u'l_2ndWon', u'l_SvGms', u'l_bpSaved', u'l_bpFaced']

from collections import Counter

def solution(csvData):
    # Type your solution here
    cnt = 0
    winner_cnt = Counter()
    loser_cnt = Counter()
    output = ['tourney_date, winner_name, loser_name,winner_cumulative_wins,loser_cumulative_wins']

    for line in csvData:
        if cnt == 0:            # Header record
            header = line.split(',')
            cnt += 1
        else:                    # Data
            row = line.split(',')

            tourney_date = row[5]
            winner_name = row[10]
            loser_name = row[20]

            winner_cnt[winner_name] += 1
            loser_cnt[loser_name] += 1

            output.append(tourney_date + ',' +
                          winner_name + ',' +
                          loser_name + ',' +
                          str(winner_cnt[winner_name]) + ',' +
                          str(loser_cnt[loser_name]))

    return output


if __name__ == '__main__':
    data = [    u'tourney_id,tourney_name,surface,draw_size,tourney_level,tourney_date,match_num,winner_id,winner_seed,winner_entry,winner_name,winner_hand,winner_ht,winner_ioc,winner_age,winner_rank,winner_rank_points,loser_id,loser_seed,loser_entry,loser_name,loser_hand,loser_ht,loser_ioc,loser_age,loser_rank,loser_rank_points,score,best_of,round,minutes,w_ace,w_df,w_svpt,w_1stIn,w_1stWon,w_2ndWon,w_SvGms,w_bpSaved,w_bpFaced,l_ace,l_df,l_svpt,l_1stIn,l_1stWon,l_2ndWon,l_SvGms,l_bpSaved,l_bpFaced',
                u'2018-M020,Brisbane,Hard,32,A,20180101,300,106401,3,,Nick Kyrgios,R,193,AUS,22.6830937714,21,2010,105992,,,Ryan Harrison,R,183,USA,25.6536618754,47,1010,6-4 6-2,3,F,73,17,1,56,40,33,9,9,5,5,8,3,58,32,22,12,9,4,7',
                u'2018-M020,Brisbane,Hard,32,A,20180101,299,106401,3,,Nick Kyrgios,R,193,AUS,22.6830937714,21,2010,105777,1,,Grigor Dimitrov,R,188,BUL,26.6310746064,3,5150,3-6 6-1 6-4,3,SF,93,19,2,72,50,41,11,13,1,2,5,6,74,44,32,16,13,3,6',
                u'2018-M020,Brisbane,Hard,32,A,20180101,298,105992,,,Ryan Harrison,R,183,USA,25.6536618754,47,1010,200282,,WC,Alex De Minaur,R,,AUS,18.8720054757,208,245,4-6 7-6(5) 6-4,3,SF,157,14,5,115,70,49,24,16,3,6,9,5,94,62,49,16,16,0,3',
                u'2018-M020,Brisbane,Hard,32,A,20180101,297,105777,1,,Grigor Dimitrov,R,188,BUL,26.6310746064,3,5150,106378,,,Kyle Edmund,R,,GBR,22.9815195072,50,992,6-3 6-7(3) 6-4,3,QF,145,12,9,103,65,54,18,16,2,2,6,1,89,53,39,23,15,4,6',
                u'2018-M020,Brisbane,Hard,32,A,20180101,296,106401,3,,Nick Kyrgios,R,193,AUS,22.6830937714,21,2010,105238,,,Alexandr Dolgopolov,R,180,UKR,29.1498973306,38,1231,1-6 6-3 6-4,3,QF,90,18,5,69,43,38,11,13,1,3,6,3,75,41,33,16,13,2,4',
                u'2018-M020,Brisbane,Hard,32,A,20180101,295,200282,,WC,Alex De Minaur,R,,AUS,18.8720054757,208,245,111581,,Q,Michael Mmoh,R,,USA,19.9753593429,175,299,6-4 6-0,3,QF,74,6,1,46,23,18,17,8,3,3,3,5,51,29,18,8,8,3,7',
                u'2018-M020,Brisbane,Hard,32,A,20180101,294,105992,,,Ryan Harrison,R,183,USA,25.6536618754,47,1010,104797,,,Denis Istomin,R,188,UZB,31.318275154,63,809,7-6(6) 4-2 RET,3,QF,96,11,2,60,34,27,14,9,1,2,3,1,67,46,29,12,9,5,7',
                u'2018-M020,Brisbane,Hard,32,A,20180101,293,105777,1,,Grigor Dimitrov,R,188,BUL,26.6310746064,3,5150,105357,,WC,John Millman,R,183,AUS,28.5503080082,128,436,4-6 7-6(8) 6-3,3,R16,155,6,5,113,65,51,22,16,4,7,5,1,101,67,46,18,15,3,6',
                u'2018-M020,Brisbane,Hard,32,A,20180101,292,106378,,,Kyle Edmund,R,,GBR,22.9815195072,50,992,111202,,,Hyeon Chung,R,,KOR,21.620807666,58,844,7-6(3) 5-7 6-4,3,R16,158,12,3,102,66,54,16,17,1,3,11,1,109,75,51,20,17,6,8',
                u'2018-M020,Brisbane,Hard,32,A,20180101,291,106401,3,,Nick Kyrgios,R,193,AUS,22.6830937714,21,2010,105051,,,Matthew Ebden,R,188,AUS,30.0999315537,76,670,6-7(3) 7-6(5) 6-2,3,R16,132,13,2,100,62,53,21,16,2,2,11,2,105,78,58,16,16,5,7',
                u'2018-M020,Brisbane,Hard,32,A,20180101,290,105238,,,Alexandr Dolgopolov,R,180,UKR,29.1498973306,38,1231,104547,,,Horacio Zeballos,L,188,ARG,32.681724846,66,768,6-1 6-2,3,R16,64,9,2,51,33,25,10,7,4,4,2,2,49,28,15,7,8,2,7',
                u'2018-M020,Brisbane,Hard,32,A,20180101,289,111581,,Q,Michael Mmoh,R,,USA,19.9753593429,175,299,104999,8,,Mischa Zverev,L,190,GER,30.3627652293,33,1302,6-2 5-7 6-4,3,R16,152,12,3,111,67,48,22,15,6,8,11,3,83,50,37,17,15,4,8',
                u'2018-M020,Brisbane,Hard,32,A,20180101,288,200282,,WC,Alex De Minaur,R,,AUS,18.8720054757,208,245,105683,4,,Milos Raonic,R,196,CAN,27.0143737166,24,1795,6-4 6-4,3,R16,94,5,0,67,41,29,16,10,5,6,9,4,63,38,26,13,10,7,10',
                u'2018-M020,Brisbane,Hard,32,A,20180101,287,104797,,,Denis Istomin,R,188,UZB,31.318275154,63,809,111577,,,Jared Donaldson,R,,USA,21.2292950034,54,890,7-6(5) 6-2,3,R16,91,6,1,63,45,35,8,10,5,7,4,9,72,35,26,15,10,5,9',
                u'2018-M020,Brisbane,Hard,32,A,20180101,286,105992,,,Ryan Harrison,R,183,USA,25.6536618754,47,1010,105870,,LL,Yannick Hanfmann,U,,GER,26.135523614,119,499,6-7(5) 6-4 6-2,3,R16,145,19,5,96,54,43,23,15,8,9,5,5,115,68,50,17,15,7,11']

    print(solution(data))

['tourney_date, winner_name, loser_name,winner_cumulative_wins,loser_cumulative_wins',
 u'20180101,Nick Kyrgios,Ryan Harrison,1,1',
 u'20180101,Nick Kyrgios,Grigor Dimitrov,2,1',
 u'20180101,Ryan Harrison,Alex De Minaur,1,1',
 u'20180101,Grigor Dimitrov,Kyle Edmund,1,1',
 u'20180101,Nick Kyrgios,Alexandr Dolgopolov,3,1',
 u'20180101,Alex De Minaur,Michael Mmoh,1,1',
 u'20180101,Ryan Harrison,Denis Istomin,2,1',
 u'20180101,Grigor Dimitrov,John Millman,2,1',
 u'20180101,Kyle Edmund,Hyeon Chung,1,1',
 u'20180101,Nick Kyrgios,Matthew Ebden,4,1',
 u'20180101,Alexandr Dolgopolov,Horacio Zeballos,1,1',
 u'20180101,Michael Mmoh,Mischa Zverev,1,1',
 u'20180101,Alex De Minaur,Milos Raonic,2,1',
 u'20180101,Denis Istomin,Jared Donaldson,1,1',
 u'20180101,Ryan Harrison,Yannick Hanfmann,3,1']
