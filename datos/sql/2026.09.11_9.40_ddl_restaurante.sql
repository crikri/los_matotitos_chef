create database restaurante;

use restaurante;

create table comunas(
    id_comuna int auto_increment, -- auto increment hace q ponga el id solito
    codigo_comuna char(5) not null,
    comuna varchar(30) not null,

    constraint pk_comunas primary key (id_comuna)        
) COMMENT = 'Listado de comunas de Chile deacuerdo a la SUBDERE';

create table  direcciones
(
    id_direccion integer auto_increment,
    comuna integer not null,
    calle varchar(50) not null,
    numero varchar(10) not null,
    departamento varchar(10) null,

    constraint pk_direcciones primary key (id_direccion),
    constraint fk_direcciones_comunas foreign key(comuna) references comunas (id_comuna)
) comment = 'Tabla para guardar direcciones de restaurante, cliente, usuarios, etc';

create table restaurantes(
    id_restaurantes integer auto_increment,
    nombre varchar(50) not null,
    direccion integer not null,
    telefono char(12) not null,
    email varchar(50) not null,
    website varchar(50) null,

    constraint pk_restaurantes primary key (id_restaurantes),
    constraint fk_restaurantes_direcciones foreign key(direccion) references direcciones (id_direccion)
) comment = 'Tabla para guardar los restaurantes';

create table paises (
    id_pais integer auto_increment,
    nombre varchar(60) not null,
    nacionalidad varchar(30) not null,
    iso_2 char(2) null,
    iso_3 char(3) null,

    constraint pk_paises primary key (id_pais)
);

create table clientes(
    id_cliente integer auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    fecha_nacimiento date not null,
    nacionalidad integer not null,
    direccion integer not null,
    telefono char(12) not null,
    email varchar(50) not null,

    constraint pk_clientes primary key (id_cliente),
    constraint fk_clientes_paises foreign key(nacionalidad) references paises (id_pais),
    constraint fk_clientes_direcciones foreign key(direccion) references direcciones (id_direccion)
) comment = 'Tabla para guardar los clientes del restaurante';

create table estado_reserva(
    id_estado integer auto_increment,
    estado varchar(20) not null,

    constraint pk_estado primary key (id_estado)
) comment = 'Tabla para guardar los estados de las reservas';

create table restaurante_mesas(
    id_restaurante_mesa integer auto_increment,
    restaurante integer not null,
    mesa integer not null,

    constraint pk_restaurante_mesas primary key (id_restaurante_mesa),
    constraint fk_restaurante_mesas_restaurantes foreign key(restaurante) references restaurantes (id_restaurantes),
    constraint fk_restaurante_mesas_mesas foreign key(mesa) references mesas (id_mesa)
) comment = 'Tabla para guardar la relación de las mesas con los restaurantes';

create table mesas(
    id_mesa integer auto_increment,
    capacidad integer not null,
    estado char(1) not null,
    restaurante integer not null,
    numero_mesa char(5) not null,

    constraint pk_mesas primary key (id_mesa),

) comment = 'Tabla para guardar las mesas de los restaurantes';

create table reservas(
    id_reserva integer auto_increment,
    cliente integer not null,
    estado integer not null,
    mesa integer not null,
    fecha date not null,
    hora_inicio time not null,
    hora_termino time not null,
    cantidad_personas integer not null,

    constraint pk_reservas primary key (id_reserva),
    constraint fk_reservas_clientes foreign key(cliente) references clientes (id_cliente),
    constraint fk_reservas_estados foreign key(estado) references estado_reserva (id_estado),
    constraint fk_reservas_mesas foreign key(mesa) references mesas (id_mesa)
) comment = 'Tabla para guardar las reservas de los clientes en los restaurantes';



create table restaurantes_trabajadores(
    id_restaurante_trabajador integer auto_increment,
    restaurante integer not null,
    trabajador integer not null,

    constraint pk_restaurantes_trabajadores primary key (id_restaurante_trabajador),
    constraint fk_restaurantes_trabajadores_restaurantes foreign key(restaurante) references restaurantes (id_restaurantes),
    constraint fk_restaurantes_trabajadores_trabajadores foreign key(trabajador) references trabajadores (id_trabajador)
) comment = 'Tabla para guardar la relación de los trabajadores con los restaurantes';

create table trabajadores(
    id_trabajador integer auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    fecha_nacimiento date not null,
    nacionalidad integer not null,
    direccion integer not null,
    telefono char(12) not null,
    email varchar(50) not null,
    restaurante integer not null,

    constraint pk_trabajadores primary key (id_trabajador),
    constraint fk_trabajadores_paises foreign key(nacionalidad) references paises (id_pais),
    constraint fk_trabajadores_direcciones foreign key(direccion) references direcciones (id_direccion),
) comment = 'Tabla para guardar los trabajadores de los restaurantes';


-- select au.nombre, au.pseudonimo, (select p.nacinalidad from países p where au.nacionalidad = p.id_pais), au.fecha_nacimiento from autores au git gigits