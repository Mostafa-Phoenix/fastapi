{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-24.05"; # or "unstable"
  # Use https://search.nixos.org/packages to find packages
  packages = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.fastapi
    python311Packages.uvicorn
    wget
    tree
    nano
    llama-cpp  # The system package, if needed.
    gcc
    cmake
    ccache
    busybox
    util-linux
  ];
  # Sets environment variables in the workspace
  env = {};
  idx = {
    previews = {
      enable = true;
      previews = {
        web = {
          command = [ "./devserver.sh" ];
          env = { PORT = "8080"; };
          manager = "web";
          cwd = ".";
        };
      };
    };
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [ "ms-python.python" "ms-python.debugpy"];
    workspace = {
      # Runs when a workspace is first created with this `dev.nix` file
      onCreate = {
        install =
          "python -m venv .venv && source .venv/bin/activate &&  pip install -r requirements.txt";
        # Open editors for the following files by default, if they exist:
        default.openFiles = [ "app.py" ];
      };
    };
  };
}
