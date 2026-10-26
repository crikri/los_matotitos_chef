
-- 1. Renombrar la tabla actual a 'usuario' (reemplaza 'nombre_tabla_actual' por el nombre real)
RENAME TABLE clientes TO usuarios;

-- 2. Agregar los nuevos campos 'habilitados' y 'contrasena'
ALTER TABLE usuarios
ADD COLUMN habilitados BOOLEAN NOT NULL DEFAULT 1,
ADD COLUMN contrasena VARCHAR(60) NULL;

ALTER TABLE usuarios
ADD COLUMN rut VARCHAR(12) NOT NULL UNIQUE;