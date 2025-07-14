
def movie_ticket():
    seat = []
    user_info = []
    print("Wecome! to our movie Theatre 🤩\n")
    
    name = input("Enter your Name : ")
    phone_numebr = int(input("Enter your mobile number : "))
    payment_method = input("Select your payment method : Cash / Card / UPI  ")
    booked_movie= ""
    timing = ""
    def add_seats():
        global select_timing
        global seat_number
        age_check = int(input("Enter your age : "))
        if age_check <= 3 :
            print("ticket are not need \n")
            return
        else:
            pass
        seat_number = input("Enter the seat number : ")
        if seat_number in seat:
            print("\nSorry the seat are already booked..Try another seat\n")
        else:
            seat.append(seat_number)
            print("\nYour seat booking is : " , seat_number)
    def premium_seat():
        print("\nBest choicee for movie experience 😎\n")
        premium_seat_number = input("Enter the seat number : ☐☐☐☐☐☐☐☐☐")
    def movie_list():
        global search
        global select_timing 
        movies = ['Housefull 5', 'Jaran', 'Dragon']
        print("\n 1. Housefull 5 🌟 6.2 \n 2. Jaran (Marathi) 🌟 7.6 \n 3. Dragon (English) 🌟 9.2 \n")

        search = input("Enter the movie name: ")
        if search in movies:
            print("\nMovie:", search)
            print("\nBook your seat for movie:", search)

            show_timing = [6, 9, 12]
            print("\nAvailable show timings:", show_timing)
            select_timing = int(input("Select show time: "))

            print(f"\nYour show timing is: {select_timing} PM")
            add_seats()
        else:
            print("\nThe movie is not available....") 

    def ticket_print():
        print("\n........Your Ticket..........")
        print("Name : ",name )
        print("Movie name :" , search)
        print(f"Show Timing : {select_timing} PM"  )
        print(f"Your seat no .. {seat_number}")
        print("Price : 300")
        print("...............................")

    def main_():
        while True :
            print("\n What you want Today ...\n 1. book your seat \n 2.book your premium seat\n Do you want a ticket print yes / no ?\n 4.Exit ")
            print("\nThe price are shown below:  \n\n For normal seat 300 Rs \n For premium 800 Rs per seat\n No ticket required under 3 age\n ")
            choice = input("Enter choice : ")
            



            if choice == '1':
                movie_list()
            elif choice == '2':
                premium_seat()
            elif choice == "yes":
                ticket_print()
                break
            elif choice == '4':
                print("Come back again.....")
                break
            else:
                print("Enter valid stetament")
      
    main_()
movie_ticket()

    
    