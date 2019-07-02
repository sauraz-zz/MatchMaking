# Skill Based MatchMaking

Skill based MatchMaking finds unique matches of M vs M players depending on their Score.
The matches are sorted based on the quality of each match. 
The quality of each match is defined by the closeness of minimum difference between the teams.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.7
```

### Installing

A step by step series of examples that tell you how to get a development env running

```
1. git clone
2. cd sostronk
3. pip3 install virtualenv
4. virtualenv .venv
5. source .venv/bin/activate
6. python -m pip install -r requirements.txt
7. python app.py
```

### Future Works

- MatchMaking can be deployed as a web server.
- Dockerfile with hot-reloading


## Running the tests - Unit Testing

To make use of random inputs change `config.json`

Run the following command
```
python -m unittest utils_test
```


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/sauraz) for details on our code of conduct, and the process for submitting pull requests to us.
 

## Authors

* **Saurav Sarkar** - *Initial work* - [sauraz](https://gist.github.com/sauraz)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

