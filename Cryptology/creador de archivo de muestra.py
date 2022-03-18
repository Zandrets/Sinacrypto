org_file=open('GNS3 Topology-20220202T182024Z-001.zip', 'rb')
new_file=open('test_file.tmp', '+wb')
new_file.write(org_file.read(1048576))
org_file.close
new_file.close