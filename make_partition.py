import yamale
import partition_generate as pg

banner='-----'
data = yamale.make_data('partition_config.yaml')
schema = yamale.make_schema('schema.yaml')

try:
    yamale.validate(schema, data)
    print('Validation success! 👍')
    print(banner)
    data,_ = data[0]
    for d in data:
    	pg.generate_partitions(**d)
    	print(banner)
except Exception as e:
    print('Validation failed!\n%s' % str(e))
    exit(1)
