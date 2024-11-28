from googlesearch import search
from colorama import Fore, Style, init
init(autoreset=True)

BANNER = f"""
{Fore.CYAN}ooo.                8      .oPYo.                                        
{Fore.CYAN}8  `8.              8      8                                             
{Fore.CYAN}8   `8 {Fore.RED}.oPYo.{Fore.CYAN} oPYo. 8  .o  {Fore.YELLOW}`Yooo.{Fore.CYAN} .oPYo. .oPYo. {Fore.GREEN}odYo. odYo.{Fore.CYAN} .oPYo. oPYo. 
{Fore.CYAN}8    8 {Fore.RED}8    8{Fore.CYAN} 8  `' 8oP'       {Fore.YELLOW}`8{Fore.CYAN} 8    ' .oooo8 {Fore.GREEN}8' `8 8' `8{Fore.CYAN} 8oooo8 8  `' 
{Fore.CYAN}8   .P {Fore.RED}8    8{Fore.CYAN} 8     8 `b.       {Fore.YELLOW}8{Fore.CYAN} 8    . 8    8 {Fore.GREEN}8   8 8   8{Fore.CYAN} 8.     8     
{Fore.CYAN}8ooo'  {Fore.RED}`YooP'{Fore.CYAN} 8     8  `o. {Fore.YELLOW}`YooP'{Fore.CYAN} `YooP' `YooP8 {Fore.GREEN}8   8 8   8{Fore.CYAN} `Yooo' 8     
{Fore.CYAN}.....:::.....:..::::..::...:.....::.....::.....:..::....::..:.....:..::::
                       {Fore.MAGENTA}Google Dorking Tool
                          {Fore.MAGENTA}Version: 1.0
                       {Fore.MAGENTA}Author: G4UR4V007
{Fore.CYAN}.....:::.....:..::::..::...:.....::.....::.....:..::....::..:.....:..::::
"""

def google_dork(query, num_results=10):
    results = list(search(query, num_results=num_results))
    return results

def main():
    print(BANNER)
    query = input(f"{Fore.GREEN}Enter a dorking query: {Style.RESET_ALL}")
    num_results = int(input(f"{Fore.GREEN}Enter the number of results to return (default=10): {Style.RESET_ALL}") or 10)
    results = google_dork(query, num_results)

    print(f"\n{Fore.YELLOW}Search Results:")
    for i, result in enumerate(results, 1):
        print(f"{Fore.CYAN}{i}. {Fore.BLUE}{result}")

if __name__ == "__main__":
    main()
