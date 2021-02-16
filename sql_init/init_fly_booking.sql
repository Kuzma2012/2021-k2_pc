CREATE TABLE fly_booking (
	Booking_Id serial PRIMARY KEY,
	Client_Name VARCHAR (50) NOT NULL,
	Fly_Number VARCHAR (50) NOT NULL,
	Fly_From VARCHAR (3) NOT NULL,
	Fly_To VARCHAR (3) NOT NULL,
	Fly_Date DATE NOT NULL 
);

INSERT INTO fly_booking (Booking_Id, Client_Name, Fly_Number, Fly_From, Fly_To, Fly_Date) VALUES 
(1,'Nik', 'KLM 1382', 'KBP', 'AMS','01/05/2015')