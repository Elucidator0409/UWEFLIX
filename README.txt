Terminal in order

cd UWEFLIX-main
cd uwe_flix
activate venv
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

create an admin account:
python manage.py createsuperuser

Adding Movie on Website:
access admin page
add a movie
add shows
add seat

Reminders: Make sure that the dates on MOVIE, SHOWS and SEAT are up to date.


TO ACCESS MAIN WEBSITE:
python manage.py runserver

How to book a ticket:
Login or Create an Account
Click Booking
Choose a Film
Click Showing Times
Select Seat

Regular Seats (1,2,3)
Deluxe Seats (4,5,6)
VIP Seats (7,8)
Click Confirm

Click Pay
Paypal Checkout

ticket will be stored at booking/booked seat database.

