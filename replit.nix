{ pkgs }: {
  deps = [
    pkgs.unzip
    pkgs.wget
    pkgs.nano
    pkgs.bashInteractive
    pkgs.nodePackages.bash-language-server
    pkgs.man
  ];
}