# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://www.baseball-reference.com/bullpen/Baseball_statistics for all the stats
# Megan helped and gave feedback
# football stats https://simulatedfootball.com/tools/points-calculator.html
# jersey numbers: https://bleacherreport.com/articles/2883209-the-best-nba-players-by-jersey-number  
# jersey numbers https://www.basketball-reference.com/leagues/NBA_2020_numbers.html

def average():
        avg_hits=int(input("enter the amount of hits you had "))
        avg_atbats=int(input("enter the amount of plate appearances you had "))
        finalavg=float(avg_hits/avg_atbats)
        avg_list = [f"{avg_hits} / {avg_atbats}"]
        for x in avg_list:
            print(x)
        print(f"your batting average is {finalavg}")
        while finalavg<=0.5:
            print("That's a very high batting average! good job")
            break


def onbaseperc():
        obp_abs=int(input("how many plate appearances did you have? "))
        obp_hits=int(input("how many hits did you get? "))
        obp_walks=int(input("how many times did you get walked? "))
        obp_hbp=int(input("how many times did you get hit by a pitch? "))
        obp_sf=int(input("how many times did you hit a sacrifice fly? "))
        finalobp=((obp_hits + obp_walks + obp_hbp) / (obp_abs + obp_hits + obp_walks + obp_sf + obp_hbp))
        obp_list = [f"({obp_hits} + {obp_walks} + {obp_hbp}) / ({obp_abs} + {obp_hits} + {obp_walks} + {obp_sf} + {obp_hbp}) "]
        for x in obp_list:
            print(x)
        print (f"your on base percentage is {finalobp}")

def slugging():
    
    slg_abs=int(input("how many plate appearances did you have? "))
    slg_single=int(input("how many singles did you hit? "))
    slg_double=int(input("how many doubles did you hit? "))
    slg_triples=int(input("how many triples did you hit? "))
    slg_homer=int(input("how many home runs did you hit? "))
    slg=float(((slg_single)+(2*slg_double)+(3*slg_triples)+(slg_homer*4))/ slg_abs)
    slg_list = [f"({slg_single} + {slg_double*2} + {slg_triples*3} + {slg_homer*4}) / {slg_abs} = {slg}"]
    for x in slg_list:
        print(x)
    print (f"your slugging percentage is {slg}")

def ops():
    ops_abs=int(input("how many plate appearances did you have? "))
    ops_single=int(input("how many singles did you hit? "))
    ops_double=int(input("how many doubles did you hit? "))
    ops_triples=int(input("how many triples did you hit? "))
    ops_homer=int(input("how many home runs did you hit? "))
    ops_hits=int(input("how many hits did you get? "))
    ops_walks=int(input("how many times did you get walked? "))
    ops_hbp=int(input("how many times did you get hit by a pitch? "))
    ops_sf=int(input("how many times did you hit a sacrifice fly? "))
    final_ops1=float(((ops_single)+(2*ops_double)+(3*ops_triples)+(ops_homer*4))/ ops_abs)
    finalops2=float((ops_hits + ops_walks + ops_hbp) / (ops_abs + ops_hits + ops_walks + ops_sf + ops_hbp))
    final_ops=(final_ops1+finalops2)
    opslist=[f"({ops_hits} + {ops_walks} + {ops_hbp}) / ({ops_abs} + {ops_hits} + {ops_walks} + {ops_sf} + {ops_hbp}) + ({ops_single} + {ops_double*2} + {ops_triples*3} + {ops_homer*4}) / {ops_abs}) = {final_ops}"]
    for x in opslist:
        print(x)
    print (f"your OPS percentage is {final_ops}")

def passperc():
    pass_attempts=int(input("how many passes did you throw? "))
    pass_comp=int(input("how many passes did you complete? "))
    finalpassperc=float(pass_comp / pass_attempts)
    passperc_list=[f"{pass_comp} / {pass_attempts} = {finalpassperc}"]
    for x in passperc_list:
        print(x)
    print (f"your pass completion percentage is {finalpassperc}")
    while pass_comp<=10:
        print("That's alot of completions! good job")
        break

