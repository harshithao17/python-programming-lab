# Create a log file

file = open("sample.log", "w")

file.write("INFO: Program started\n")
file.write("WARNING: Low memory\n")
file.write("ERROR: File not found\n")
file.write("INFO: Program completed\n")

file.close()

# Read the log file

file = open("sample.log", "r")

print("LOG FILE CONTENTS")

for line in file:
    print(line.strip())

file.close()