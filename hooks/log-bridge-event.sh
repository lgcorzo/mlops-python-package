#!/bin/bash
# hooks/log-bridge-event.sh
# Utility script to log structured bridge events for ISO 15289 traceability.
# Usage: ./hooks/log-bridge-event.sh <event_type> [details]
#
# Example: ./hooks/log-bridge-event.sh "graphify_update" "432 nodes, 578 edges"

EVENT_TYPE="${1:-unknown}"
DETAILS="${2:-}"
BRIDGE_LOG=".specify/bridge/bridge-events.jsonl"

# Get current commit SHA (short)
COMMIT_SHA=$(git rev-parse --short HEAD 2>/dev/null || echo "N/A")

# Get ISO 8601 UTC timestamp
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Build JSON event line
if [ -n "$DETAILS" ]; then
    EVENT_JSON="{\"event\":\"${EVENT_TYPE}\",\"commit\":\"${COMMIT_SHA}\",\"timestamp\":\"${TIMESTAMP}\",\"agent\":\"git-hook\",\"details\":\"${DETAILS}\"}"
else
    EVENT_JSON="{\"event\":\"${EVENT_TYPE}\",\"commit\":\"${COMMIT_SHA}\",\"timestamp\":\"${TIMESTAMP}\",\"agent\":\"git-hook\"}"
fi

# Append to bridge events log (create if missing)
if [ -d "$(dirname "$BRIDGE_LOG")" ]; then
    echo "$EVENT_JSON" >> "$BRIDGE_LOG"
fi
