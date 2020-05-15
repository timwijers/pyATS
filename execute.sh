#!/bin/bash

banner()
{
  echo "+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"
  printf "| %-40s |\n" "`date`"
  echo "|                                                                                                                                                                           |"
  printf "|`tput bold` %-40s `tput sgr0` |\n" "$@"
  echo "+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"
}

banner "Creating the Labs and Nodes for the pyATS framework in Eve-NG"

cd /etc/ansible/pyATS

sudo git pull http://github.com/timwijers/pyATS

sudo python 'Configure Eve-ng Labs.py'

banner "Waking the Nodes in Eve-NG so a telnet session can be instantiated"
cd

./test.sh
./test.sh

cd /etc/ansible/pyATS

banner "Find the DHCP leases given to the Eve-NG nodes, extract them to the Ansible Hosts file and pyATS testbed and finally enable SSH on the Nodes for pyATS connectivity"

sudo python3 'searchIP_Fill_TB_&_Hosts.py'

sudo python setSSH_Routers.py

sudo rm -r /etc/ansible/hosts

sudo cp /etc/ansible/pyATS/hosts /etc/ansible/hosts

banner "Execute the Ansible Playbook which creates the Docker Container on which the PyATS framework will run and finally execute the test cases"

ansible-playbook -v AnsiblePLB_Execute_TestingPipeline.yml --extra-vars "ansible_sudo_pass=pfne"

banner "The Results can be viewed with the Docker Host IP"