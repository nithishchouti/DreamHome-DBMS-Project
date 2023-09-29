show databases;
create database DreamHome;
use DreamHome;
show tables;

create table Staff(
					StaffId int UNIQUE not NULL,
					StaffFName varchar(15),
					StaffMName varchar(15),
                    StaffLName varchar(15),
                    Sex char(1),
                    Position char(1), -- this can be 'a'(assistant), 's'(supervisor) and 'm'(manager)--
                    Salary int,
                    BranchId int,
                    SuperId int,
                    Startdate date,
                    Bonus int -- bonus here refers to signing bonus
                    );
                    
-- this table keeps staff telephones, separate table was created since
-- a single employee can have more than one phone number
create table StaffTelephone(
							StaffId int Not Null,
                            StaffNumber int
							);
             drop table branch;               
create table Branch(
					BranchId int Unique not null,
                    managerId int unique,
                    locality varchar(40),
                    city varchar(20),
                    state varchar(20),
                    country varchar(20) -- the last four attributes combine to form address
					);

create table BranchTelephone(
							BranchId int Not Null,
                            BranchNumber char(10)
							);

create table owner(
					ownerId int unique not null,
                    Name varchar(40), -- this can be person's name or a business
                    locality varchar(40),
                    city varchar(20),
                    state varchar(20),
                    country varchar(20) -- the last four attributes combine to form address
					);
     drop table ownertelephone;
create table ownerTelephone(
							ownerId int unique Not Null,
                            ownerNumber char(10) unique -- two numbers cannot be the same
							);
show tables;

create table registration(ClientId int not null,
							BranchId int not null,
                            StaffId int,
                            DateJoined date
                            );
    drop table properties;                   
create table Properties(
						PropertyId int unique not null,
                        Type varchar(30),
                        NumOfRooms int,
                        Rent int,
                        locality varchar(40),
						city varchar(20),
						state varchar(20),
						country varchar(20), -- the last four attributes combine to form address
                        ownerId int,
                        RegisteredAtBranchId int,
                        ManagingStaffId int,
                        TypeOfBusiness varchar(30), -- can be private or any other busines
						contactName varchar(45), -- name of person to contact at this business
                        Availability char(1), -- can only be true(t) or false(f)
                        depositRequired int
						);
                   
create table Client (
					ClientId int unique not null,
                    clientFname varchar(15),
                    clientMname varchar(10),
                    clientLname varchar(20),
                    RegisteredAtBranchId int, 
                    RegisteredByStaffId int,
                    DateofRegistrattion date,
                    TypeWanted varchar(30), -- type of apartment wanted, flat bungalow etc
                    MaxRent int
					);

drop table clientTelephone;
create table clientTelephone(
							clientId int Not Null,
                            clientNumber char(10) unique -- two numbers cannot be the same
							);	

show tables;
create table propertyview(
							propertyid int not null,
							clientid int,
							DateofVisit date,
							comments TEXT
							);
drop table leaseAgreement;
create table LeaseAgreement(
							LeaseId int unique not null,
							clientid int not null,
                            propertyId int,
                            MonthlyRent int,
                            paymentmethod varchar(25),
                            deposit char(1), -- can only be true(t) or false(f)
							RentStartDate date,
                            RentEndDate date
							);

