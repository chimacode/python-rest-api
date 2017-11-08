drop table if exists user;
create table user (
    id integer primary key autoincrement,
    username text not null unique,
    name text not null,
    email text not null
);

insert into user (username, name, email)
values ('rogowski', 'Marcos', 'mvrogowski@gmail.com');
