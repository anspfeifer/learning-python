#!/usr/bin/python

import subprocess
import json

from jinja2 import Environment
from jinja2 import FileSystemLoader
from time import sleep

DEADLINE = 300


def replace_name_job(node):
    template = 'job-docker-gc.jinja'
    target = '/etc/docker-gc/{}.yaml'.format(node)
    env = Environment(loader=FileSystemLoader('/etc/docker-gc/'))
    with open(target, 'w') as file_target:
        file_target.write(env.get_template(template).render({'node': node, 'deadline': DEADLINE}))


def get_nodes_name():
    cmd = ["kubectl", "get", "nodes", "-o", "json"]
    out = subprocess.check_output(cmd)
    nodes = json.loads(out)
    list_node_names = []
    for node in nodes['items']:
        list_node_names.append(node['metadata']['name'])
    return list_node_names


def get_jobs():
    cmd = ["kubectl", "get", "jobs", "--namespace=jenkins", "-o", "json"]
    out = subprocess.check_output(cmd)
    jobs = json.loads(out)
    return jobs


def get_list_jobs_name():
    list_job_names = []
    for job in get_jobs()['items']:
        list_job_names.append(job['metadata']['name'])
    return list_job_names


def delete_job_by_name(job):
    cmd = ["kubectl", "delete", "job", job, "--namespace=jenkins"]
    delete_job = subprocess.check_output(cmd)
    print("Deleting job: {}".format(job))
    print(delete_job)


def delete_jobs():
    for job in get_list_jobs_name():
        delete_job_by_name(job)


def create_jobs():
    for node_name in get_nodes_name():
        replace_name_job(node_name)
        job_file = '/etc/docker-gc/{}.yaml'.format(node_name)
        cmd = ["kubectl", "create", "-f", job_file, '--namespace=jenkins']
        subprocess.check_output(cmd)
        print("Creating job docker-gc-{}".format(node_name))


if __name__ == '__main__':
    print('Starting docker-gc')

    print('Cleanup old jobs')
    delete_jobs()

    print('Create Jobs')
    create_jobs()

    print('Waiting {}'.format(DEADLINE + 60) + ' seg.')
    sleep(DEADLINE + 60)

    print('Deleting Jobs')
    delete_jobs()
