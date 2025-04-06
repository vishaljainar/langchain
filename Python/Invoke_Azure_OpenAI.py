import getpass # get user input without echoing the characters on the screen
import os # a way to interact with the operating system, allowing you to perform tasks like managing files, directories, and accessing environment variables. 

def fn_load_env_variables():
    
    try:
        # load environment variables from .env file (requires `python-dotenv`)
        from dotenv import load_dotenv

        load_dotenv() # load environment variables from .env file
    except ImportError:
        pass

# print("OpenAI API Key:", os.environ.get("OPENAI_API_KEY"))
# print("LangSmith API Key:", os.environ.get("LANGSMITH_API_KEY"))

def fn_invoke_model(input):
    from langchain_openai import AzureChatOpenAI

    #handle creation for Azure model
    model = AzureChatOpenAI(
        # azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    )

    from langchain_core.messages import HumanMessage, SystemMessage

    messages = [
        SystemMessage(""),
        HumanMessage(input),
    ]

    model.invoke(messages)

    for token in model.stream(messages):
        print(token.content, end="")

def fn_read_env_vars():

    os.environ["LANGSMITH_TRACING"] = "true"

    if "LANGSMITH_API_KEY" not in os.environ:
        os.environ["LANGSMITH_API_KEY"] = getpass.getpass(
            prompt="Enter your LangSmith API key (optional): "
        )
        
    if "LANGSMITH_PROJECT" not in os.environ:
        os.environ["LANGSMITH_PROJECT"] = getpass.getpass(
            prompt='Enter your LangSmith Project Name (default = "default"): '
        )

    if not os.environ.get("LANGSMITH_PROJECT"):
            os.environ["LANGSMITH_PROJECT"] = "default"        

    if not os.environ.get("AZURE_OPENAI_API_KEY"):
        os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass("Enter API key for Azure: ")

    if not os.environ.get("AZURE_OPENAI_ENDPOINT"):
        os.environ["AZURE_OPENAI_ENDPOINT"] = getpass.getpass(
            prompt="Enter endpoint for Azure (default = 'https://<your-resource-name>.openai.azure.com/'): "
        )

    if not os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME"):
        os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"] = getpass.getpass(
            prompt="Enter deployment name for Azure (default = 'gpt-35-turbo'): "
        )

    if not os.environ.get("AZURE_OPENAI_API_VERSION"):
        os.environ["AZURE_OPENAI_API_VERSION"] = getpass.getpass(
            prompt="Enter API version for Azure (default = '2023-05-15'): "
        )

def fn_main():
    # Load environment variables from .env file
    fn_load_env_variables()

    # Call the function to read environment variables
    # fn_read_env_vars()

    # Call the function to invoke the model
    fn_invoke_model("What is full form of RAG in AI ML? Give me only the full form.. nothing else")

def fn_connect_to_oracle():
    # Placeholder function for connecting to Oracle database
    try:
        # import cx_Oracle
        import oracledb
        # import os

        conn = oracledb.connect(user='COSVT02', password='c0Yest1#29', host='10.3.70.82', port=1521, service_name='BPATA01Q')

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM study_site_details")

        for row in cursor:
            print(row)

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\q764391\Downloads\instantclient-basiclite-windows.x64-23.7.0.25.01")

        # dsn = cx_Oracle.makedsn("10.3.70.82", port, sid="your_sid")
        # connection = cx_Oracle.connect(user="username", password="password", dsn=dsn)
        # print("Connected to Oracle Database:", connection.version)
        # connection.close()

        # hostname = os.environ.get("ora_hostname")
        # port = os.environ.get("ora_port")
        # sid = os.environ.get("ora_sid")
        # Connect to Oracle database
        # dsn = f"(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=10.3.70.82)(PORT=1521))(CONNECT_DATA=(SID=BPATA01Q)))"
        # print(dsn)
        # connection = cx_Oracle.connect(user="COSVT02", password="c0Yest1#29", dsn=dsn)

        # # dsn = cx_Oracle.makedsn(os.environ.get("ora_hostname"), os.environ.get("ora_sid"), service_name="service_name")
        # # connection = cx_Oracle.connect(user=os.environ.get("ora_username"), password=os.environ.get("ora_password"), sid=os.environ.get("ora_dsn"))
        # print("Connected to Oracle database")
    # except cx_Oracle.DatabaseError as e:
    #     error, = e.args
    #     print("Oracle error code:", error.code)
    #     print("Oracle error message:", error.message)
    # except ImportError:
    #     print("cx_Oracle module is not installed. Please install it to connect to Oracle database.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Close the connection if it was established
        try:
            connection.close()
        except NameError:
         pass

if __name__ == "__main__":
    fn_main()
    # fn_connect_to_oracle()
