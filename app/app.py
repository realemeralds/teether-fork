import re
from web3 import Web3
import subprocess
from pathlib import Path

def main():
    # get user input for smart contract
    while True:
        print("Key in a smart contract address!")
        userInput = input()
        if (re.search("^0x[a-fA-F0-9]{40}$", userInput)):
            break
        print("Key in a valid address, make sure to include the 0x")

    my_provider = Web3.HTTPProvider("https://eth-mainnet.public.blastapi.io")
    w3 = Web3(my_provider)
    if (w3.isConnected()):
        print("connected!")

    bytecode = w3.eth.get_code(userInput)
    with open('compiled/contract.data', "w+") as f:
        f.write(bytecode.hex()[2:])
        f.close()
    
    with open(f'graphs/{userInput}.dot', 'w') as f:
        process = subprocess.Popen(['python3', Path.cwd() / 'bin/plot_cfg.py', 'compiled/contract.data', '-t'], stdout=f)
        process.wait()
        with open(f'graphs/{userInput}.svg', 'w') as f:
            process = subprocess.Popen(["dot", "-Tsvg", f'graphs/{userInput}.dot'], stdout=f)
            process.wait()            
            process = subprocess.Popen(["explorer.exe", f"."])
            print("done!")
            
        
        

    
    

if __name__ == "__main__":
    main()
