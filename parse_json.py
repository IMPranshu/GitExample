import json

jsonstr = """ {
    "people":[
        {
            "Id": "1",
            "FirstName": "Pk",
            "LastName": "Agrawal",
            "Email": "pranshuk@gmail.com"
        },
        {
            "Id": "2",
            "FirstName": "Ck",
            "LastName": "Agrawal",
            "Email": "cranshuk@gmail.com"
        },
        {
            "Id": "3",
            "FirstName": "Bk",
            "LastName": "Agrawal",
            "Email": "vranshuk@gmail.com"
        },
        {
            "Id": "4",
            "FirstName": "lk",
            "LastName": "Agrawal",
            "Email": "lranshuk@gmail.com"
        }
    ]
}"""

# jsonobj = json.loads(jsonstr)

# print(jsonobj)

jsonobj = json.load(open('sample_json.json'))
print(jsonobj['people'])
