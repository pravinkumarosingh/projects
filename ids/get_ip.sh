#!/bin/bash
cat files.log |grep $1 > temp_file.txt
cut -b 53-62 temp_file.txt > destination_ip.txt
rm temp_file.txt
