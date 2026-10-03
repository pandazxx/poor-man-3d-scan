# List available recipes
default:
    @just --list

# Update flake inputs
update:
    nix flake update

# Pull latest template changes
template-update:
    copier update --trust
