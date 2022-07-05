# transaction

## Running the project

To run the project, we have to use the following commands

**Step1**: clone the repository

```
git clone https://github.com/aqifcse/transaction.git
```

**Step 2**: Enter the directory
```
cd transaction
```

**Step 3**: Create virtual environment
```
virtualenv venv && source venv/bin/activate
```

**Step 4**: Install Packages from requirements.txt 
```
pip install -r requirements.txt
```

**Step 5**: Migrate
```
Python manage.py migrate
```

**Step 6**: Run the Server
```
python manage.py runserver
```

## Test the API Endpoint

**Hit on the following link with postman or curl**

```
http://127.0.0.1:8000/api/v1/transaction/
```
In Postman select raw_data -> JSON And **POST** the following dictionary data

```
{
    "sent_from": 2,
    "sent_to":[
        3,
        4
    ], 
    "sent_at": "2022-07-03T08:53:05Z",
    "amount_sent": 580.34  
}
```

This 2, 3, 4 are pk id of the user. Here User id 2 is sending 580.34 balance to User Id 3 and 4. Before testing the api, you have to create users from the admin panel.

To see the transaction History simply **GET** request the upper URL with no input of data.

To sent the balance at **NOW** simply remove the 'sent_at' key and it's value and **POST** rest of the input. The program by default, takes **NOW** as a sent_at input.

Thank you!!!!

