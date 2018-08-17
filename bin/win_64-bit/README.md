###These are executable files of stable FLO Core Wallet for Windows 64-bit

Run the following cmds in command prompt (open cmd-prompt in this directory)

To run FLO core wallet QT :
	flo-qt

To run FLO testnet wallet QT :
	flo-qt -testnet

To run FLO cli commands:
	flo-cli

To run FLO transaction commands :
	flo-tx

To start FLO server :
	flod

To start FLO server in daemon mode :
	flod -daemon


###Upgrade Details

AAdded 2 features to the FLO wallet :
1. CoinControlFIFO - selects the coins that were received first to be spent first (First-In-First-Out).
To enable it:add **CoinControlFIFO=1** in flo.conf (or) pass **-CoinControlFIFO** as cmdline arg. For ex:
	flo-qt -CoinControlFIFO

2. SendChangeToBack - send the change back to the coin's original address
To enable it, add **SendChangeToBack=1** in flo.conf (or) pass **-SendChangeToBack** as cmdline arg. For ex:
	flo-qt -SendChangeToBack

