###These are pre-compiled binaries of stable FLO Core Wallet (For Linux)

To run FLO core wallet QT :
	./flo-qt

To run FLO testnet wallet QT :
	./flo-qt -testnet

To run FLO cli commands:
	./flo-cli

To run FLO transaction commands :
	./flo-tx

To start FLO server :
	./flod

To start FLO server in daemon mode :
	./flod -daemon


###Upgrade Details

Added 2 features to the FLO wallet :
1. CoinControlFIFO - selects the coins that were received first to be spent first (First-In-First-Out).
To enable it:add **CoinControlFIFO=1** in flo.conf (or) pass **-CoinControlFIFO** as cmdline arg. For ex:
	./flo-qt -CoinControlFIFO

2. SendChangeToBack - send the change back to the coin's original address
To enable it, add **SendChangeToBack=1** in flo.conf (or) pass **-SendChangeToBack** as cmdline arg. For ex:
	./flo-qt -SendChangeToBack


###FLO Core MultiWallet
This executable file is used to run more than 1 wallet simultaneously

Usage:

	./multiWallet -create [walletName]
		creates a wallet under 'walletName' if specified
		else creates wallet with name 'floxxxxxx'
	
	./multiWallet <walletName> <command> [option]
		executes the command in wallet 'walletName'

commands:

	flo-qt		-	open FLO Core Wallet
	flo-cli		-	run cli commands
	flod		-	run FLO daemon

for more info on each commands use option -help (or) -?
	./flo-qt -?
	./flo-cli -?
	./flod -?
