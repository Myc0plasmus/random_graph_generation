{
  inputs = {
    nixpkgs.url = "github:/nixos/nixpkgs?ref=nixos-unstable";
    # nixpkgs.url = "github:/nixos/nixpkgs/c0b0e0fddf73fd517c3471e546c0df87a42d53f4";
  };

  outputs = { nixpkgs, ... }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs {
        inherit system;
      };
      fsh = pkgs.buildFHSEnv rec {
        name = "random_graph_generation";

        targetPkgs = _: [
          pkgs.micromamba
          pkgs.jupyter
        ];

        profile = ''
          set -e

          export MAMBA_ROOT_PREFIX=''${HOME}/.mamba

          # Check if the environment already exists
          if ! micromamba env list | grep -q "$MAMBA_ROOT_PREFIX/envs/${name}"; then
            echo "Creating environment '${name}'..."
            micromamba create -q -y -n ${name}
          else
            echo "Environment '${name}' already exists. Skipping creation."
          fi

          echo "$MAMBA_ROOT_PREFIX/envs/${name}"
          chmod u+w "$MAMBA_ROOT_PREFIX/envs/${name}"

          # Install packages only if env.yml has been updated
          if [ ! -f "$MAMBA_ROOT_PREFIX/envs/${name}/.env-hash" ] ||
             ! sha256sum -c "$MAMBA_ROOT_PREFIX/envs/${name}/.env-hash"
          then
              echo "Installing/updating packages from environment files..."
              micromamba install -y -n ${name} -f env.yml
              sha256sum env.yml > "$MAMBA_ROOT_PREFIX/envs/${name}/.env-hash"
          else
            echo "Packages already installed. Skipping."
          fi

          set +e
        '';

        # Activate the environment directly.
        # The nixpkgs micromamba binary is named ".mamba-wrapped",
        # which breaks `micromamba shell hook` name detection, so we
        # skip the hook and eval the activation script instead.
        #
        # Also allows for both:
        # * micromamba environment visibility
        # * ensuring that env is activated only once
        runScript = ''
          bash --rcfile <(
            echo 'eval "$(micromamba shell activate --shell posix --name ${name})"'
          )
        '';
      };
    in
    {
      devShells.${system}.default = fsh.env;

    };
}
