# Eidolon

Eidolon is a game engine made in Python
using [Raylib](https://www.raylib.com/)
and [Esper](https://pypi.org/project/esper/).

## 📑 <samp>Requirements</samp>

You have the choice between using nix or local dependencies.

### 🔧 <samp>Dependencies</samp>

- [Python 3.10+](https://www.python.org/downloads/) (with pip)
- [Make](https://www.gnu.org/software/make/)

### 🌸 <samp>[Nix](https://nixos.org/download.html) user</samp>

You will need to enable `nix-command` and `flakes`experimental features
If you get an error about it, consider this command:

```sh
mkdir -p ~/.config/nix
echo "experimental-features = nix-command flakes" \
    | tee ~/.config/nix/nix.conf
```

## ⚡ <samp>Usage</samp>

### 🔧 <samp>Setup</samp>

Start by cloning this repository

```sh
git clone https://github.com/Miou-zora/Eidolon.git
cd Eidolon
```

#### With local dependencies

Install the dependencies with pip

```sh
python -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/pip install -e .
```

#### With 🌸 <samp>nix</samp>

Run the client directly

```sh
nix develop
```

### 🚀 <samp>Running</samp>

#### With local dependencies

```sh
make client
# or / and
make server
```

#### With 🌸 <samp>nix</samp>

```sh
nix run 
```

### ➕ <samp>Using direnv</samp>

You may load the devShell automatically using [direnv](https://direnv.net)
shell integration.

```

echo "use flake" | tee .envrc
direnv allow

```

### 👷 <samp>Building</samp>

#### Release

```sh
make exe-client
# or / and
make exe-server
```

After, you can find the executable in the `dist` directory.

### 🩵 Contributors

![alt](https://contrib.rocks/image?repo=Miou-zora/Eidolon)
