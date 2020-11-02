import sqlite3
import json


DB_response = ""


def dictionary_to_json(JSONdictionary):
    dict_string = JSONdictionary
    json_response = json.dumps(dict_string) #dictionary converted to string
    final_json_response = json.loads(json_response) #string is converted to JSON
    return final_json_response

def get(DB_request):
    if DB_request == "MAIN":

        #Create an empty dictionary to contain all objects with their attributes
        json_response = {0:{},1:{},2:{},3:{}}

        #create each dictionary for item
        for i in range(4):
            json_response[i]["img_url"] = ""
            json_response[i]["product_title"] = ""
            json_response[i]["price"] = 0.0

        #Make request to the datbase file and acess the most recent
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute("SELECT * FROM product WHERE Manufacturer == 'apple'")
        DB_response = c.fetchmany(4)
        conn.commit()
        conn.close()


        #update values from the retrived results
        #in range of the length of the response to prevent errors with NULL entries
        for i in range(len(DB_response)):
            json_response[i]["img_url"] = DB_response[i][4]
            json_response[i]["product_title"] = DB_response[i][8]
            json_response[i]["price"] = DB_response[i][3]

        #call method to convert the dictionary to JSON
        json_response = dictionary_to_json(json_response)
        return json_response
