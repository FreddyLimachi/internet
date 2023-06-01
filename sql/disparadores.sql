/* Ingresar registro de corte o activación en el historial */
create or replace function sp_insert_state_history() returns trigger as
$$
begin
	if (old.is_active != new.is_active and old.is_active = false) then
        insert into core_history values 
        (default, 'Reactivación', CURRENT_DATE, NOW(), NOW(), old.id);
	elseif (old.is_active != new.is_active and old.is_active = true) then
        insert into core_history values 
        (default, 'Corte', CURRENT_DATE, NOW(), NOW(), old.id);
	end if;
	return new;
End
$$
Language plpgsql;


/* Actualizar estado del cliente */
create trigger customer_au after update on core_customer
for each row execute procedure sp_insert_state_history();

/* Ingresar registro de instalación en el historial */
create or replace function sp_insert_install_history() returns trigger as
$$
begin
        insert into core_history values 
        (default, 'Inslatación', new.install_date, NOW(), NOW(), new.id);
	return new;
End
$$
Language plpgsql;


/* Ingresar nuevo cliente */
create trigger customer_ai after insert on core_customer
for each row execute procedure sp_insert_install_history();
