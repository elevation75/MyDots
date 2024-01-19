#!/bin/bash

# Check for updates
checkupdates=$(checkupdates | wc -l)

# If there are no updates, show "Up to date"
if [[ "$checkupdates" -eq 0 ]]; then
  echo "Up to date"
  exit 0
fi

# Show the number of updates
echo "Updates: $checkupdates"

# Ask the user if they want to update
read -p "Do you want to update? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  # Update the system
  sudo pacman -Syyu
fi
