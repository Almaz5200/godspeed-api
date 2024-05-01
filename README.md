# Godspeed-API

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python API wrapper for [Godspeed](https://godspeedapp.com/). 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Godspeed-API.

```bash
pip install godspeed-api
```

## Features

- Task creation (`create_task`)
- Task modification (`update_task`)
- Paginated task query (`list_tasks`)

## Usage
```python
from godspeed_api import API

api = API("your-username", "your-password")

# to create a task
api.create_task(
    title='Your Task Title', 
    list_id='list_id', 
    location='location', 
    notes='notes', 
    due_at=datetime.datetime.now(), 
    # Note that current godspeed api will fail to add a task with new label_names, however it will not throw an error
    label_names=['label1', 'label2']
)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
