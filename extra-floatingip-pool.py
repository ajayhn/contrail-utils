import uuid

from vnc_api import vnc_api
lib = vnc_api.VncApi()

# read pool and associate to tenant-project
proj_obj = lib.project_read(fq_name=['<domain>', '<user-proj>'])
fip_pool_obj = lib.floating_ip_pool_read(fq_name=['default-domain', '<infra-proj>', '<extra-net>', '<extra-pool>'])
proj_obj.add_floating_ip_pool(fip_pool_obj)
lib.project_update(proj_obj)

# create fip
fip_name = str(uuid.uuid4())
fip_obj = vnc_api.FloatingIp(fip_name, fip_pool_obj, <floating_ip_address='<fip-ip>'>)
proj_obj = lib.project_read(fq_name=['<domain>', '<user-proj>'])
fip_obj.set_project(proj_obj)
lib.floating_ip_create(fip_obj)
fip_obj = lib.floating_ip_read(id=fip_obj.uuid)

# read port and associate
port_obj = lib.virtual_machine_interface_read(id='<port-uuid>')
fip_obj.add_virtual_machine_interface(port_obj)
lib.floating_ip_update(fip_obj)

# to delete
fip_obj.del_virtual_machine_interface(port_obj)
lib.floating_ip_delete(fip_obj)
