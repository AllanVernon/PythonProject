class Batsman:
    def __init__(self):
        self.name = ""
        self.runs = 0
        self.balls = 0
        self.ones = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.sixes = 0
        self.str = 0.0

class Bowler:
    def __init__(self):
        self.name = ""
        self.runsgv = 0
        self.overs = 0
        self.wkttkn = 0
        self.econ = 0.0

def main():
    pl1 = [Batsman() for _ in range(100)]
    pl2 = [Bowler() for _ in range(100)]
    pl3 = Batsman()
    pl4 = Bowler()

    m = int(input("Enter the number of batsmen: "))
    for i in range(m):
        pl1[i].name = input(f"Enter name of batsman {i+1}: ")
        pl1[i].ones = int(input(f"Enter the number of ones scored by {pl1[i].name}: "))
        pl1[i].twos = int(input(f"Enter the number of twos scored by {pl1[i].name}: "))
        pl1[i].threes = int(input(f"Enter the number of threes scored by {pl1[i].name}: "))
        pl1[i].fours = int(input(f"Enter the number of fours scored by {pl1[i].name}: "))
        pl1[i].sixes = int(input(f"Enter the number of sixes scored by {pl1[i].name}: "))
        pl1[i].balls = int(input(f"Enter the balls played by {pl1[i].name}: "))

    n = int(input("Enter the number of bowlers: "))
    for i in range(n):
        pl2[i].name = input(f"Enter name of bowler {i+1}: ")
        pl2[i].runsgv = int(input(f"Enter the runs given by {pl2[i].name}: "))
        pl2[i].overs = int(input(f"Enter the overs bowled by {pl2[i].name}: "))
        pl2[i].wkttkn = int(input(f"Enter the wickets taken by {pl2[i].name}: "))

    print("Thank you, all details are recorded.")

    while True:
        print("Enter the choice:")
        print("1) Batsman detail")
        print("2) Bowlers detail")
        print("3) Match summary")
        print("4) Record")
        print("5) Exit")
        choice = int(input())

        if choice == 1:
            plno = int(input("Enter the batsman number to see the details: "))
            plno -= 1
            print("Player Detail")
            print("=" * 75)
            print("{:<15} {:<14} {:<13} {:<11} {:<11} {:<9}".format("Batsman", "runs", "balls", "fours", "sixes", "sr"))
            print("=" * 75)

            pl1[plno].runs = (1 * pl1[plno].ones) + (2 * pl1[plno].twos) + (3 * pl1[plno].threes) + (4 * pl1[plno].fours) + (6 * pl1[plno].sixes)
            pl1[plno].str = (pl1[plno].runs * 100.00) / pl1[plno].balls
            print("{:<15} {:<14} {:<13} {:<11} {:<11} {:<9.2f}".format(pl1[plno].name, pl1[plno].runs, pl1[plno].balls, pl1[plno].fours, pl1[plno].sixes, pl1[plno].str))

        elif choice == 2:
            plno = int(input("Enter the bowler number to see the details: "))
            plno -= 1
            print("Player Detail")
            print("=" * 60)
            print("{:<15} {:<14} {:<13} {:<11} {:<11}".format("Bowler", "overs", "runs", "wicket", "economy"))
            print("=" * 60)

            pl2[plno].econ = pl2[plno].runsgv / pl2[plno].overs
            print("{:<15} {:<14} {:<13} {:<11} {:<11.2f}".format(pl2[plno].name, pl2[plno].overs, pl2[plno].runsgv, pl2[plno].wkttkn, pl2[plno].econ))

        elif choice == 3:
            print("Match summary")
            print("=" * 75)
            print("{:<15} {:<14} {:<13} {:<11} {:<11} {:<9}".format("Batsman", "runs", "balls", "fours", "sixes", "sr"))
            print("=" * 75)

            for i in range(m):
                pl1[i].runs = (1 * pl1[i].ones) + (2 * pl1[i].twos) + (3 * pl1[i].threes) + (4 * pl1[i].fours) + (6 * pl1[i].sixes)
                pl3.runs += pl1[i].runs
                pl1[i].str = (pl1[i].runs * 100.00) / pl1[i].balls
                print("{:<15} {:<14} {:<13} {:<11} {:<11} {:<9.2f}".format(pl1[i].name, pl1[i].runs, pl1[i].balls, pl1[i].fours, pl1[i].sixes, pl1[i].str))
            print("TOTAL RUNS: {}\n".format(pl3.runs))
            print("=" * 60)
            print("{:<15} {:<14} {:<13} {:<11} {:<11}".format("Bowler", "overs", "runs", "wicket", "economy"))
            print("=" * 60)
            for i in range(n):
                pl2[i].econ = pl2[i].runsgv / pl2[i].overs
                print("{:<15} {:<14} {:<13} {:<11} {:<11.2f}".format(pl2[i].name, pl2[i].overs, pl2[i].runsgv, pl2[i].wkttkn, pl2[i].econ))
        
        elif choice == 4:
            # Initialize variables to store player statistics
            pl3.max_run = 0
            pl3.max_four = 0
            pl3.max_six = 0
            pl4.max_w = 0
            best_batsman = ""
            best_bowler = ""

            # Calculate maximum runs, fours, and sixes for batsmen
            for i in range(m):
                pl1[i].runs = (1 * pl1[i].ones) + (2 * pl1[i].twos) + (3 * pl1[i].threes) + (4 * pl1[i].fours) + (6 * pl1[i].sixes)

                if pl1[i].runs > pl3.max_run:
                    pl3.max_run = pl1[i].runs
                    best_batsman = pl1[i].name

                if pl1[i].fours > pl3.max_four:
                    pl3.max_four = pl1[i].fours

                if pl1[i].sixes > pl3.max_six:
                    pl3.max_six = pl1[i].sixes

            # Calculate the maximum wickets and economy for bowlers
            for i in range(n):
                if pl2[i].wkttkn > pl4.max_w:
                    pl4.max_w = pl2[i].wkttkn
                    best_bowler = pl2[i].name

            # Display the best batsman and bowler
            print("Best Batsman: {}, Max Runs: {}".format(best_batsman, pl3.max_run))
            print("Best Bowler: {}, Max Wickets: {}".format(best_bowler, pl4.max_w))

        elif choice == 5:
            # Exit the program
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
