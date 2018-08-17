FLO Core MultiWallet

This executable file is used to run more than 1 wallet at a same time

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
