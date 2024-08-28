from googlesearch import search  # Ensure this is the correct import

# Banner Information
BANNER = """
ooo.                8      .oPYo.                                        
8  `8.              8      8                                             
8   `8 .oPYo. oPYo. 8  .o  `Yooo. .oPYo. .oPYo. odYo. odYo. .oPYo. oPYo. 
8    8 8    8 8  `' 8oP'       `8 8    ' .oooo8 8' `8 8' `8 8oooo8 8  `' 
8   .P 8    8 8     8 `b.       8 8    . 8    8 8   8 8   8 8.     8     
8ooo'  `YooP' 8     8  `o. `YooP' `YooP' `YooP8 8   8 8   8 `Yooo' 8     
.....:::.....:..::::..::...:.....::.....::.....:..::....::..:.....:..::::
                       Google Dorking Tool
                          Version: 1.0
                       Author: G4UR4V007
.....:::.....:..::::..::...:.....::.....::.....:..::....::..:.....:..::::
"""

def google_dork(query, num_results=10):
    """
    Perform a Google search using the given dorking query.

    Args:
        query (str): The dorking query to use.
        num_results (int): The number of results to return. Defaults to 10.

    Returns:
        list: A list of search results.
    """
    results = list(search(query, num_results=num_results))  # Use the correct search function
    return results

def main():
    print(BANNER)
    query = input("Enter a dorking query: ")
    num_results = int(input("Enter the number of results to return (default=10): ") or 10)
    results = google_dork(query, num_results)

    print("\nSearch Results:")
    for result in results:
        print(result)  # Print each result directly

if __name__ == "__main__":
    main()
