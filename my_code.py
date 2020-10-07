# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://www.baseball-reference.com/bullpen/Baseball_statistics for all the stats
# Megan helped and gave feedback
# football stats https://simulatedfootball.com/tools/points-calculator.html

def average():
        avg_hits=int(input("enter the amount of hits you had "))
        avg_atbats=int(input("enter the amount of plate appearances you had "))
        finalavg=float(avg_hits/avg_atbats)
        avg_list = [f"{avg_hits} / {avg_atbats}"]
        for x in avg_list:
            print(x)
        print(f"your batting average is {finalavg}")

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

def yards_compl():
    completions=int(input("How many passes did you complete? "))
    yards=int(input("How many total yards passing do you have? "))
    finalyardcomp=float(yards / completions)
    completionlist={f"{yards} / {completions} = {finalyardcomp}"}
    for x in completionlist:
        print(x)
    print (f"you average {finalyardcomp} yards per completion")

def yardsperattempt():
    attempts=int(input("How many times did you attempt to throw the ball? "))
    yards2=int(input("How many total yards passing do you have? "))
    finalyrdatt=float(yards2 / attempts)
    list_attemptyard={f"{yards2} / {attempts} = {finalyrdatt}"}
    for x in list_attemptyard:
        print(x)
    print (f"you average {finalyrdatt} yards per attempt")

def yardsrush():
    rushattempts=int(input("How many times did you attempt to run the ball? "))
    yards3=int(input("How many total yards passing do you have? "))
    finalrun=float(yards3 / rushattempts)
    list_attemptyard={f"{yards3} / {rushattempts} = {finalrun}"}
    for x in list_attemptyard:
        print(x)
    print (f"you average {finalrun} yards per run")

def fieldgoal():
    fg_attempt=int(input("How many times did you attempt a field goal? "))
    fg_made=int(input("How many times did you make a field goal? "))
    final_fg_perc=float(fg_made / fg_attempt)
    total_fgpoints=float(fg_made*3)
    list_fg={f"{fg_made} / {fg_attempt} = {final_fg_perc}"}
    for x in list_fg:
        print(x)
    print (f"your field goal percentage is {final_fg_perc} and in total, you got {total_fgpoints} points")

def tripledouble():
    td_points=int(input("How many points did you score? "))
    td_rebs=int(input("How many rebounds did you get? "))
    td_assists=int(input("How many assists did you get? "))
    td_steals=int(input("How many steals did you get? "))
    td_blocks=int(input("How many times did you block a shot? "))
    if td_points>=10 and td_rebs>=10 and td_assists>=10:
        print ("You got a triple double!")
    if td_points>=10 and td_steals>=10 and td_blocks>=10:
        print ("You got a triple double!")
    if td_rebs>=10 and td_assists>=10 and td_steals>=10:
        print ("You got a triple double!")
    if td_rebs>=10 and td_blocks>=10 and td_points>=10:
        print ("You got a triple double!")
    if td_assists>=10 and td_steals>=10 and td_blocks>=10:
        print ("You got a triple double!")
    if td_assists>=10 and td_points>=10 and td_blocks>=10:
        print ("You got a triple double!")
    if td_steals>=10 and td_blocks>=10 and td_points>=10:
        print ("You got a triple double!")
    if td_steals>=10 and td_assists>=10 and td_points>=10:
        print ("You got a triple double!")
    if td_steals>=10 and td_assists>=10 and td_rebs>=10:
        print ("You got a triple double!")
    if td_blocks>=10 and td_points>=10 and td_rebs>=10:
        print ("You got a triple double!")
    if td_blocks>=10 and td_assists>=10 and td_steals>=10:
        print ("You got a triple double!")
    if td_blocks>=10 and td_assists>=10 and td_steals>=10 and td_points>=10 and td_rebs=>10:
        print ("You got a triple double!")
    if td_blocks>=10 and td_assists>=10 and td_steals>=10 and td_points>=10:
        print ("You got a triple double!")
    if td_blocks>=10 and td_assists>=10 and td_steals>=10 and td_rebs=>10:
        print ("You got a triple double!")
    if td_blocks>=10 and td_assists>=10 and td_points>=10 and td_rebs=>10:
        print ("You got a triple double!")
    if td_blocks>=10 and td_steals>=10 and td_points>=10 and td_rebs=>10:
        print ("You got a triple double!")
    if td_assists>=10 and td_steals>=10 and td_points>=10 and td_rebs=>10:
        print ("You got a triple double!")
    '''else:
        print("You did not get a triple double")'''
        
        
        

        
        



def code():
    asker = int(input("this is a sports calculator. Enter 1 for baseball, 2 for football, and 3 for basketball "))
    if asker==1:
        baseball_choice=int(input("Ok. you chose baseball. Press 1 to calculate batting average, press 2 to find on base percentage, press 3 to calculate slugging percentage, or press 4 to find on-base percentage plus slugging average "))
        if baseball_choice==1:
            average()
            runagain=(input("want to calculate again? press y for yes or n for no "))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")

        if baseball_choice==2:
            onbaseperc()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")

        if baseball_choice==3:
            slugging()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")

        if baseball_choice==4:
            ops()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")
    if asker==2:
        football_choice=int(input("Ok. you chose football. Enter 1 for completion percentage, enter 2 for yards per completion, enter 3 for yards per pass attempt, enter 4 for yards per rush, or enter 5 for field goal percentage "))
        if football_choice==1:
            passperc()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")
        if football_choice==2:
            yards_compl()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")
        if football_choice==3:
            yardsperattempt()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")
        if football_choice==4:
            yardsrush()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")
        if football_choice==5:
            fieldgoal()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")
    if asker==3:
        basketball_choice=int(input("Ok. You chose basketball. Press 1 to see if you got a triple double, press 2 too calculate your shooting percentage, or press 3 to compare your jersey number to the best who ever wore it "))
        if basketball_choice==1:
            tripledouble()
            runagain=(str(input("want to calculate again? press y for yes or n for no ")))
            if runagain=="y":
                code()
            if runagain=="n":
                print("thanks for using!")
            else:
                print("invalid input")



            



code()