show tables;
select * from owner;
-- inserting into owner
INSERT INTO `dreamhome`.`owner` (`ownerId`, `Name`, `locality`, `city`, `state`, `country`) VALUES ('1', 'Shaikh', 'H no 3 Ittigatti', 'Hubli', 'Karnataka', 'India');
INSERT INTO `dreamhome`.`owner` (`ownerId`, `Name`, `locality`, `city`, `state`, `country`) VALUES ('2', 'Shri Balaji Builders', 'HNo 10 Richie Rich Colony', 'PavBhajiNagar', 'Maharashtra', 'India');
INSERT INTO `dreamhome`.`owner` (`ownerId`, `Name`, `locality`, `city`, `state`, `country`) VALUES ('3', 'Nithish', 'H no 3 Ittigatti', 'Hubli', 'Karnataka', 'India');
-- inserting into staff
INSERT INTO `dreamhome`.`staff` (`StaffId`, `StaffFName`, `StaffLName`, `Sex`, `Position`, `Salary`, `BranchId`, `SuperId`, `Startdate`, `Bonus`) VALUES ('1', 'Uday', 'Teja', 'M', 'S', '9000', '1', '3', '2023-01-01', '0');
INSERT INTO `dreamhome`.`staff` (`StaffId`, `StaffFName`, `StaffMName`, `StaffLName`, `Sex`, `Position`, `Salary`, `BranchId`, `SuperId`, `Startdate`, `Bonus`) VALUES ('2', 'Rahul', 'S', 'Narkedimilli ', 'M', 'A', '5800', '1', '1', '2023-02-01', '0');
INSERT INTO `dreamhome`.`staff` (`StaffId`, `StaffFName`, `StaffMName`, `StaffLName`, `Sex`, `Position`, `Salary`, `BranchId`, `Startdate`, `Bonus`) VALUES ('3', 'Goyal', 'Ram', 'Ratan', 'M', 'M', '14000', '1', '2022-12-01', '3000');
INSERT INTO `dreamhome`.`staff` (`StaffId`, `StaffFName`, `StaffMName`, `StaffLName`, `Sex`, `Position`, `Salary`, `BranchId`, `Startdate`, `Bonus`) VALUES ('4', 'Shriya', 'S', 'Patare', 'F', 'M', '15000', '2', '2022-12-01', '3200');
INSERT INTO `dreamhome`.`staff` (`StaffId`, `StaffFName`, `StaffMName`, `StaffLName`, `Sex`, `Position`, `Salary`, `BranchId`, `SuperId`, `Startdate`, `Bonus`) VALUES ('5', 'Likith', 'R', 'Verma', 'M', 'A', '6300', '2', '6', '2023-02-01', '0');
INSERT INTO `dreamhome`.`staff` (`StaffId`, `StaffFName`, `StaffMName`, `StaffLName`, `Sex`, `Position`, `Salary`, `BranchId`, `SuperId`, `Startdate`, `Bonus`) VALUES ('6', 'Pranay', 'C', 'Karthik', 'M', 'S', '11000', '2', '4', '2023-01-01', '2200');
-- inserting into branch
INSERT INTO `dreamhome`.`branch` (`BranchId`, `managerId`, `locality`, `city`, `state`, `country`) VALUES ('1', '3', 'Dreamhome Building Ittigatti', 'Hubli', 'Karnataka', 'India');
INSERT INTO `dreamhome`.`branch` (`BranchId`, `managerId`, `locality`, `city`, `state`) VALUES ('2', '4', 'Dreamhome Building chatstore', 'PavbhajiNagar', 'Maharashtra');
-- inserting into branchtelephone
insert into branchtelephone values (1, '9113087495'), (2,'9890869839');
-- inserting into client
INSERT INTO `dreamhome`.`client` (`ClientId`, `clientFname`, `clientMname`, `clientLname`, `RegisteredAtBranchId`, `RegisteredByStaffId`, `DateofRegistrattion`, `TypeWanted`, `MaxRent`) VALUES ('1', 'Vipul', 'S', 'Bawankar', '2', '6', '2023-04-01', 'Flat', '9000');
INSERT INTO `dreamhome`.`client` (`ClientId`, `clientFname`, `clientMname`, `clientLname`, `RegisteredAtBranchId`, `RegisteredByStaffId`, `DateofRegistrattion`, `TypeWanted`, `MaxRent`) VALUES ('2', 'Aman', 'A', 'Gupta', '2', '5', '2023-04-02', 'Flat', '8500');
INSERT INTO `dreamhome`.`client` (`ClientId`, `clientFname`, `clientMname`, `clientLname`, `RegisteredAtBranchId`, `RegisteredByStaffId`, `DateofRegistrattion`, `TypeWanted`, `MaxRent`) VALUES ('3', 'Salman', 'Khursheed', 'Khan', '1', '2', '2023-04-01', 'Bungalow', '40000');
INSERT INTO `dreamhome`.`client` (`ClientId`, `clientFname`, `clientMname`, `clientLname`, `RegisteredAtBranchId`, `RegisteredByStaffId`, `DateofRegistrattion`, `TypeWanted`, `MaxRent`) VALUES ('4', 'Rakesh', 'C', 'Agrawal', '2', '4', '2023-04-04', 'Flat', '9800');
INSERT INTO `dreamhome`.`client` (`ClientId`, `clientFname`, `clientLname`, `RegisteredAtBranchId`, `RegisteredByStaffId`, `DateofRegistrattion`, `TypeWanted`, `MaxRent`) VALUES ('5', 'Aliya', 'Birla', '1', '2', '2023-04-09', 'Bungalow', '65000');
INSERT INTO `dreamhome`.`client` (`ClientId`, `clientFname`, `clientMname`, `clientLname`, `RegisteredAtBranchId`, `RegisteredByStaffId`, `DateofRegistrattion`, `TypeWanted`, `MaxRent`) VALUES ('6', 'Wilma', 'B', 'James', '2', '5', '2023-04-11', 'Flat', '10000');
-- inserting into properties
INSERT INTO `dreamhome`.`properties` (`PropertyId`, `Type`, `NumOfRooms`, `Rent`, `locality`, `city`, `state`, `country`, `ownerId`, `RegisteredAtBranchId`, `ManagingStaffId`, `TypeOfBusiness`, `contactName`, `availability`, `depositRequired`) VALUES ('1', 'Bungalow', '14', '45000', 'The Bungalow Rich Colony', 'PavbhajiNagar', 'Maharastra', 'India', '2', '2', '4', 'Real Estate Developers', 'NotSangram', 'T', 100000);
INSERT INTO `dreamhome`.`properties` (`PropertyId`, `Type`, `NumOfRooms`, `Rent`, `locality`, `city`, `state`, `country`, `ownerId`, `RegisteredAtBranchId`, `ManagingStaffId`, `TypeOfBusiness`, `contactName`,`availability`, `depositRequired`) VALUES ('2', 'Flat', '2', '9000', 'Flat 256 Near Chatstore', 'PavbhajiNagar', 'Maharashtra', 'India', '2', '2', '6', 'Real Estate Developers', 'NotSangram', 'F', 10000);
INSERT INTO `dreamhome`.`properties` (`PropertyId`, `Type`, `NumOfRooms`, `Rent`, `locality`, `city`, `state`, `country`, `ownerId`, `RegisteredAtBranchId`, `ManagingStaffId`, `TypeOfBusiness`, `contactName`,`availability`, `depositRequired`) VALUES ('3', 'Flat', '3', '1100', 'Flat 12 Near Ittigatti', 'Hubli', 'Karnataka', 'India', '1', '1', '1', 'Private', 'Shaikh', 'T', 11000);
INSERT INTO `dreamhome`.`properties` (`PropertyId`, `Type`, `NumOfRooms`, `Rent`, `locality`, `city`, `state`, `country`, `ownerId`, `RegisteredAtBranchId`, `ManagingStaffId`, `TypeOfBusiness`, `contactName`,`availability`, `depositRequired`) VALUES ('4', 'Flat', '1', '6000', 'Flat', 'Hubli', 'Karnataka', 'India', '3', '1', '3', 'Private', 'Nithish', 'F', 14000);
-- inserting into propertyview
INSERT INTO `dreamhome`.`propertyview` (`propertyid`, `clientid`, `DateofVisit`, `comments`) VALUES ('2', '2', '2023-03-01', 'Needs to be better furnished');
INSERT INTO `dreamhome`.`propertyview` (`propertyid`, `clientid`, `DateofVisit`, `comments`) VALUES ('1', '5', '2023-03-10', 'Loved the place, is looking to place a bid');
INSERT INTO `dreamhome`.`propertyview` (`propertyid`, `clientid`, `DateofVisit`, `comments`) VALUES ('2', '4', '2023-03-11', 'Thought the price was too high, but liked the place.');
INSERT INTO `dreamhome`.`propertyview` (`propertyid`, `clientid`, `DateofVisit`, `comments`) VALUES ('4', '2', '2023-03-02', 'Liked the place and want to bid on it');
-- insreting into clientTelephon
insert into clienttelephone values( 2, '9113087595'), (2, '8989898989'), (4, '2342342344'),(4, '2345623456');


