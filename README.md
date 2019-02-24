# Sell Orders APP


## Application to create sell orders with Client and Product.
### Rules:
* The quantity of product in the order must be a multiplier value of the product multiplier
* The application recommends the price of the product when creating the order, but the user can change this value to any number greater than zero
* If the price of the product in the order is greater than the value of the product, the order will have an optimum profitability
* If the price of the product in the order is equal to or up to 10% lower than the value of the product, the order will have a good profitability
* If the product price on the order is less than 10% less product value, the order will have a poor return.

## Demo
http://lucasgms.pythonanywhere.com/


## Requirements
* Docker: 	https://docs.docker.com/install/linux/docker-ce/ubuntu/
* Docker compose: 	https://docs.docker.com/compose/install/
## Setting up

##### Clone the repo
```
$ git clone https://github.com/Lucasgms/sell-orders-app.git
$ cd sell-orders-app
```

#### Run docker-compose build
```
$ docker-compose up --build
```

#### Test the app locally on http://localhost:5000
