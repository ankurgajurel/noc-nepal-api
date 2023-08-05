# noc-nepal-api

noc-nepal-api is an unofficial API for data related to petrol, diesel, and LPG.

## Installation

Install my-project with pip3

1. Clone the repository: 

```sh
git clone https://github.com/ankurgajurel/noc-nepal-api.git
```

2. Create a virtual environment

```sh
pip3 install virtualenv
python3 -m virtualenv venv 
source ./venv/bin/activate
```

3. Install the required dependencies: 

```sh
pip install -r requirements.txt
```
    
## Run Locally

1. Launch the application: 

```sh
python app.py
```

2. Access noc-nepal-api through your web browser at `http://localhost:3000`.
## API Reference

#### Get prices

```http
  GET /{view}
```

| View |  Description                |
| :--------  :------------------------- |
| `petrol` | price for petrol from each naaka |
| `diesel` |  price for diesel from each naaka |
| `lpg` | price for lpg from each naaka |



## Related

Here are some related projects

[rashifal-api](https://github.com/ankurgajurel/rashifal-api)\
[nepse-cli](https://github.com/ankurgajurel/nepse-cli)\
[share-file](https://github.com/ankurgajurel/share-files)\
[career-sangraha](https://github.com/ankurgajurel/career-sangraha)


## Authors

- [@ankurgajurel](https://www.github.com/ankurgajurel)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Support

For support, email ankurgajurel02@gmail.com

