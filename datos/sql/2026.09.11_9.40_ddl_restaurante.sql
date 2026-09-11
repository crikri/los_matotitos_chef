create database restaurante;

use restaurante;

create table comunas(
    id_comunas int auto_increment, -- auto increment hace q ponga el id solito
    codigo_comuna char(5) not null,
    comuna varchar(30) not null,

    constraint pk_comunas primary key (id_comunas)        
) COMMENT = 'Listado de comunas de Chile deacuerdo a la SUBDERE';

create table  direcciones
(
    id_direcciones integer auto_increment,
    comuna integer not null,
    calle varchar(50) not null,
    numero varchar(10) not null,
    departamento varchar(10) null,

    constraint pk_direcciones primary key (id_direcciones),
    constraint fk_direcciones_comunas foreign key(comuna) references comunas (id_comunas)
) comment = 'Tabla para guardar direcciones de restaurante, cliente, usuarios, etc';

