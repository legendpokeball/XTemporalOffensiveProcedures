{ pkgs }:
 let
   # assuming this is the path to chromedriver
   chromedriverPath = "/nix/store/n4qcnqy0isnvxcpcgv6i2z9ql9wsxksw-chromedriver-114.0.5735.90/bin/chromedriver";
   setPermissionsScript = ''
     chmod 777 ${chromedriverPath}
   '';
 in{
  deps = [
    pkgs.wget
    pkgs.chromium
    pkgs.chromedriver
  ];
  # postBuild = ''
  #   chmod 777 $out/nix/store/n4qcnqy0isnvxcpcgv6i2z9ql9wsxksw-chromedriver-114.0.5735.90/bin/chromedriver
  # '';
  # postInstall = "
  #   mkdir -p $out/bin
  #   # Copy the post-installation script
  #   cp $src/post-install.sh $out/bin
  #   # Make sure the script is executable
  #   chmod +x $out/bin/post-install.sh
  #   # Run the script as part of the installation
  #   $out/bin/post-install.sh
  # ";
   shellHook = ''
     ${setPermissionsScript}
     # other shell hooks
   '';
   }