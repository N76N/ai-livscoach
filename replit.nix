{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.uvicorn
    pkgs.python311Packages.fastapi
    pkgs.python311Packages.openai
    pkgs.python311Packages.python-dotenv
  ];
}
