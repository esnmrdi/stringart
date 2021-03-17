# %%
# format code sequence in an appropriate way

# %%
with open("manual-test-2.txt", "r") as reader:
    sequence = reader.readline()
lst = sequence.split(",")

# %%
large_chunk_size = 50
n_rows = 5
small_chunk_size = int(large_chunk_size / n_rows)
large_chunks = [
    lst[i : i + large_chunk_size] for i in range(0, len(lst), large_chunk_size)
]
with open("manual-test-2-sequence.txt", "w") as writer:
    n = 0
    for large_chunk in large_chunks:
        small_chunks = [large_chunk[i : i + small_chunk_size] for i in range(0, len(large_chunk), small_chunk_size)]
        writer.write(f"{n} - {n + large_chunk_size - 1}\n")
        writer.write("--------------\n")
        for row in small_chunks:
            row = '\t'.join(row)
            writer.write(f"{row}\n")
        writer.write("\n")
        n += large_chunk_size

# %%
