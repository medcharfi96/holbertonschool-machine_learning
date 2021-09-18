-- Scraetion de triggle

delimiter $$
CREATE TRIGGER decrease_items
    AFTER INSERT
    ON orders
    FOR EACH ROW
        BEGIN
            UPDATE items
            SET items.quantity = items.quantity - NEW.number
            WHERE items.name = NEW.item_name;

        END;
$$
delimiter ;