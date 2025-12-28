#!/bin/bash

# Calculate line and word counts
lines=$(wc -l < /app/input.txt)
words=$(wc -w < /app/input.txt)

# Write output to /app/output.txt
echo "lines: $lines" > /app/output.txt
echo "words: $words" >> /app/output.txt
