# Minecraft Mode Manager or MMM for short

Suggested git client: <https://git-fork.com/update/win/ForkInstaller.exe>

## Steps to use the tools

1. Download and install Fork
2. Press `Ctrl + N` -> new repo
3. Paste github link in: <https://github.com/joshika39/minecraft-mods.git>
4. Leave everything as it is, (`%homepath%\Fork\minecraft-mods`)
5. Start the `Terminal` application:
    - *(If running of the scripts are disabled run the following in a Terminal ran as **Admin**: `Set-ExecutionPolicy Unrestricted`)*
6. Run the following command: `cd $HOME\Fork\minecraft-mods\; .\download.ps1`
7. Follow the following sequence in the options: `from-cdn` -> `client` -> `Yes`

#### Other useful options

- command to get the ip from the terminal: `cd $HOME\Fork\minecraft-mods\; .\print-ip.ps1`
- command to open the ports for minecraft server(25565):
  - start an **Admin** Terminal end run the following command: `cd $HOME\Fork\minecraft-mods\; .\open-ports.ps1`

#### To Search for mods

- [link search](https://www.curseforge.com/minecraft/mc-mods/mod_name/files/all?filter-game-version=2020709689%3A8203)
- [general search](https://www.curseforge.com/minecraft/mc-mods/search?category=&search=mode_name)
