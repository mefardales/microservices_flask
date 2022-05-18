from flask import Flask, jsonify,request
from marvel import Marvel
import pandas as pd
import json


app = Flask(__name__)

#Api Information
m = Marvel("678820154589bdd4732be5f67dcf6fd7","3f4c838e8fc1832c75b205797ad117407cf80b48") 

@app.route("/searchComics/", methods=["GET"])
def searchComics():
    #0 characters
    #1 comics
    debut = ['comics','series','stories','events']
    data = request.json['data']
    type = data['type']
    filter = data['filter']
    name = filter['name']
    
    if type == 0 :
        print ('Characters')
        all_characters = m.characters.all(nameStartsWith=name)
        df_characters = pd.DataFrame(all_characters["data"]["results"])
        
        #Count debut character
        c = 0
        for i in debut:
            c += int(df_characters[i][0]["returned"])
            
        output = {'id':int(df_characters["id"][0]),
            'name':name,
            'image':df_characters["thumbnail"][0]["path"] + ".jpg",
        'appearances':c}
        
        return jsonify(output)
    elif type == 1:
        print ('Comics')
        name_comic = []
        all_comics = m.comics.all()
   
                # name_comic.append(output_comics[i]["variants"]["name"])
        # output2 = {'id':all_comics.get(id) ,
        #             'title':'',
        #             'description':'',
        #             'onsaleDate':''}
   
    return jsonify({'Out':'200'})

if __name__ == '__main__':
   app.run(debug = True)