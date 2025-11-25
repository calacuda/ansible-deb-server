_:
  @just -l

run:
  ansible-playbook -i ./inventory setup.yml

run-no-boot:
  ansible-playbook -i ./inventory --skip-tags boot-vms setup.yml
