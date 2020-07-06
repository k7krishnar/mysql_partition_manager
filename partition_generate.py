
import pandas as pd
from datetime import datetime


def generate_partitions(database,table,column,type,start_time,count,interval):
	conversion_function = 'TO_SECONDS' if type == 'datetime' else 'UNIX_TIMESTAMP'
	dti = pd.date_range(start_time, periods=count, freq=interval)
	print(f"ALTER TABLE {database}.{table} PARTITION BY RANGE ({conversion_function}({column}))\n( PARTITION p_min VALUES LESS THAN (1),")
	for d in dti:
		print(f"PARTITION upto_{d.date().strftime('%Y_%m_%d')} VALUES LESS THAN ({conversion_function}('{d}')),")
	print(f"PARTITION pmax VALUES LESS THAN MAXVALUE )")
