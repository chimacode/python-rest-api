drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null unique,
    name text not null,
    email text not null
);

insert into users (username, name, email)
values ('rogowski', 'Marcos', 'mvrogowski@gmail.com');
