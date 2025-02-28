import os
import re

# The script you want to add to each HTML file
script_to_add = """
<script>
  // Initialize the agent on page load.
  const fpPromise = import('https://fpjscdn.net/v3/OMK6LuUwm9TBwFox0cyX')
    .then(FingerprintJS => FingerprintJS.load())

  // Get the visitorId when you need it.
  fpPromise
    .then(fp => fp.get())
    .then(result => {
      const visitorId = result.visitorId
      console.log(visitorId)
    })
</script>
"""

# Function to add or remove the script from an HTML file
def modify_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the script already exists in the file
        if script_to_add in content:
            # If it exists, remove it
            content = content.replace(script_to_add, "")
            print(f"Removed script from {file_path}")
        else:
            # If it doesn't exist, add it at the bottom
            # Only add if the closing </body> tag exists
            if "</body>" in content:
                content = content.replace("</body>", script_to_add + "\n</body>")
                print(f"Added script to {file_path}")

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

# Function to go through the directory and subdirectories
def process_html_files_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                modify_html_file(file_path)

# Run the function on the current directory
if __name__ == "__main__":
    current_directory = os.getcwd()
    process_html_files_in_directory(current_directory)
