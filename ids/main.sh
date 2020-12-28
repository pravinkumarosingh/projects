#!/bin/bash


tshark -i eth0 -a duration:15 -w temp.pcap
bro -Cr temp.pcap extract-all-files
bro -Cr temp.pcap
sleep 1
python yaraZeekAlert.py
sleep 2

rm temp.pcap

