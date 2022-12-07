import argparse
import subprocess

if __name__ == '__main__':

   p = argparse.ArgumentParser()

  #--testdir command line argument added

   p.add_argument('--testdir', required=False, help="File path")

   a = p.parse_args()

   testdir = "C:\\Users\\Sandoval\\Documents\\AUTOMATION\\Nueva_carpeta\\Frame_behave\\features\\FailLogin.feature"  #PUEDES INDICAR EL SCRIPT A EJECUTAR

   #complete command

   c = f'behave --no-capture {testdir}'

   s = subprocess.run(c, shell=True, check=True)