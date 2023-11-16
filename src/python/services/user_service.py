import subprocess


def get_windows_users():
    # Execute the "net user" command to get the list of users
    result = subprocess.run(['net', 'user'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)

    # Check for errors
    if result.returncode != 0:
        raise Exception("Error retrieving users: " + result.stderr)

    # Parse command output
    users = []
    output = result.stdout.splitlines()

    # The relevant output starts after the line "-----" and goes until the line "The command completed successfully."
    start = False
    for line in output:
        if '---' in line:
            start = True
            continue
        if 'The command completed' in line:
            break
        if start:
            # Split line by spaces and filter out empty strings
            line_users = [u.strip() for u in line.split() if u]
            users.extend(line_users)

    return users
