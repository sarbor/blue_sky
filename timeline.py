import subprocess
import re

def get_usernames(text):
    """
    Extract unique usernames from the given text. Usernames are identified as substrings
    that appear before ".bsky.social" in the text.

    Args:
        text (str): The input text from which to extract usernames.

    Returns:
        list[str]: A list of unique usernames with the format "username.bsky.social".
    """
    # Modify the pattern to capture the entire username, including the ".bsky.social" suffix
    pattern = r"(\w+\.bsky\.social)"

    # Use a set comprehension to extract unique usernames
    usernames = {username for username in re.findall(pattern, text)}

    return list(usernames)

def get_followers(handle):
    """
    Retrieve and print the followers of a given bsky.social handle using the "bsky" command-line tool.
    The function prints the list of follower handles and the total number of followers.

    Args:
        handle (str): The bsky.social handle for which to retrieve followers.
    """
    result = subprocess.run(["bsky", "followers", "-H", handle], capture_output=True, text=True)
    followers_raw_text = result.stdout
    followers_handles = get_usernames(followers_raw_text)
    print(followers_handles)
    print(len(followers_handles))
    

def main():
    result = subprocess.run(["bsky", "tl"], capture_output=True, text=True)

    timeline = result.stdout

    usernames = get_usernames(timeline)

    first_username = usernames[0]
    print(first_username)

    get_followers(first_username)

if __name__ == '__main__':
    main()
