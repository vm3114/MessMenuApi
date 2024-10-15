
# Mess Menu API

[MessMenuAPI](https://messmenuapi.onrender.com/doc) is an API that scrapes current day's mess menu from https://www.ssms-pilani.in/ and returns json data (For Bits Pilani - Pilani Campus).


## Documentation

You can check out the official documentation [here](https://messmenuapi.onrender.com/doc).


## Features

- Fetch menu for the current day, the next day, or any specified day.
- Update the menu for a single day or a range of days and then fetch it.
- This API supports fetching or updating menus for a custom range of days.
## Run Locally


#### 1. Clone the Repository

```bash
  git clone https://github.com/vm3114/MessMenuApi
  cd MessMenuApi
```

#### 2. Set up a Virtual Environment

```bash
python3 -m venv env
env\Scripts\activate
```
#### 3. Install Dependencies  

```bash 
pip install -r requirements.txt
```

#### 4. Removing the service object initialization in  line 26 of `functions.py`
  change ```
driver = webdriver.Chrome(service=service,options=chrome_options) ```

  to ```driver = webdriver.Chrome(options=chrome_options)```

#### 5. Run the FastAPI Application
```bash   
fastapi dev app.py    
```
## API Reference


#### Get menu for a certain day

```
  GET /get
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `day` | `string` | Default value is the current day |

#### Update (from SSMS website) and return menu for a certain day

```
  GET /update
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `day`      | `string` | Same as /get |

#### Get/Update menu for a range of days
```
  GET /getall or GET /updateall
```

| Parameters | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `start`      | `string` | Start of range. Inclusive. Default Monday. |
| `end`      | `string` | End of range. Inclusive. Default Sunday. |

#### Response codes

| Code | Description     | 
| :-------- | :---------------- | 
| `0`      | No error | 
| `1`      | Unable to get/update menu. Usually due to SSMS site not being updated. | 
| `2`      | Query parameter(s) passed are invalid.  | 

## Contributing

Feel free to fork this repository, make improvements, and create a pull request. Contributions and suggestions are always welcome!


## Feedback and Support
For any kind of feedback/support/suggestions, please reach out to me at vm311436@gmail.com.

