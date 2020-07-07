# mysql_partition_manager

Scope:

1. generate partitions ie, non-partitioned to a partitioned table
2. manage partitions ie, adding new/removing old partitions

Sample output:
krishna.r@sonata % python3 make_partition.py
Validation success! 👍
-----
ALTER TABLE classic.furelise PARTITION BY RANGE (UNIX_TIMESTAMP(created_at))
( PARTITION p_min VALUES LESS THAN (1),
PARTITION upto_2020_07_01 VALUES LESS THAN (UNIX_TIMESTAMP('2020-07-01 00:00:00')),
PARTITION upto_2020_08_01 VALUES LESS THAN (UNIX_TIMESTAMP('2020-08-01 00:00:00')),
PARTITION upto_2020_09_01 VALUES LESS THAN (UNIX_TIMESTAMP('2020-09-01 00:00:00')),
PARTITION upto_2020_10_01 VALUES LESS THAN (UNIX_TIMESTAMP('2020-10-01 00:00:00')),
PARTITION upto_2020_11_01 VALUES LESS THAN (UNIX_TIMESTAMP('2020-11-01 00:00:00')),
PARTITION upto_2020_12_01 VALUES LESS THAN (UNIX_TIMESTAMP('2020-12-01 00:00:00')),
PARTITION upto_2021_01_01 VALUES LESS THAN (UNIX_TIMESTAMP('2021-01-01 00:00:00')),
PARTITION pmax VALUES LESS THAN MAXVALUE )
-----
ALTER TABLE modern.yaani PARTITION BY RANGE (TO_SECONDS(created_on))
( PARTITION p_min VALUES LESS THAN (1),
PARTITION upto_2020_07_01 VALUES LESS THAN (TO_SECONDS('2020-07-01 12:00:00')),
PARTITION upto_2020_07_02 VALUES LESS THAN (TO_SECONDS('2020-07-02 12:00:00')),
PARTITION upto_2020_07_03 VALUES LESS THAN (TO_SECONDS('2020-07-03 12:00:00')),
PARTITION upto_2020_07_04 VALUES LESS THAN (TO_SECONDS('2020-07-04 12:00:00')),
PARTITION upto_2020_07_05 VALUES LESS THAN (TO_SECONDS('2020-07-05 12:00:00')),
PARTITION upto_2020_07_06 VALUES LESS THAN (TO_SECONDS('2020-07-06 12:00:00')),
PARTITION upto_2020_07_07 VALUES LESS THAN (TO_SECONDS('2020-07-07 12:00:00')),
PARTITION pmax VALUES LESS THAN MAXVALUE )
-----
