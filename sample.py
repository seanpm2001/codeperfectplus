from subprocess import call

date = '2022-07-21 12:00:00'

call(['git', 'add', '.'], shell=True)

call(['git',  'commit',  '--amend', '--date=2022-07-22 12:00:00'], shell=True)
call(['git', 'pull'], shell=True)
call(['git', 'push'], shell=True)