-- Creation of all primary keys
Alter table Staff
add constraint pk_staff 
Primary key Staff(StaffId);

Alter table Branch
Add constraint pk_branch
primary key Branch(BranchId);

Alter Table client
Add constraint pk_client
primary key client(clientId);

Alter table StaffTelephone
Add constraint pk_StaffTelephone
primary key StaffTelephone(StaffId, StaffNumber);


Alter table Owner
Add constraint pk_owner
primary key Owner(OwnerId);

Alter table Registration
Add constraint pk_registration
primary key Registration(clientId);


Alter table BranchTelephone
Add constraint pk_BranchTelephone
primary key BranchId(BranchId, branchNumber);

Alter table ClientTelephone
Add constraint pk_StaffTelephone
primary key clientTelephone(clientId,clientNumber);

Alter table OwnerTelephone
Add constraint pk_OwneTelephone
primary key OwnerTelephone(OwnerId, OwnerNumber);

Alter table Properties
Add constraint pk_properties
primary key properties(PropertyId);

Alter table LeaseAgreement
Add constraint pk_leaseAgreement
primary key LeaseAgreement(LeaseId);

Alter table PropertyView
Add constraint pk_propertyView
primary key propertyView(propertyId, ClientId, DateOfVisit);

-- done with adding primary keys:


