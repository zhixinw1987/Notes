#!/bin/sh
set -e

term_handler() {
    echo "SIGTERM received, waiting..."
    sleep 120
    echo "Forwarding SIGTERM to child"
    kill -TERM "$child_pid" 2>/dev/null
}

trap term_handler TERM

# start nfectl and fix
nfecmd="myapp --option"
$nfecmd &
child_pid=$!

# wait till line 8 stop child pid
wait "$child_pid"