def seat_booking(booked_seats,seat_no):
    if(seat_no in booked_seats):
        print("Seat alerady booked.")
        return
    else:
        booked_seats.append(seat_no)
        print("Seat booked Successfully.")
def seat_cancellation(booked_seats,seat_no):
    if(seat_no in booked_seats):
        booked_seats.remove(seat_no)
        print("Seat cancellation done successfully.")
    else:
        print("Seat not yet allocated so cannot be cancelled.")
        return
def display_seats(total_seats_list,booked_seats):
    available=[]
    for seat_no in total_seats_list:
        if seat_no not in booked_seats:
            available.append(seat_no)
    print("Available Seats: ",available)
total_seats=int(input("Enter total number of seats : "))
total_seats_list=[x for x in range(1,total_seats+1)]
booked_seats=eval(input("Enter the booked seats : "))
while True:
    print("Menu\n1.Book a seat\n2.Cancel a seat\n3.Display Available seats\n4.Exit")
    try:
        ch=int(input("Enter your choice : "))
    except ValueError:
        print("Enter the integer value.")
        exit(1)
    if(ch<1 or ch>4):
        print("Please enter valid option between 1 and 4")
        exit(1)
    else:
        if(ch==1):
            seat_no=int(input("Enter seat number to be booked : "))
            seat_booking(booked_seats,seat_no)
        elif(ch==2):
            seat_no=int(input("Enter seat number to be cancelled : "))
            seat_cancellation(booked_seats,seat_no)
        elif(ch==3):
            display_seats(total_seats_list,booked_seats)
        elif(ch==4):
            print("Enjoy your movie.")
            exit(1)