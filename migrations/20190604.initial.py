from yoyo import step

steps = [
    step("""
    CREATE TABLE `first_table` (
      `first_table_id` INT(11)  NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `some_value` VARCHAR(50) DEFAULT NULL,
      `create_time` TIMESTAMP DEFAULT NOW(),
      CONSTRAINT UNIQUE INDEX `some_value` (`some_value`)
    ) ENGINE=INNODB DEFAULT CHARSET=utf8mb4
    """,
         "DROP TABLE `first_table`")
]
