import os
import subprocess

def run_subfinder(url):
    output_file = "subdomains.txt"
    text=''' 
 _____ ___ _  ___   _          _                
| ____|_ _| |/ / | | |_      _| |   _   ___   __
|  _|  | || ' /| |_| \ \ /\ / / |  | | | \ \ / /
| |___ | || . \|  _  |\ V  V /| |__| |_| |\ V / 
|_____|___|_|\_\_| |_| \_/\_/ |_____\__,_| \_/  

    '''
    print(text)
    command = f"subfinder -d {url} -all -silent | httpx -mc 200 -silent | nuclei -silent"
    output = subprocess.check_output(command, shell=True, text=True)
    with open(output_file, "w") as file:
        file.write(output)

    print(f"Subdomains saved in {output_file}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    run_subfinder(url)