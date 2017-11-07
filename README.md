# BMV INFO API

API to extract data from the BMV website.

## Usage

Base url: https://bmv-info-api.herokuapp.com

#### Stocks

**Statistics**

This service returns the statistics for a given stock 
available at the BMV (see: https://www.bmv.com.mx/es/emisoras/estadisticas). 

Perform a get request replacing _stock_ with the ticker of a
mexican (BMV) stock:

* https://bmv-info-api.herokuapp.com/stocks/statistics/ + stock

Example:

This example illustrates how to get the BMV-statistics for AC. 

Use a bash to perform a get request.

```bash
curl https://bmv-info-api.herokuapp.com/stocks/statistics/AC
```

Or python:

```python
import requests
stock_statistics = requests.get("https://bmv-info-api.herokuapp.com/stocks/statistics/AC").json()
print(stock_statistics)
```


#### add
[add content]

## Development and deployment

[add content]

## Configure instance

#### Creation 

```bash
heroku create bmv-info-api
```

#### Add buildpacks

```bash
heroku buildpacks:set heroku/python
heroku buildpacks:add heroku buildpacks:add --index 1 https://github.com/stomita/heroku-buildpack-phantomjs.git
```

## TODO

