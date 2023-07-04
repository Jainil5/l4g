    import openai
    from flask import Flask,make_response
    from flask_restful import Api,Resource,reqparse
    import os 
    import boto3
    import json

    app = Flask(__name__)

    api = Api(app)

    x = boto3.client('lambda')

    openai.api_key = os.getenv('OPENAI_TOKEN')
    lambdaName = os.getenv('SQL_SCHEMA_LAMBDA')
    schema_input =x.invoke(FunctionName=lambdaName,InvocationType="RequestResponse")
    fetch = schema_input["Payload"].read()
    schema = json.loads(fetch)

    tables = []
    for i in schema:
        tables.append(i)
    print("Tables:",tables)

    messages = []
    pre_prompt = """
                    ### We are providing you MySQL database with some tables with its properties as our database.
                    ### SF in prefix is for Salesforce data
                    ### SM in prefix is for SurveyMonkey data
                    ### L4G in prefix is for Listen4Good data
                        """
    messages.append({"role":"user","content":pre_prompt})

    for i in schema:
        pre = "# Table {} has properties: {} ."
        add = pre.format(i,schema[i])
        messages.append({"role":"user","content":str(add)})
        

    def ask(input):

        text = str(input).strip()
        prompt = f"""
        # On basis of above table and its properties, generate SQL query for {text}. The output should only be the SQL query without any other texts.
        # The output should just be as SQL Query or give error but dont print "reply" or anything else.
        """
        messages.append({"role":"user","content":prompt})
        response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role":"assistant" , "content":"reply"})
        
        return reply


    class Generate(Resource):

        def post(self):
            parser = reqparse.RequestParser()
            
            parser.add_argument('input', type=str, required=True)
            args = parser.parse_args()        
            print(args)
            
            input = args['input']  
            response = ask(input)
            return {"response":response}
        
        def get(self):
            return schema

    api.add_resource(Generate,"/query")



    #          sls deploy --aws-profile ag-dev@l4g -f api