def yards_compl():
    completions=int(input("How many passes did you complete? "))
    yards=int(input("How many total yards passing do you have? "))
    finalyardcomp=float(yards / completions)
    completionlist={f"{yards} / {completions} = {finalyardcomp}"}
    for x in completionlist:
        print(x)
    print (f"you average {finalyardcomp} yards per completion")
    while yards<=100:
        print("That's alot of yards! good job")
        break

def yardsperattempt():
    attempts=int(input("How many times did you attempt to throw the ball? "))
    yards2=int(input("How many total yards passing do you have? "))
    finalyrdatt=float(yards2 / attempts)
    list_attemptyard={f"{yards2} / {attempts} = {finalyrdatt}"}
    for x in list_attemptyard:
        print(x)
    print (f"you average {finalyrdatt} yards per attempt")
    while yards2<=100:
        print("That's alot of yards! good job")
        break

def yardsrush():
    rushattempts=int(input("How many times did you attempt to run the ball? "))
    yards3=int(input("How many total yards running do you have? "))
    finalrun=float(yards3 / rushattempts)
    list_attemptyard={f"{yards3} / {rushattempts} = {finalrun}"}
    for x in list_attemptyard:
        print(x)
    print (f"you average {finalrun} yards per run")
    while yards3<=100:
        print("That's alot of yards! good job")
        break

def fieldgoal():
    fg_attempt=int(input("How many times did you attempt a field goal? "))
    fg_made=int(input("How many times did you make a field goal? "))
    final_fg_perc=float(fg_made / fg_attempt)
    total_fgpoints=float(fg_made*3)
    list_fg={f"{fg_made} / {fg_attempt} = {final_fg_perc}"}
    for x in list_fg:
        print(x)
    print (f"your field goal percentage is {final_fg_perc} and in total, you got {total_fgpoints} points")
    while fg_made<=10:
        print("That's alot of points! good job")
        break

def tripledouble():
    td_points=int(input("How many points did you score? "))
    td_rebs=int(input("How many rebounds did you get? "))
    td_assists=int(input("How many assists did you get? "))
    td_steals=int(input("How many steals did you get? "))
    td_blocks=int(input("How many times did you block a shot? "))
    if td_points>=10 and td_rebs>=10 and td_assists>=10:
        print ("You got a triple double!")
    elif td_points>=10 and td_steals>=10 and td_blocks>=10:
        print ("You got a triple double!")
    elif td_rebs>=10 and td_assists>=10 and td_steals>=10:
        print ("You got a triple double!")
    elif td_rebs>=10 and td_blocks>=10 and td_points>=10:
        print ("You got a triple double!")
    elif td_assists>=10 and td_steals>=10 and td_blocks>=10:
        print ("You got a triple double!")
    elif td_assists>=10 and td_points>=10 and td_blocks>=10:
        print ("You got a triple double!")
    elif td_steals>=10 and td_blocks>=10 and td_points>=10:
        print ("You got a triple double!")
    elif td_steals>=10 and td_assists>=10 and td_points>=10:
        print ("You got a triple double!")
    elif td_steals>=10 and td_assists>=10 and td_rebs>=10:
        print ("You got a triple double!")
    elif td_blocks>=10 and td_points>=10 and td_rebs>=10:
        print ("You got a triple double!")
    elif td_blocks>=10 and td_assists>=10 and td_steals>=10:
        print ("You got a triple double!")
    elif td_blocks>=10 and td_assists>=10 and td_steals>=10 and td_points>=10 and td_rebs>=10:
        print ("You got a triple double!")
    elif td_blocks>=10 and td_assists>=10 and td_steals>=10 and td_points>=10:
        print ("You got a triple double!")
    elif td_blocks>=10 and td_assists>=10 and td_steals>=10 and td_rebs>=10:
        print ("You got a triple double!")
    elif td_blocks>=10 and td_assists>=10 and td_points>=10 and td_rebs>=10:
        print ("You got a triple double!")
    elif td_blocks>=10 and td_steals>=10 and td_points>=10 and td_rebs>=10:
        print ("You got a triple double!")
    elif td_assists>=10 and td_steals>=10 and td_points>=10 and td_rebs>=0:
        print ("You got a triple double!")
    else:
        print("you did not get a triple double")

