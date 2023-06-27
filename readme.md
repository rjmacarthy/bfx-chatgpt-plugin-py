## ChatGPT Plugin for Bitfinex Public API

This is an **unofficial** ChatGPT plugin for the [Bitfinex](https://www.bitfinex.com) currency exchange.

This ChatGPT plugin integrates with the Bitfinex Public API, enabling users to access data and analysis related to cryptocurrency trading within the ChatGPT environment.

### Development:

You can run this plugin on localhost.

To do that firstly clone this repository and run the `main.py` server.

`python main.py` 

It will start a server on `localhost:3333`

Open ChatGPT, open plugins, and select "Develop your own plugin" option.

- Enter localhost:3333 as the plugin URL.
- Install the plugin.
- You are now ready to use the plugin on GPT4.

You can issue the following commands, for example:

- "Analyze the candles for Bitcoin USD"
- "Give me the latest stats for Etherrum against USD"
- "What do you think about the current BTCUSD book?"
- "Compare the ETHUSD and BTCUSD tickers"

GPT4 will analyze the current market data and provide a response.

### License:

This plugin is licensed under the MIT license, allowing you to do whatever you want with it.

### Contributing:

Contributions are welcome. Please open a pull request (PR) to contribute to the project.
