#!/usr/bin/bash

set -e
SESSION_NAME="Chess Engine"

tmuxAttachCommand=""
if [ "$TMUX" != "" ]; then
  tmuxAttachCommand="tmux switch-client -t \"$SESSION_NAME:Editor\""
else
  tmuxAttachCommand="tmux attach -t \"$SESSION_NAME:Editor\""
fi

if tmux has-session -t "$SESSION_NAME" 2> /dev/null; then
  eval "$tmuxAttachCommand"
fi

tmux new-session -d -s "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "Editor"
tmux send-keys -t "$SESSION_NAME" "nvim" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "Compilation"
tmux send-keys -t "$SESSION_NAME" "nvim" Enter

tmux new-window -t "$SESSION_NAME"

tmux rename-window -t "$SESSION_NAME" "Git"
tmux send-keys -t "$SESSION_NAME" "clear; wgs" Enter

eval "$tmuxAttachCommand"
