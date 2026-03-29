#!/usr/bin/env bash

# usage: cd 2025 && ../link-top-level-dirs.sh en-us

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: link-top-level-dirs.sh <target-dir>

Scans the immediate subdirectories under <target-dir>, removes entries with the
same names in the current directory, and recreates them as symlinks pointing
back to <target-dir>.
EOF
}

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 1
fi

target_dir=${1%/}

if [[ -z "$target_dir" ]]; then
  echo "Target directory cannot be empty." >&2
  exit 1
fi

if [[ ! -d "$target_dir" ]]; then
  echo "Target directory does not exist: $target_dir" >&2
  exit 1
fi

current_dir=$(pwd -P)
target_realpath=$(cd "$target_dir" && pwd -P)

if [[ "$current_dir" == "$target_realpath" ]]; then
  echo "Target directory cannot be the current directory." >&2
  exit 1
fi

found_any=0

while IFS= read -r -d '' child_path; do
  found_any=1
  folder_name=${child_path##*/}

  if [[ -e "$folder_name" || -L "$folder_name" ]]; then
    rm -rf -- "$folder_name"
  fi

  ln -s -- "$child_path" "$folder_name"
  printf 'linked %s -> %s\n' "$folder_name" "$child_path"
done < <(find "$target_dir" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

if [[ $found_any -eq 0 ]]; then
  echo "No immediate subdirectories found in $target_dir."
fi
