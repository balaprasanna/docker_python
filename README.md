## Steps to build this image

## To Build
```
docker build -t hello_flask .
```

## To Run
```
docker run -d -p 3000:3000 hello_flask
```

## To tag
```
docker tag hello_flask balanus/hello_flask
```

## To push
```
docker push balanus/hello_flask
```

## To pull
```
docker pull balanus/hello_flask
```