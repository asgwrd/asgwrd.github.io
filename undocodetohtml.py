import os

# Define the script tag to be removed
SCRIPT_TAG = '<script async data-id="101479244" src="/055fd9e41d00ec.js"></script>'

def remove_script_from_html(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                # Read the file content
                with open(file_path, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Remove the script tag if present
                    if SCRIPT_TAG in content:
                        content = content.replace(SCRIPT_TAG, '').strip()
                        
                        # Write the modified content back to the file
                        f.seek(0)
                        f.write(content)
                        f.truncate()
                        print(f"Reverted: {file_path}")
                    else:
                        print(f"Skipped (script not found): {file_path}")

# Run the function on the current directory
remove_script_from_html(".")
