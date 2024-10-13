
# Mess Menu API

An API that scrapes current day's mess menu from https://www.ssms-pilani.in/ and returns json data (For Bits Pilani - Pilani Campus).


## Documentation

You can check out the official documentation [here](https://messmenuapi.onrender.com/doc).


## Features

- **Retrieve Menu**: Fetch the menu for today, tomorrow, or any specified day.
- **Update Menu**: Update the menu for a single day or a range of days and then fetch it.
- **Day Range Support**: Supports fetching or updating menus for a custom range of days (e.g., from Tuesday to Friday).

## API Reference


#### Get menu for a certain day

````
  GET /get
````

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `day` | `string` | Default value is the current day |

#### Update (from SSMS website) and return menu for a certain day

````
  GET /update
````

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `day`      | `string` | Same as /get |

#### Get/Update menu for a range of days
````
  GET /getall or GET /updateall
````

| Parameters | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `start`      | `string` | Start of range. Inclusive. Default Monday. |
| `end`      | `string` | End of range. Inclusive. Default Sunday. |


## Contributing

Feel free to fork this repository, make improvements, and create a pull request. Contributions and suggestions are always welcome!


## Feedback

If you have any feedback, please reach out to me at vm311436@gmail.com

