# BMV INFO API

API to extract data from the BMV website. 

## USAGE

## NOTES

Create instance: 

```heroku create bmv-info-api```

### Add buildpacks

```
heroku buildpacks:set heroku/python
heroku buildpacks:add eroku buildpacks:add --index 1 https://github.com/stomita/heroku-buildpack-phantomjs.git
```

### Buildpack url

```
heroku config:add BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git
```

### PhantomJS Lib

```
heroku config:add LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:/lib:/app/vendor/phantomjs/lib
```

## TODO