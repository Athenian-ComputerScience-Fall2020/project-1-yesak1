# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  https://www.baseball-reference.com/bullpen/Baseball_statistics for all the stats
# Megan helped and gave feedback

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




def code():
    asker = int(input("this is a sports calculator. Enter 1 for baseball, 2 for basketball, and 3 for football "))
    if asker==1:
        baseball_choice=int(input("Ok. you chose baseball. Press 1 to calculate batting average, press 2 to find on base percentage, press 3 to calculate slugging percentage, or press 4 to find on-base percentage plus slugging average "))
    if baseball_choice==1:
        average()
        runagain=(input("want to calculate again? press y for yes or n for no "))
        if runagain=="y":
            code()
        if runagain=="n":
            print("thanks for using!")
    if baseball_choice==2:
        onbaseperc()
        runagain=(str(input("want to calculate again? press y for yes or n for no ")))
        if runagain=="y":
            code()
        if runagain=="n":
            print("thanks for using!")
    if baseball_choice==3:
        slugging()
        runagain=(str(input("want to calculate again? press y for yes or n for no ")))
        if runagain=="y":
            code()
        if runagain=="n":
            print("thanks for using!")
    if baseball_choice==4:
        ops()
        runagain=(str(input("want to calculate again? press y for yes or n for no ")))
        if runagain=="y":
            code()
        if runagain=="n":
            print("thanks for using!")
    

        

code()
        

    
    