input_file = "./original-src/challengefile"
output_file = "./original-src/fixed_challengefile.jpg"

with open(input_file, "rb") as f:
    data = f.read()

reordered_data = bytearray()
for i in range(0, len(data), 4):
    reordered_data.extend(data[i : i + 4][::-1])  # noqa

with open(output_file, "wb") as f:
    f.write(reordered_data)

print(f"Reordered file saved as {output_file}")