def shotperc():
    shotattempt=int(input("How many shots did you take? "))
    shotmake=int(input("How many shots did you make? "))
    finalperc=(shotmake/shotattempt)
    shotstring=[f"{shotmake} / {shotattempt} = {finalperc}"]
    for x in shotstring:
        print(x)
    print(f"your shot percentage is {finalperc}")
    while shotmake<=10:
        print("That's alot of points! good job")
        break

def jerseynumber():
    inputjersey=int(input("Enter a jersey number (0-99) "))
    if inputjersey==0:
        list_0=["Russell Westbrook", "Gilbert Arenas"]
        asklegendint0=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint0==1:
            print(list_0[0])
        elif asklegendint0==2:
            print(list_0[1])
    
    elif inputjersey==1:
        list_1=["Zion Williamson", "Tracy McGrady"]
        asklegendint1=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint1==1:
            print(list_1[0])
        elif asklegendint1==2:
            print(list_1[1])
    
    elif inputjersey==2:
        list_2=["Kawhi Leonard", "Moses Malone"]
        asklegendint2=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint2==1:
            print(list_2[0])
        elif asklegendint2==2:
            print(list_2[1])
    
    elif inputjersey==3:
        list_3=["Chris Paul", "Dwyane Wade"]
        asklegendint3=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint3==1:
            print(list_3[0])
        elif asklegendint3==2:
            print(list_3[1])
    
    elif inputjersey==4:
        list_4=["Victor Oladipo", "Dolph Schayes"]
        asklegendint4=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint4==1:
            print(list_4[0])
        elif asklegendint4==2:
            print(list_4[1])

    elif inputjersey==5:
        list_5=["De'Aaron Fox", "Jason Kidd"]
        asklegendint5=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint5==1:
            print(list_5[0])
        elif asklegendint5==2:
            print(list_5[1])

    elif inputjersey==6:
        list_6=["Kristaps Porzingis", "Bill Russell"]
        asklegendint6=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint6==1:
            print(list_6[0])
        elif asklegendint6==2:
            print(list_6[1])
    
    elif inputjersey==7:
        list_7=["Kyle Lowry", "Pete Maravich"]
        asklegendint7=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint7==1:
            print(list_7[0])
        elif asklegendint7==2:
            print(list_7[1])

    elif inputjersey==8:
        list_8=["Kemba Walker", "Kobe Bryant"]
        asklegendint8=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint8==1:
            print(list_8[0])
        elif asklegendint8==2:
            print(list_8[1])

    elif inputjersey==9:
        list_9=["Nikola Vucevic", "Bob Petitt"]
        asklegendint9=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint9==1:
            print(list_9[0])
        elif asklegendint9==2:
            print(list_9[1])

    elif inputjersey==10:
        list_10=["DeMar Derozan", "Walt Frazier"]
        asklegendint10=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint10==1:
            print(list_10[0])
        elif asklegendint10==2:
            print(list_10[1])

    elif inputjersey==11:
        list_11=["Klay Thompson", "Yao Ming"]
        asklegendint11=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint11==1:
            print(list_11[0])
        elif asklegendint11==2:
            print(list_11[1])

    elif inputjersey==12:
        list_12=["Ja Morant", "John Stockton"]
        asklegendint12=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint12==1:
            print(list_12[0])
        elif asklegendint12==2:
            print(list_12[1])

    elif inputjersey==13:
        list_13=["James Harden", "Wilt Chamberlain"]
        asklegendint13=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint13==1:
            print(list_13[0])
        elif asklegendint13==2:
            print(list_13[1])

    elif inputjersey==14:
        list_14=["Tyler Herro", "Oscar Robertson"]
        asklegendint14=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint14==1:
            print(list_14[0])
        elif asklegendint14==2:
            print(list_14[1])

    elif inputjersey==15:
        list_15=["Nikola Jokic", "Vince Carter"]
        asklegendint15=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint15==1:
            print(list_15[0])
        elif asklegendint15==2:
            print(list_15[1])

    elif inputjersey==16:
        list_16=["Juwan Morgan", "Pau Gasol"]
        asklegendint16=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint16==1:
            print(list_16[0])
        elif asklegendint16==2:
            print(list_16[1])

    elif inputjersey==17:
        list_17=["Jonas Valanciunas", "Pau Gasol"]
        asklegendint17=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint17==1:
            print(list_17[0])
        elif asklegendint17==2:
            print(list_17[1])

    elif inputjersey==18:
        list_18=["Dion Waiters", "Dave Cowens"]
        asklegendint18=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint18==1:
            print(list_18[0])
        elif asklegendint18==2:
            print(list_18[1])

    elif inputjersey==19:
        list_19=["Tyson Chandler", "Willis Reed"]
        asklegendint19=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint19==1:
            print(list_19[0])
        elif asklegendint19==2:
            print(list_19[1])

    elif inputjersey==20:
        list_20=["Gordon Hayward", "Gary Payton"]
        asklegendint20=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint20==1:
            print(list_20[0])
        elif asklegendint20==2:
            print(list_20[1])

    elif inputjersey==21:
        list_21=["Joel Embiid", "Tim Duncan"]
        asklegendint21=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint21==1:
            print(list_21[0])
        elif asklegendint21==2:
            print(list_21[1])

    elif inputjersey==22:
        list_22=["Jimmy Butler", "Clyde Drexler"]
        asklegendint22=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint22==1:
            print(list_22[0])
        elif asklegendint22==2:
            print(list_22[1])

    elif inputjersey==23:
        list_23=["LeBron James", "Michael Jordan"]
        asklegendint23=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint23==1:
            print(list_23[0])
        elif asklegendint23==2:
            print(list_23[1])

    elif inputjersey==24:
        list_24=["Buddy Hield", "Kobe Bryant"]
        asklegendint24=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint24==1:
            print(list_24[0])
        elif asklegendint24==2:
            print(list_24[1])

    elif inputjersey==25:
        list_25=["Ben Simmons", "Chet Walker"]
        asklegendint25=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint25==1:
            print(list_25[0])
        elif asklegendint25==2:
            print(list_25[1])

    elif inputjersey==26:
        list_26=["Kyle Korver", "James Robinson"]
        asklegendint26=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint26==1:
            print(list_26[0])
        elif asklegendint26==2:
            print(list_26[1])

    elif inputjersey==27:
        list_27=["Jamal Murray", "Jack Twyman"]
        asklegendint27=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint27==1:
            print(list_27[0])
        elif asklegendint27==2:
            print(list_27[1])

    elif inputjersey==28:
        list_28=["Andre Iguodala", "Andrew Lang"]
        asklegendint28=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint28==1:
            print(list_28[0])
        elif asklegendint28==2:
            print(list_28[1])

    elif inputjersey==29:
        list_29=["No Current Player Wears #29", "Paul Silas"]
        asklegendint29=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint29==1:
            print(list_29[0])
        elif asklegendint29==2:
            print(list_29[1])

    elif inputjersey==30:
        list_30=["Stephen Curry", "George McGinnis"]
        asklegendint30=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint30==1:
            print(list_30[0])
        elif asklegendint30==2:
            print(list_30[1])

    elif inputjersey==31:
        list_31=["Marcus Morris", "Reggie Miller"]
        asklegendint31=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint31==1:
            print(list_31[0])
        elif asklegendint31==2:
            print(list_31[1])

    elif inputjersey==32:
        list_32=["Karl-Anthony Towns", "Magic Johnson"]
        asklegendint32=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint32==1:
            print(list_32[0])
        elif asklegendint32==2:
            print(list_32[1])

    elif inputjersey==33:
        list_33=["Marc Gasol", "Kareem Abdul-Jabbar"]
        asklegendint33=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint33==1:
            print(list_33[0])
        elif asklegendint33==2:
            print(list_33[1])

    elif inputjersey==34:
        list_34=["Giannis Antetokounmpo", "Shaquille O'Neal"]
        asklegendint34=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint34==1:
            print(list_34[0])
        elif asklegendint34==2:
            print(list_34[1])

    elif inputjersey==35:
        list_35=["Marvin Bagley III", "Roger Brown"]
        asklegendint35=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint35==1:
            print(list_35[0])
        elif asklegendint35==2:
            print(list_35[1])

    elif inputjersey==36:
        list_36=["Marcus Smart", "Rasheed Wallace"]
        asklegendint36=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint36==1:
            print(list_36[0])
        elif asklegendint36==2:
            print(list_36[1])

    elif inputjersey==37:
        list_37=["Kostas Antetokounmpo", "Derek Fisher"]
        asklegendint37=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint37==1:
            print(list_37[0])
        elif asklegendint37==2:
            print(list_37[1])

    elif inputjersey==38:
        list_38=["No Current Player Wears #38", "Anthony Cook"]
        asklegendint38=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint38==1:
            print(list_38[0])
        elif asklegendint38==2:
            print(list_38[1])

    elif inputjersey==39:
        list_39=["Dwight Howard", "Caldwell Jones"]
        asklegendint39=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint39==1:
            print(list_39[0])
        elif asklegendint39==2:
            print(list_39[1])

    elif inputjersey==40:
        list_40=["Harrison Barnes", "Shawn Kemp"]
        asklegendint40=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint40==1:
            print(list_40[0])
        elif asklegendint40==2:
            print(list_40[1])

    elif inputjersey==41:
        list_41=["Juan Hernangomez", "Dirk Nowitzki"]
        asklegendint41=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint41==1:
            print(list_41[0])
        elif asklegendint41==2:
            print(list_41[1])

    elif inputjersey==42:
        list_42=["Al Horford", "Nate Thurmond"]
        asklegendint42=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint42==1:
            print(list_42[0])
        elif asklegendint42==2:
            print(list_42[1])

    elif inputjersey==43:
        list_43=["Pascal Siakam", "Jack Sikma"]
        asklegendint43=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint43==1:
            print(list_43[0])
        elif asklegendint43==2:
            print(list_43[1])

    elif inputjersey==44:
        list_44=["Bojan Bogdanovic", "Jerry West"]
        asklegendint44=int(input("Would you like to know a current player, or a retired legend? Press 1 for current player or 2 for retired legend "))
        if asklegendint44==1:
            print(list_44[0])
        elif asklegendint44==2:
            print(list_44[1])





    

    





    


