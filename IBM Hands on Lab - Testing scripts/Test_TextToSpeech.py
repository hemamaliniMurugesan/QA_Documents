import subprocess
import sys
script_name = 'TextToSpeech.py'
output_prefix = 'out'
n_iter = 3

for i in range(n_iter):
    output_file = output_prefix + '_' + str(i) + '.txt'
    sys.stdout = open(output_file, 'w')
    subprocess.call(['python', script_name], stdout=sys.stdout, stderr=subprocess.STDOUT)