create user "iec-n2-c2"@"localhost" identified by "iec-n2-c2";

grant  all privileges on restaurante.* to "iec-n2-c2"@"localhost";

flush privileges;