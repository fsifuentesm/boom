# Interview / phonenumbers

### Requirements

It is necessary to have `Docker` and `CURL` installed.

### Run

```
mkdir interview
cd interview
git clone git@github.com:fsifuentesm/boom.git
cd boom
cd boom
sudo docker-compose up
```
## Result
The project get a `numbers.csv` from `POST` request and return a `output.csv`created with the [phonenumbers library](https://pypi.org/project/phonenumbers/) granted.

### CULR COMMAND
```
curl -i -X POST -H "Content-Type: multipart/form-data" -F "numbers=@numbers.csv" http://localhost:9000/locate_numbers
```

Readme created with [stackedit.io](https://stackedit.io/app#)
