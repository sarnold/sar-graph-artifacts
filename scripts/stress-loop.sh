#!/bin/bash

MEM=${1:-128M}
TMOUT=${2:-20s}
SLEEP=${3:-5}

while :; do
    stress-ng --cpu 2 --io 4 --vm 4 --vm-bytes $MEM --fork 4 --timeout $TMOUT
    sleep $SLEEP
done
