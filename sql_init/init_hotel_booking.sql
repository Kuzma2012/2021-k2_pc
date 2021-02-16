CREATE TABLE hotel_booking (
	Booking_Id serial PRIMARY KEY,
	Client_Name VARCHAR (50) NOT NULL,
	Hotel_Name VARCHAR (50) NOT NULL,
	Arrival DATE NOT NULL ,
	Departure DATE NOT NULL
);

INSERT INTO hotel_booking (Booking_Id,	Client_Name, Hotel_Name, Arrival, Departure) VALUES 
(1,'Nik', 'Hilton', '01/05/2015', '07/05/2015')