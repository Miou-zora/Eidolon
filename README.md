# Eidolon

Eidolon is a Terraria replica made in Python using custom game engine
using [Raylib](https://www.raylib.com/)
and [Esper](https://pypi.org/project/esper/).

## :bookmark_tabs: <samp>Requirements</samp>

You have the choice between using nix or local dependencies.

### :wrench: <samp>Dependencies</samp>

- [Python 3.10+](https://www.python.org/downloads/) (with pip)
- [Make](https://www.gnu.org/software/make/)

### :cherry_blossom: <samp>[Nix](https://nixos.org/download.html) user</samp>

You will need to enable `nix-command` and `flakes`experimental features
If you get an error about it, consider this command:
`mkdir -p ~/.config/nix && echo "experimental-features = nix-command flakes" | tee ~/.config/nix/nix.conf`

## :zap: <samp>Usage</samp>

### :wrench: <samp>Setup</samp>

Start by cloning this repository

```sh
git clone git clone https://github.com/Miou-zora/Eidolon.git
cd Eidolon
```

#### With local dependencies

Install the dependencies with pip

```sh
python -m venv venv
venv/bin/pip install -r requirements.txt
venv/bin/pip install -e .
```

#### With :cherry_blossom: <samp>nix</samp>

Run the client directly

```sh
nix develop
```

### :rocket: <samp>Running</samp>

```sh
make client
# or / and
make server
```

#### With :cherry_blossom: <samp>nix</samp>
```sh
nix run 
```

### :heavy_plus_sign: <samp>Using direnv</samp>

You may load the devShell automatically using [direnv](https://direnv.net)
shell integration.

```

echo "use flake" | tee .envrc
direnv allow

```

### :construction_worker: <samp>Building</samp>

#### Release

```sh
make exe-client
# or / and
make exe-server
```

After, you can find the executable in the `dist` directory.

### :heart: Contributors

![alt](https://contrib.nn.ci/api?repo=Miou-zora/Zaytracer)
