create table users(
    id integer primary key,
    user varchar(255)
);

create table boxes(
    id integer primary key,
    box varchar(255)
);

create table userboxes(
    id integer primary key,
    user varchar(255),
	box varchar(255)
);

insert into users(id,user) values (123,'123');
