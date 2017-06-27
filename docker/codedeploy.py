#!/usr/bin/env python

import subprocess
import yaml
import zipfile


def main():
    print "Iniciando PyCodeDeploy"

    data_loaded = ""
    with open("/tmp/appspec.yml", 'r') as stream:
        data_loaded = yaml.load(stream)

    if data_loaded['os'] == 'linux' and data_loaded['version'] == 0.0:
        hooks = data_loaded['hooks']
        files = data_loaded['files']
        steps = ['ApplicationStop', 'DownloadBundle', 'BeforeInstall', 'Install',
                'AfterInstall', 'ApplicationStart', 'ValidateService']

        dir_destination = files[0]['destination']

        for step in steps:
            if step == "DownloadBundle":
                with zipfile.ZipFile('/tmp/artifactor.zip', "r") as z:
                    z.extractall(dir_destination)
                continue

            if step in hooks:
                print "### Step: " + str(step)
                for task in hooks[step]:
                    # print task['timeout']
                    # print task['runas']
                    print str(step) + " - " + str(task['location'])
                    rc = subprocess.call("sh " + dir_destination + "/" + task['location'], shell=True)
                    print(rc)

        #input("Debug: ")


if __name__ == "__main__":
    main()