def code():
    asker = int(input("this is a sports calculator. Enter 1 for baseball, 2 for football, and 3 for basketball "))
    if asker==1:
        baseball_choice=int(input("Ok. you chose baseball. Press 1 to calculate batting average, press 2 to find on base percentage, press 3 to calculate slugging percentage, or press 4 to find on-base percentage plus slugging average "))
        if baseball_choice==1:
            average()
            runagain=(input("want to calculate again? press y for yes or n for no "))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")

        elif baseball_choice==2:
            onbaseperc()
            runagain1=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain1=="y":
                    code()
                if runagain1=="n":
                    print("thanks for using!")
            except:
                print("invalid input")

        elif baseball_choice==3:
            slugging()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")

        elif baseball_choice==4:
            ops()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                    print("invalid input")
    elif asker==2:
        football_choice=int(input("Ok. you chose football. Enter 1 for completion percentage, enter 2 for yards per completion, enter 3 for yards per pass attempt, enter 4 for yards per rush, or enter 5 for field goal percentage "))
        if football_choice==1:
            passperc()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")
        elif football_choice==2:
            yards_compl()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")
        elif football_choice==3:
            yardsperattempt()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")
        elif football_choice==4:
            yardsrush()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")
        elif football_choice==5:
            fieldgoal()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")
    elif asker==3:
        basketball_choice=int(input("Ok. You chose basketball. Press 1 to see if you got a triple double, press 2 too calculate your shooting percentage, or press 3 to find the best players ever for every jersey number "))
        if basketball_choice==1:
            tripledouble()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")
        elif basketball_choice==2:
            shotperc()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")
        elif basketball_choice==3:
            jerseynumber()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            try:    
                if runagain=="y":
                    code()
                if runagain=="n":
                    print("thanks for using!")
            except:
                print("invalid input")


    else:
        print("Invalid input")





            



code()