-- code for adding foreign key constraints
Alter table LeaseAgreement
Add constraint fk_propertyId
foreign key LeaseAgreement(PropertyId)
references Properties(propertyId);


Alter table LeaseAgreement
Add constraint fk_clientid
foreign key LeaseAgreement(clientid)
references client(clientid);


Alter table properties
Add constraint fk_ownerid
foreign key properties(ownerid)
references owner(ownerid);


Alter table properties
Add constraint fk_managingstaffid
foreign key properties(managingstaffid)
references Staff(StaffId);

Alter table propertyview
Add constraint fk_propertyviewpropertyId
foreign key propertyview(propertyId)
references properties(propertyid);

Alter table propertyview
Add constraint fk_propertviewclientid
foreign key propertyview(clientid)
references client(clientid);

Alter table OwnerTelephone
Add constraint fk_Ownertelephone
foreign key OwnerTelephone(ownerid)
references owner(ownerid);

Alter table Registration
Add constraint fk_registrationclientId
foreign key registration(clientid)
references client(clientid);

Alter table Registration
Add constraint fk_registrationBranchId
foreign key registration(Branchid)
references branch(branchid);

Alter table Registration
Add constraint fk_registrationclientId
foreign key registration(clientid)
references client(clientid);

Alter table Registration
Add constraint fk_registrationstaffid
foreign key registration(staffid)
references staff(staffid);

Alter table branchtelephone
Add constraint fk_branchtelephoneBranchId
foreign key branchtelephone(branchid)
references branch(Branchid);

Alter table StaffTelephone
Add constraint fk_StafftelephoneStaffId
foreign key StaffTelephone(StaffId)
references Staff(StaffiD);

Alter table Branch
Add constraint fk_branchmanagerId
foreign key Branch(managerid)
references Staff(staffid);

Alter table ClientTelephone
Add constraint fk_ClienttelephoneClientId
foreign key clientTelephone(clientId)
references client(clientid);


Alter table Client
Add constraint fk_clientRegisteredAtBranchId
foreign key client(RegisteredAtBranchId)
references branch(branchId);

Alter table client
add constraint fk_clientregisteredbyStaffId
foreign key client(registeredbyStaffId)
references staff(staffid);





select * from clienttelephone;

select * from staff;
drop database dreamhouse;
use dreamhome;
Alter table staff 
Add column(DOB date);
/*
Queries required by the Branch:
(a) List the details of branches in a given city.
(b) Identify the total number of branches in each city.
(c) List the name, position, and salary of staff at a given branch, ordered by staff name.
(d) Identify the total number of staff and the sum of their salaries.
(e) Identify the total number of staff in each position at branches in Glasgow.
(f) List the name of each Manager at each branch, ordered by branch address.
(g) List the names of staff supervised by a named Supervisor.
(h) List the property number, address, type, and rent of all properties in Glasgow, ordered by rental
amount.
*/
show tables;

-- a
select * from branch, branchtelephone 
where branch.branchid = branchtelephone.branchid and city = ('city name');

-- b
select city, count(BranchId) as numOfBranches
from branch
group by city;

-- c
select * from staff;
select concat_ws(' ',fname,lname), position, salary
from staff;

-- d
select count(staffid) as total_staff, sum(salary) as total_salary
from staff;

-- e
select * from branch;
select count(staffid), branchId
from staff where branchId = (select e.branchid from branch as e where city = "Hubli") -- or your city
group by branchid;

-- f
select managerId, branchid, city from branch 
order by locality, city, state, country;

-- g
select concat_ws(' ',StaffFname, staffMname, staffLname) 
from staff
where position = 'S' and superid is not NULL;

-- h List the property number, address, type, and rent of all properties in Glasgow, ordered by rental
-- amount.
select propertyId, type, NumOfRooms, rent,concat_ws(' ', locality, city, state, country) 
from properties
order by rent;

-- (i) List the details of properties for rent managed by a named member of staff.
select * from properties
where managingStaffId is not null;

-- (j) Identify the total number of properties assigned to each member of staff at a given branch.

select count(propertyId), ManagingStaffId
from properties
where managingSTaffid in (select staffid from staff where branchid = 2) -- your branch
group by ManagingStaffId;

-- (k) List the details of properties provided by business owners at a given branch.

select * from properties 
where RegisteredAtBranchId = 2; -- or your branches
	
