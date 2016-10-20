
drop table if exists user;
create table user(
    user_id integer primary key,
    nickname text not null,
    email text not null
);

drop table if exists trip;
create table trip(
    trip_id integer primary key,
    destination text not null,
    trip_date text not null,
    duration integer not null,
    budget integer not null
);

drop table if exists user_trip;
create table user_trip(
    id integer primary key,
    user_id integer not null,
    trip_id integer not null,
        foreign key (user_id) references user(user_id),
        foreign key (trip_id) references trip(trip_id)
);

insert into user values(1, 'sberthely', 'Selenne', 'Berthely', 'sberthely@berkeley.edu');
insert into user values(2, 'nyhyang', 'Nancy', 'Yang', 'nyhyang@berkeley.edu');

insert into trip values(1, 'Mallorca', '10152016', '5', '3500');

insert into user_trip values(1, 2, 1);