-- (l) Identify the total number of properties of each type at all branches. !!!THIS DOESN'T WORK
select count(propertyId), type from properties 
group by type, propertyId;
select * from owner;
-- (m) Identify the details of private property owners that provide more than one property for rent.
select * from properties
where TypeOfbusiness = 'Private' and ownerId in (select ownerid from properties
													group by ownerid
												having count(ownerid)>1);

-- (n) Identify flats with at least three rooms and with a monthly rent no higher than £500 in Aberdeen.
select * from properties
where Type = "Flat" and NumofRooms>=3 and rent <=200 and city = "Aberdeen";

-- (o) List the number, name, and telephone number of clients and their property preferences at a given
-- branch.
select * from clientTelephone;
select * from registration;
select * from client;
select a.clientId, concat_ws(' ', a.clientFname,  a.clientLname), a.TypeWanted , b.clientNumber
from client as a, clientTelephone as b
where a.clientId = b.clientId;


-- (p) Identify the properties that have been advertised more than the average number of times. !!!Havent Done

-- (q) List the details of leases due to expire next month at a given branch.
show tables;
select * from leaseAgreement
where RentEndDate < '2023-05-31'; -- the date today is 18th April 2023

-- (r) List the total number of leases with rental periods that are less than one year at branches in
-- London.

select count(LeaseId) 
from LeaseAgreement 
where propertyId in (select propertyId from properties
					  where RegisteredAtbranchId = (select branchId from branch where city = "london")
                      ) and  (RentEndDate-RentStartDate) <= 365;


-- (s) List the total possible daily rental for property at each branch, ordered by branch number.
-- WHAT!!!????


/*
Queries required by the Staff:
(a) List details of staff supervised by a named Supervisor at the branch. -- done before
(b) List details of all Assistants alphabetically by name at the branch.
(c) List the details of property (including the rental deposit) available for rent at the branch, along
with the owner’s details.
(d) List the details of properties managed by a named member of staff at the branch. -- done before
(e) List the clients registering at the branch and the names of the members of staff who registered
the clients.
(f) Identify properties located in Glasgow with rents no higher than £450.
(g) Identify the name and telephone number of an owner of a given property.
(h) List the details of comments made by clients viewing a given property.
(i) Display the names and phone numbers of clients who have viewed a given property but not
supplied comments.
(j) Display the details of a lease between a named client and a given property.
(k) Identify the leases due to expire next month at the branch.
(l) List the details of properties that have not been rented out for more than three months.
(m) Produce a list of clients whose preferences match a particular property.
*/

-- (b) List details of all Assistants alphabetically by name at the branch.
select * from staff
where Position = 'A'
order by StaffFName, StaffMName,StaffLName;

-- (c) List the details of property (including the rental deposit) available for rent at the branch, along
-- with the owner’s details.

select * from properties as p, owner as o where p.ownerid = o.ownerid;

-- (e) List the clients registering at the branch and the names of the members of staff who registered
-- the clients.
select * from registration;

-- (f) Identify properties located in Glasgow with rents no higher than £450.
select * from properties where rent <= 450*100; -- cuz 1 pound = 100rs roughly

-- (g) Identify the name and telephone number of an owner of a given property.
select * from ownerTelephone;
select * from owner;
select * from properties;
select Name, ownerNumber
from owner as og, ownerTelephone as pg
where og.ownerId = pg.ownerId and og.ownerId in (select cg.ownerId from properties as cg
													where propertyId = '3'); -- or your pid

-- (h) List the details of comments made by clients viewing a given property.
show tables;
select propertId, clientId, comments from propertyView;

-- (i) Display the names and phone numbers of clients who have viewed a given property but not
-- supplied comments.
select * from client;
select * from propertyview;
select * from clientTelephone;
select concat_ws(' ', clientFname, ClientMname, clientLname) as name, clientNumber as number
from client as a, clientTelephone as b 
where a.clientId = b.clientId and a.clientid in (select c.clientId from propertyview as c
												 where comments is null);
											
-- (j) Display the details of a lease between a named client and a given property.
select * from leaseAgreement
where clientId is not null;

-- (l) List the details of properties that have not been rented out for more than three months.
select * from properties;
select * from leaseagreement;

select * from properties as f
where propertyId in (select propertyId from leaseAgreement
					  where rentEndDate - '2023-04-18' >=90);
                      
-- (m) Produce a list of clients whose preferences match a particular property.
select * from client;
select * from properties;
select * from client
where Typewanted = (select type from properties where propertyId = (2))
		and maxRent<=(select rent from properties where propertyId = (2));
